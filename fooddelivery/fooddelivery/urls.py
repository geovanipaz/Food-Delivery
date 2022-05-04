
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from clientes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Index.as_view(), name='index'),
    path('about', views.About.as_view(), name='about'),
    path('pedido', views.Pedidos.as_view(), name='pedido'),
    path('confirmacao-pedido/<pk>', views.ConfirmacaoPedido.as_view(),
         name='confirmacao_pedido'),
    path('pagamento-confirmacao', views.ConfirmacaoPagPedido.as_view(),
         name='pagamento_realizado')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

