from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()

router.register("usuarios", views.UsuarioViewSet)
router.register("tipo_usuarios", views.Tipo_UsuarioViewSet)
router.register("contendios", views.ContendioViewSet)
router.register("tipo_contenidos", views.Tipo_ContenidoViewSet)
router.register("comentarios", views.ComentarioViewSet)
router.register("catalogos", views.CatalogoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]