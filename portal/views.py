from django.shortcuts import render, redirect
from .models import Noticia, Categoria, MemoriaViva, Participacao
from django.contrib import messages

def home(request):
    noticias_recentes = Noticia.objects.order_by('-data_publicacao')[:3]
    noticias_destaque = Noticia.objects.filter(destaque=True).order_by('-data_publicacao')
    return render(request, 'portal/home.html', {
        'noticias_recentes': noticias_recentes,
        'noticias_destaque': noticias_destaque
    })

def quem_somos(request):
    return render(request, 'portal/quem_somos.html')

def noticias_list(request):
    categorias = Categoria.objects.all()
    noticias = Noticia.objects.all().order_by('-data_publicacao')
    return render(request, 'portal/noticias.html', {'noticias': noticias, 'categorias': categorias})

def memoria_viva(request):
    memorias = MemoriaViva.objects.all()
    return render(request, 'portal/memoria_viva.html', {'memorias': memorias})

def territorios(request):
    return render(request, 'portal/territorios.html')

def multimidia(request):
    return render(request, 'portal/multimidia.html')

def participe(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        tipo = request.POST.get('tipo')
        mensagem = request.POST.get('mensagem')
        Participacao.objects.create(nome=nome, email=email, tipo=tipo, mensagem=mensagem)
        messages.success(request, 'Sua mensagem foi enviada com sucesso!')
        return redirect('participe')
    return render(request, 'portal/participe.html')
