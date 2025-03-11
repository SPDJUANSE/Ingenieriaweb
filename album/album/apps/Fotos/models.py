from django.db import models

# crear modelos aca si lo manejas en diferentes apps deberas crear el modelo correspondiente en cada app
# si lo manejas en una sola app puedes crear todos los modelos en este archivo
class Galeria(models.Model):
    Descripcion1 = models.CharField(max_length=90)
    Descripcion2 = models.CharField(max_length=2000)
    imageurl = models.CharField(max_length=120)
    
    def __str__(self):
        return self.Descripcion1 #retorna el nombre de la imagen    

class Noticias(models.Model):
    Titulo = models.CharField(max_length=90)
    descripcion = models.CharField(max_length=2000)
    Palabra = models.CharField(max_length=2000)
    imageurl = models.CharField(max_length=120)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Titulo #retorna el nombre de la noticia
    
    