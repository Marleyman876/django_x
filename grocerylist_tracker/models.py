# from os import name
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.

class Food_item(models.Model):
  name = models.CharField(max_length=64)
  purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
  description = models.TextField(max_length=250)
  
  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('food_item_detail', args=[str(self.id)])
  