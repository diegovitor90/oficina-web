from django.shortcuts import render


def lista(request):
    return render(request, 'financeiros/lista.html')


def cadastrar(request):
    return render(request, 'financeiros/form.html')


def detalhe(request, pk):
    return render(request, 'financeiros/detalhe.html')


def editar(request, pk):
    return render(request, 'financeiros/form.html')


def excluir(request, pk):
    return render(request, 'financeiros/excluir.html')


def desativar(request, pk):
    return excluir(request, pk)
