from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('dashboard',views.Dashboard.as_view(),name='dashboard'),
    path('pedido/<pk>', views.PedidoDetalhe.as_view(), name='pedido_detalhe')
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
