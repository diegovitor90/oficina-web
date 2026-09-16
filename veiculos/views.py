from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from .forms import VeiculoForm
from .models import Veiculo


def lista(request):
    veiculos = Veiculo.objects.all()
    paginator = Paginator(veiculos, 10)
    pagina = request.GET.get('page')
    return render(request, 'veiculos/lista.html', {'veiculos': paginator.get_page(pagina)})


def cadastrar(request):
    if request.method == 'POST':
        form = VeiculoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Veículo cadastrado com sucesso.')
            return redirect('veiculos:lista')
    else:
        form = VeiculoForm()
    return render(request, 'veiculos/form.html', {'form': form, 'modo': 'novo'})


def detalhe(request, pk):
    veiculo = get_object_or_404(Veiculo, pk=pk)
    return render(request, 'veiculos/detalhe.html', {'veiculo': veiculo})


def editar(request, pk):
    veiculo = get_object_or_404(Veiculo, pk=pk)
    if request.method == 'POST':
        form = VeiculoForm(request.POST, instance=veiculo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Veículo atualizado com sucesso.')
            return redirect('veiculos:lista')
    else:
        form = VeiculoForm(instance=veiculo)
    return render(request, 'veiculos/form.html', {'form': form, 'modo': 'editar', 'veiculo': veiculo})


def excluir(request, pk):
    veiculo = get_object_or_404(Veiculo, pk=pk)
    if request.method == 'POST':
        veiculo.ativo = False
        veiculo.save()
        messages.success(request, 'Veículo desativado com sucesso.')
        return redirect('veiculos:lista')
    return render(request, 'veiculos/detalhe.html', {'veiculo': veiculo, 'confirmar_desativacao': True})


def desativar(request, pk):
    return excluir(request, pk)
