from django.contrib.auth.decorators import login_required
from django.urls import reverse

from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView

from src.apps.board.models import Board


class BoardListView(ListView):
    model = Board
    paginate_by = 10
    template_name = 'board/list.html'
    context_object_name = 'boards'  # instead of object_list (as default)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_queryset(self):
        qs = super().get_queryset()
        qs.filter(owner=self.request.user)
        return qs.active()


class BoardDetailView(DetailView):
    model = Board
    template_name = 'board/detail.html'
    context_object_name = 'board'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['resource_url'] = reverse('board:detail', kwargs={'pk': self.get_object().id})
        return data
