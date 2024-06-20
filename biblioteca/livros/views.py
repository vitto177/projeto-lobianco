from django.shortcuts import redirect
from .models import Livros, Emprestimo

def listar_livros(request):
    livros = Livro.objects.all()  # Busca todos os livros
    contexto = {'livros': livros}  # Cria um contexto com os livros
    return render(request, 'livros/listar_livros.html', contexto)  # Renderiza o template


def listar_emprestimos(request):
    emprestimos = Emprestimo.objects.all()  # Busca todos os empréstimos
    contexto = {'emprestimos': emprestimos}  # Cria um contexto com os empréstimos
    return render(request, 'livros/listar_emprestimos.html', contexto)  # Renderiza o template
