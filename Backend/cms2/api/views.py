from django.shortcuts import render
from rest_framework import viewsets
from . import models,serializers

# Create your views here.

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = models.Usuario.objects.all()
    serializer_class = serializers.UsuarioSerializers

class Tipo_UsuarioViewSet(viewsets.ModelViewSet):
    queryset = models.Tipo_Usuario.objects.all()
    serializer_class = serializers.Tipo_UsuarioSerializers

class ContendioViewSet(viewsets.ModelViewSet):
    queryset = models.Contenido.objects.all()
    serializer_class = serializers.ContenidoSerializers

class Tipo_ContenidoViewSet(viewsets.ModelViewSet):
    queryset = models.Tipo_Contenido.objects.all()
    serializer_class = serializers.Tipo_ContenidoSerializers
    
class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = models.Comentario.objects.all()
    serializer_class = serializers.ComentarioSerializers

class CatalogoViewSet(viewsets.ModelViewSet):
    queryset = models.Catalogo.objects.all()
    serializer_class = serializers.CatalogoSerializers