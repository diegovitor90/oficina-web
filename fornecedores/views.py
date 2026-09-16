from django.shortcuts import render


def lista(request):
    return render(request, 'fornecedores/lista.html')


def cadastrar(request):
    return render(request, 'fornecedores/form.html')


def detalhe(request, pk):
    return render(request, 'fornecedores/detalhe.html')


def editar(request, pk):
    return render(request, 'fornecedores/form.html')


def excluir(request, pk):
    return render(request, 'fornecedores/excluir.html')


def desativar(request, pk):
    return excluir(request, pk)
