from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', include('cliente.urls')),
    path('veiculos/', include('veiculos.urls')),
    path('pecas/', include('pecas.urls')),
    path('servicos/', include('servicos.urls')),
    path('mecanicos/', include('mecanicos.urls')),
    path('fornecedores/', include('fornecedores.urls')),
    path('estoque/', include('estoque.urls')),
    path('ordens-servico/', include('ordens_servicos.urls')),
    path('financeiro/', include('financeiros.urls')),
    path('relatorios/', include('relatorios.urls')),
]