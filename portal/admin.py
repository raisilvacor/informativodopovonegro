from django.contrib import admin
from .models import Categoria, Noticia, MemoriaViva, Participacao, Configuracao

@admin.register(Configuracao)
class ConfiguracaoAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Impede adicionar mais de uma configuração
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        # Impede deletar a configuração
        return False

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nome',)}

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'data_publicacao', 'destaque')
    list_editable = ('destaque',)
    list_filter = ('categoria', 'data_publicacao', 'destaque')
    search_fields = ('titulo', 'conteudo')

@admin.register(MemoriaViva)
class MemoriaVivaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo')
    search_fields = ('nome', 'biografia')

@admin.register(Participacao)
class ParticipacaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'data_envio')
    list_filter = ('tipo', 'data_envio')
    readonly_fields = ('data_envio',)
