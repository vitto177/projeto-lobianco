from django.shortcuts import render

def listar_usuarios(request):
    usuarios = Usuario.objects.all()  # Busca todos os usuários
    contexto = {'usuarios': usuarios}  # Cria um contexto com os usuários
    return render(request, 'usuarios/listar_usuarios.html', contexto)