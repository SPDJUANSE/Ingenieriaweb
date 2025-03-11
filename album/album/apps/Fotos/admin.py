from django.contrib import admin

# Register your models here.
from .models import Galeria 
from .models import Noticias 

admin.site.register(Galeria)
admin.site.register(Noticias)