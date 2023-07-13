from django.contrib import admin
from .models import Usuario, Tipo_Usuario, Contenido, Tipo_Contenido, Comentario, Catalogo

admin.site.register(Usuario)
admin.site.register(Tipo_Usuario)
admin.site.register(Contenido)
admin.site.register(Tipo_Contenido)
admin.site.register(Comentario)
admin.site.register(Catalogo)

