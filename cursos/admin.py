from django.contrib import admin

from .models import Curso, Avaliacao

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'url', 'criacao', 'atualizacao', 'ativo')

@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('curso', 'nome', 'email', 'avaliacao', 'criacao', 'atualizacao', 'ativo')
    # list_filter = ('curso', 'avaliacao', 'ativo')
    # search_fields = ('nome', 'email', 'comentario')
    # autocomplete_fields = ('curso',)
