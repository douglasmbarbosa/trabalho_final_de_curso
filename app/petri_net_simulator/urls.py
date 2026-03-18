from django.urls import path
from . import views

urlpatterns = [
    # Adicione suas URLs aqui
    path('', views.index, name='index'),
]