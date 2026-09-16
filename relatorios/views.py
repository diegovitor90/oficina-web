from django.shortcuts import render


def lista(request):
    return render(request, 'relatorios/lista.html')


def cadastrar(request):
    return render(request, 'relatorios/form.html')


def detalhe(request, pk):
    return render(request, 'relatorios/detalhe.html')


def editar(request, pk):
    return render(request, 'relatorios/form.html')


def excluir(request, pk):
    return render(request, 'relatorios/excluir.html')


def desativar(request, pk):
    return excluir(request, pk)
