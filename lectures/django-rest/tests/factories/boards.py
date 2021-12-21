import string

import factory
from factory import fuzzy

from src.apps.board.models import Board, Column, Comment, Task
from tests.factories.users import TrelloUserFactory


class BoardFactory(factory.django.DjangoModelFactory):
    name = fuzzy.FuzzyText(length=12, chars=string.ascii_letters, prefix='')
    owner = factory.SubFactory(TrelloUserFactory)

    class Meta:
        model = Board


class ColumnFactory(factory.django.DjangoModelFactory):
    name = fuzzy.FuzzyText(length=12, chars=string.ascii_letters, prefix='')
    board = factory.SubFactory(BoardFactory)

    class Meta:
        model = Column


class TaskFactory(factory.django.DjangoModelFactory):
    name = fuzzy.FuzzyText(length=12, chars=string.ascii_letters, prefix='')
    column = factory.SubFactory(ColumnFactory)
    created_by = factory.SubFactory(TrelloUserFactory)

    class Meta:
        model = Task


class CommentFactory(factory.django.DjangoModelFactory):
    message = fuzzy.FuzzyText(length=12, chars=string.ascii_letters, prefix='')
    task = factory.SubFactory(TaskFactory)
    owner = factory.SubFactory(TrelloUserFactory)

    class Meta:
        model = Comment
