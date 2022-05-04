from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.nome

class MenuItem(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='menu_imagens/')
    preco = models.DecimalField(max_digits=5,decimal_places=2)
    categoria = models.ManyToManyField(Categoria, related_name='item')
    
    def __str__(self) -> str:
        return self.nome
    
class Pedido(models.Model):
    criado = models.DateTimeField(auto_now_add=True)
    preco = models.DecimalField(max_digits=7, decimal_places=2)
    itens = models.ManyToManyField(MenuItem,related_name='pedido', blank=True)
    nome = models.CharField(max_length=50,blank=True)
    email = models.EmailField(max_length=50, blank=True)
    rua  = models.CharField(max_length=50, blank=True)
    cidade = models.CharField(max_length=50, blank=True)
    estado = models.CharField(max_length=15, blank=True)
    cep = models.IntegerField(blank=True, null=True)
    ja_pago = models.BooleanField(default=False)
    
    
    def __str__(self) -> str:
        return f'Pedido {self.criado.strftime("%b %d %Y %I:%M %p")}'

