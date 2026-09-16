from django.urls import path

from . import views

app_name = 'pecas'

urlpatterns = [
    path('', views.lista, name='lista'),
    path('novo/', views.cadastrar, name='cadastrar'),
    path('<int:pk>/', views.detalhe, name='detalhe'),
    path('<int:pk>/editar/', views.editar, name='editar'),
    path('<int:pk>/excluir/', views.desativar, name='excluir'),
]
