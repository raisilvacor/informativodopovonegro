from .models import Configuracao

def configuracoes_gerais(request):
    config = Configuracao.objects.first()
    return {
        'config': config
    }
