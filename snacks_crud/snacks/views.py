from django.shortcuts import render
from .models import Snacks
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class SnackListview(ListView):
    model = Snacks
    template_name ='snack_list.html'
    context_object_name ='snacks'


class SnackDetailView(DetailView):
    model = Snacks
    template_name ='snack_detail.html'


class SnackCreateView(CreateView):
    model = Snacks
    template_name ='create.html'
    fields = '__all__'
    success_url = reverse_lazy('list')

class SnackUpdateView(UpdateView):
    model = Snacks
    template_name ='update.html'
    fields = '__all__'
    success_url = reverse_lazy('list')

class SnackDeleteView(DeleteView):
    model = Snacks
    template_name ='delete.html'
    success_url = reverse_lazy('list')




