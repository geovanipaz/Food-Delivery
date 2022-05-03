from multiprocessing import context
from django.shortcuts import render
from django.views import View
from .models import Categoria, MenuItem, Pedido
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
            
        pedido = Pedido.objects.create(preco=preco)
        pedido.itens.add(*itens_id)
        
        context = {
            'itens': itens_pedido['itens'],
            'preco':preco,
            
        }
        return render(request, 'clientes/pedidos_confirmacao.html', context)
        