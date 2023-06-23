from django.urls import path, include

from Recipes.common import views

urlpatterns = [
    path('', views.home, name='home')
]