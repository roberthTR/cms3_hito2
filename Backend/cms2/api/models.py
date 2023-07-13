from django.db import models

# Create your models here.

class Tipo_Usuario(models.Model): 
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
    
class Usuario(models.Model): 
    
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.CharField(max_length=100)
    tipoU = models.ForeignKey(Tipo_Usuario, on_delete=models.CASCADE)
    correo = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre+" - "+self.edad+" años - "+str(self.tipoU)
    
class Tipo_Contenido(models.Model): 
    
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Contenido(models.Model): 

    tipoC = models.ForeignKey(Tipo_Contenido, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=1000)
    keyMaster = models.CharField(max_length=100)
    fecha = models.DateField("%d/%m/%Y",auto_now=True)
    Usu = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.titulo+" - "+str(self.tipoC)+" - "+str(self.Usu)
    
class Comentario(models.Model): #falta editar _ str
    
    Usu = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    cont = models.ForeignKey(Contenido, on_delete=models.CASCADE)
    Descripcion = models.CharField(max_length=100)
    fecha = models.DateField(auto_now=True)
    valoracion = models.PositiveIntegerField(default=0)
    def __str__(self):
        return str(self.Usu)+" - "+str(self.cont)
    

class Catalogo(models.Model): #falta editar _ str
    
    cont = models.ForeignKey(Contenido, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.cont)
    
