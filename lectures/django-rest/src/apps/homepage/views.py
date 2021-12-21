from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['dog_name'] = 'Ichigo'
        return data
