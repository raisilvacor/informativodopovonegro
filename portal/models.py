from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Categorias"

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.TextField(blank=True)
    conteudo = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='noticias')
    imagem = models.ImageField(upload_to='noticias/', blank=True, null=True)
    destaque = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo

class MemoriaViva(models.Model):
    nome = models.CharField(max_length=200)
    tipo = models.CharField(max_length=100) # Mestre, Liderança, etc.
    depoimento = models.TextField()
    biografia = models.TextField()
    foto = models.ImageField(upload_to='memoria/', blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nome

class Participacao(models.Model):
    TIPO_CHOICES = [
        ('HISTORIA', 'Enviar História'),
        ('PERSONAGEM', 'Indicar Personagem'),
        ('EVENTO', 'Enviar Evento'),
        ('PARCERIA', 'Parceria Cultural'),
        ('VOLUNTARIO', 'Colaborador Voluntário'),
    ]
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} - {self.get_tipo_display()}"

class Configuracao(models.Model):
    instagram_url = models.URLField(verbose_name="URL do Instagram", blank=True, null=True)
    youtube_url = models.URLField(verbose_name="URL do YouTube", blank=True, null=True)
    email_contato = models.EmailField(verbose_name="E-mail de Contato", blank=True, null=True)

    class Meta:
        verbose_name = "Configuração do Site"
        verbose_name_plural = "Configurações do Site"

    def __str__(self):
        return "Configurações Gerais"
