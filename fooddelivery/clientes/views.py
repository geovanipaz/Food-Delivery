from multiprocessing import context
from django.shortcuts import render, redirect
from django.views import View
from .models import Categoria, MenuItem, Pedido
from django.core.mail import send_mail
# Create your views here.

class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request,'clientes/index.html')
    
class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'clientes/about.html')
    
class Pedidos(View):
    def get(self, request, *args, **kwargs):
       #obter todos os itens de cada categoria
        aperitivos = MenuItem.objects.filter(categoria__nome__contains = 'Aperitivo')
        entradas = MenuItem.objects.filter(categoria__nome__contains = 'Entrada')
        bebidas = MenuItem.objects.filter(categoria__nome__contains = 'Bebida')
        sobremesas = MenuItem.objects.filter(categoria__nome__contains = 'Sobremesa')
       #passar para o contexto
        context = {
            'aperitivos':aperitivos,
            'entradas':entradas,
            'bebidas':bebidas,
            'sobremesas':sobremesas
        }
       #renderizar o template
        return render(request,'clientes/pedidos.html', context)
    def post(self,request, *args, **kwargs ):
        nome = request.POST.get('name')
        email = request.POST.get('email')
        rua = request.POST.get('street')
        cidade = request.POST.get('city')
        estado = request.POST.get('state')
        cep = request.POST.get('zip')
        
        itens_pedido = {
            'itens':[]
        }
        itens = request.POST.getlist('items[]')
        
        for item in itens:
            menu_item = MenuItem.objects.get(pk__contains=int(item))
            print('-----------',menu_item)
            item_data = {
                'id':menu_item.pk,
                'nome':menu_item.nome,
                'preco':menu_item.preco
            }
            itens_pedido['itens'].append(item_data)
        preco = 0
        itens_id = []
        print(itens_pedido['itens'])
        for item in itens_pedido['itens']:
            preco += item['preco']
            itens_id.append(item['id'])
            
        pedido = Pedido.objects.create(
            preco=preco,
            nome=nome,
            email=email,
            rua=rua,
            cidade=cidade,
            estado=estado,
            cep=cep
            )
        pedido.itens.add(*itens_id)
        
        #Depois de tudo feito, envie e-mail de confirmação para o usuário
        corpo = ('Thank you for your order!  Your food is being made and will be delivered soon!\n'
        f'Your total: {preco}\n'
        'Thank you again for your order!')
        
        send_mail(
            'Thank You For Your Order!',
            corpo,
            'example@example.com',
            [email],
            fail_silently=False
        )
        
        context = {
            'itens': itens_pedido['itens'],
            'preco':preco,
            
        }
        return redirect('confirmacao_pedido', pk=pedido.pk)
        
class ConfirmacaoPedido(View):
    def get(self,request, pk, *args, **kwargs):
        pedido = Pedido.objects.get(pk=pk)
        context = {
            'pk': pedido.pk,
            'itens': pedido.itens,
            'preco': pedido.preco
        }
        
        return render(request, 'clientes/pedidos_confirmacao.html', context)
    
    def post(self,request, pk, *args, **kwargs):
        print(request.body)
        
class ConfirmacaoPagPedido(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'clientes/confirmacao_pag_pedido.html')