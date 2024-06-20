from django.contrib import admin
from .models import Livros, Emprestimos

class LivrosAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'genero']
    search_fields = ['titulo', 'autor', 'genero']

class EmprestimosAdmin(admin.ModelAdmin):
    list_display = ['nome_emprestado', 'livro', 'data_emprestimo', 'data_devolucao']
    search_fields = ['nome_emprestado', 'livro']
    list_filter = ['data_emprestimo', 'data_devolucao']

admin.site.register(Livros, LivrosAdmin)
admin.site.register(Emprestimos, EmprestimosAdmin)