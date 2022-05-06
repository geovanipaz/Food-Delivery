from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.utils.timezone import datetime
from clientes.models import Pedido
# Create your views here.

class Dashboard(LoginRequiredMixin, UserPassesTestMixin, View):
    def get(self, request, *args, **kwargs):
        #pega a atual data
        hoje = datetime.today()
        pedidos = Pedido.objects.filter(criado__year=hoje.year,
                                        criado__month=hoje.month,
                                        criado__day=hoje.day)
        
        #loop sobre os pedidos e adiciona o preço
        total_receita = 0
        pedidos_naoenviados = []
        for pedido in pedidos:
            total_receita +=pedido.preco
            
            if not pedido.ja_enviado:
                pedidos_naoenviados.append(pedido)
        
        #passe o numero total de pedidos e o total da receita para o template
        context = {
            'pedidos':pedidos,
            'total_receita':total_receita,
            'total_pedidos':len(pedidos)
        } 
        return render(request, 'restaurante/dashboard.html', context)
    def test_func(self):
        return self.request.user.groups.filter(name='Staff').exists()
    
class PedidoDetalhe(LoginRequiredMixin, UserPassesTestMixin, View):
    def get(self, request, pk, *args, **kwargs):
        pedido = Pedido.objects.get(pk=pk)
        context = {'pedido':pedido}
        
        return render(request, 'restaurante/pedido_detalhe.html', context)
    
    def post(self, request, pk, *args, **kwargs):
        pedido = Pedido.objects.get(pk=pk)
        pedido.ja_enviado = True
        pedido.save()
        context = {'pedido':pedido}
        
        return render(request, 'restaurante/pedido_detalhe.html', context)
    
    def test_func(self):
        return self.request.user.groups.filter(name='Staff').exists()