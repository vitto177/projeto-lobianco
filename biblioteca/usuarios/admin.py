from django.contrib import admin
from usuarios.models import usuario

@admin.register(usuario)
class usuarioAdmin(admin.ModelAdmin):
    list_display = ('nome','email')
    search_fields = ('nome', 'email')