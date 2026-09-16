from django.shortcuts import render


def lista(request):
    return render(request, 'servicos/lista.html')


def cadastrar(request):
    return render(request, 'servicos/form.html')


def detalhe(request, pk):
    return render(request, 'servicos/detalhe.html')


def editar(request, pk):
    return render(request, 'servicos/form.html')


def excluir(request, pk):
    return render(request, 'servicos/excluir.html')


def desativar(request, pk):
    return excluir(request, pk)
