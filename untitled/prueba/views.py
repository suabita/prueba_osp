from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView

from prueba.forms import PruebaDBForm
from prueba.models import Prueba


class PruebaListView(ListView):
    model = Prueba
    template_name = 'prueba/principal.html'

class PruebaCreateView(CreateView):
    model = Prueba
    template_name = 'prueba/create.html'
    form_class = PruebaDBForm
    success_url = reverse_lazy('prueba:principal')

class PruebaDetailView(DetailView):
    model = Prueba
    template_name = 'prueba/detail.html'

class PruebaUpdateView(UpdateView):
    model = Prueba
    template_name = 'prueba/create.html'
    form_class = PruebaDBForm
    success_url = reverse_lazy('prueba:principal')

