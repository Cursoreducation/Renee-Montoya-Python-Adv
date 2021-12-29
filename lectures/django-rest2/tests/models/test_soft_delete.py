import pytest

from src.apps.board.models import Board, Column, Task
from tests.factories.boards import BoardFactory, ColumnFactory, TaskFactory


class TestSoftDelete:

    MODELS_TO_CHECK = (
        (Board, BoardFactory),
        (Column, ColumnFactory),
        (Task, TaskFactory),
    )

    @pytest.mark.parametrize("model, factory_class", MODELS_TO_CHECK)
    @pytest.mark.django_db
    def test_delete_single_obj(self, model, factory_class):
        obj = factory_class()
        assert model.objects.active().count() == 1
        assert model.objects.deleted().count() == 0

        obj.delete()
        assert model.objects.active().count() == 0
        assert model.objects.deleted().count() == 1

    @pytest.mark.parametrize("model, factory_class", MODELS_TO_CHECK)
    @pytest.mark.django_db
    def test_delete_from_queryset(self, model, factory_class):
        factory_class()
        factory_class()
        factory_class()
        assert model.objects.active().count() == 3
        assert model.objects.deleted().count() == 0

        model.objects.all().delete()
        assert model.objects.active().count() == 0
        assert model.objects.deleted().count() == 3

    @pytest.mark.parametrize("model, factory_class", MODELS_TO_CHECK)
    @pytest.mark.django_db
    def test_hard_delete_from_queryset(self, model, factory_class):
        factory_class()
        factory_class()
        factory_class(is_deleted=True)
        assert model.objects.active().count() == 2
        assert model.objects.deleted().count() == 1

        model.objects.all().hard_delete()
        assert model.objects.active().count() == 0
        assert model.objects.deleted().count() == 0
        assert model.objects.count() == 0

    @pytest.mark.parametrize("model, factory_class", MODELS_TO_CHECK)
    @pytest.mark.django_db
    def test_hard_delete_single_obj(self, model, factory_class):
        obj = factory_class()
        assert model.objects.active().count() == 1
        assert model.objects.deleted().count() == 0

        obj.hard_delete()
        assert model.objects.active().count() == 0
        assert model.objects.deleted().count() == 0
        assert model.objects.count() == 0
    

