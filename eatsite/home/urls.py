from django.urls import path

from .views import Home,GetRecipe

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('recipe/<slug:slug>/', GetRecipe.as_view(), name='recipe')
]