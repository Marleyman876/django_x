from django.urls import path
from django.urls.resolvers import URLPattern
from .views import Food_item_add, Food_item_delete,Food_item_detail, Food_item_update, Food_item_list

urlpatterns = [
  path('', Food_item_list.as_view(), name='food_item_list'), 
  path('<int:pk>', Food_item_detail.as_view(), name='food_item_detail'),
  path('<int:pk>/update/', Food_item_update.as_view(), name='food_item_update'),
  path('add/', Food_item_add.as_view(), name='food_item_add'),
  path('<int:pk>/delete/', Food_item_delete.as_view(), name='food_item_delete'),
  
]