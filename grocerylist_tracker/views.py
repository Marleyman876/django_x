from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Food_item
from django.urls import reverse_lazy

# Create your views here.

class Food_item_list(ListView):
  template_name = 'food_item_list.html'
  model = Food_item
  
class Food_item_detail(DetailView):
  template_name = 'food_item_detail.html'
  model = Food_item
  
class Food_item_add(CreateView):
  template_name = 'food_item_create.html'
  model = Food_item
  fields = ['name','purchaser','description']
  
class Food_item_update(UpdateView):
  template_name = 'food_item_update.html'
  model = Food_item
  fields = ['name','purchaser','description']
  
class Food_item_delete(DeleteView):
  template_name = 'food_item_delete.html'
  model = Food_item
  success_url = reverse_lazy('food_item_list')