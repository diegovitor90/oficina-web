from django.shortcuts import render


def lista(request):
    return render(request, 'estoque/lista.html')


def cadastrar(request):
    return render(request, 'estoque/form.html')


def detalhe(request, pk):
    return render(request, 'estoque/detalhe.html')


def editar(request, pk):
    return render(request, 'estoque/form.html')


def excluir(request, pk):
    return render(request, 'estoque/excluir.html')


def desativar(request, pk):
    return excluir(request, pk)
