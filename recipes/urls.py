# recipes/urls.py

from django.urls import path     #serve para importar a função do path do módulo de urls do django
from . import views              #ter acesso a todas as funções e classes no arquivo views na pasta

urlpatterns = [
    path('', views.recipe_list, name='recipes_list'), #nova view para listar
    path('<int:pk>/', views.recipe_detail, name ='recipe_detail')
]