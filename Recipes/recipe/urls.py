from django.urls import path, include

from Recipes.recipe import views

urlpatterns = [
    path('create/', views.create_recipe, name='create_recipe'),
    path('edit/<int:pk>/', views.edit_recipe, name='edit_recipe'),
    path('delete/<int:pk>/', views.delete_recipe, name='delete_recipe'),
    path('details/<int:pk>/', views.details_recipe, name='details_recipe'),
]