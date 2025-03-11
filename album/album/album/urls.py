"""
URL configuration for album project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#aca importamos las vistas de la app en este caso fotos por que solo es una pero si tu tambien quieres solo un url con muchas apps lo repites als veces que quieras
from apps.Fotos import views


urlpatterns = [
    #bueno aca se linkean las urls con las vistas yo solo tengo esta pero puedes crear una por app y despues importar lo aca (me dio flojera pero seria una buena practica)
    #primero tenemos las paginas que se mostraran en el navegador y las que tienen un html recuerda que estos se crearon en views para que sepa que html abrir
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('noticias/', views.noti, name='noti'),
    path('Juego/', views.game, name='game'),
    
    #bueno de aqui para abajo si te das cuenta los metosdos views.subir_foto o view.* son los metodos que creamos en views.py
    #y los estamos usando aca por que le queremos decir que cuadno vaya a una ruta sea subir_foto o eliminar_fotos ejecute el metodo que creamos
    #si te das cuenta los metodos eliminar reciben el id desde la url como te decia yo lo hice con el metodo GET pero tu podrias hacerlo con el metodo post
    path('subir_foto/', views.subir_foto, name='subir_foto'),
    path('eliminar_fotos/<int:foto_id>/', views.eliminar_fotos, name='eliminar_fotos'),
    path('subir_noticia/', views.subir_noticia, name='subir_noticia'),
    path('eliminar_noticias/<int:noticia_id>/', views.eliminar_noticias, name='eliminar_noticias'),
]
