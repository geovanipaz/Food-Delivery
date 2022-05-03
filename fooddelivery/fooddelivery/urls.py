
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from clientes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Index.as_view(), name='index'),
    path('about', views.About.as_view(), name='about'),
    path('pedido', views.Pedidos.as_view(), name='pedido')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

