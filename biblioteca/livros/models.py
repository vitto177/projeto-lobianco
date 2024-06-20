from django.db import models
from datetime import date
import datetime
from usuarios.models import usuario

class Livros(models.Model):
    titulo = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    disponivel = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Livro'

    def __str__(self) -> str:
        return self.nome

class Emprestimos(models.Model):
    nome_emprestado = models.ForeignKey(usuario, on_delete=models.DO_NOTHING, blank = True, null = True)
    data_emprestimo = models.DateTimeField(default=datetime.datetime.now())
    data_devolucao = models.DateTimeField(blank = True, null = True)
    livro = models.ForeignKey(Livros, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return f"{self.nome_emprestado} | {self.livro}"