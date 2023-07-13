from rest_framework import serializers
from . import models

class UsuarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Usuario
        fields = '__all__'


class Tipo_UsuarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Tipo_Usuario
        fields = '__all__'


class ContenidoSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Contenido
        fields = '__all__'


class Tipo_ContenidoSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Tipo_Contenido
        fields = '__all__'


class ComentarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Comentario
        fields = '__all__'


class CatalogoSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Catalogo
        fields = '__all__'


