from django.shortcuts import render ,redirect, get_object_or_404
from django.http import JsonResponse
from .models import Galeria, Noticias

def index(request):
    imagenes = Galeria.objects.all()
    return render(request, 'pages/index.html', {'imagenes': imagenes})

def noti(request):
    noticias = Noticias.objects.order_by('-date')[:6]
    return render(request, 'pages/Noticias.html', {'noticias': noticias})

def game(request):
    return render(request, 'pages/Juego.html')

def eliminar_fotos(request, foto_id):
  foto = get_object_or_404(Galeria, id=foto_id)
  foto.delete()
  return redirect('index')

def subir_foto(request):
    if request.method == "POST" and request.FILES.get("imageurl"):
        Descripcion1 = request.POST.get("Descripcion1")
        Descripcion2 = request.POST.get("Descripcion2")
        imageurl = request.FILES["imageurl"]

        nueva_foto = Galeria(Descripcion1=Descripcion1, Descripcion2=Descripcion2, imageurl=imageurl)
        nueva_foto.save()

        return JsonResponse({"success": True})
    
    return JsonResponse({"success": False, "error": "Método no permitido"})


def eliminar_noticias(request, noticia_id):
    noticia = get_object_or_404(Noticias, id=noticia_id)
    noticia.delete()
    return JsonResponse({"success": True})

def subir_noticia(request):
    if request.method == "POST" and request.FILES.get("imageurl"):
        Titulo = request.POST.get("Titulo")
        descripcion = request.POST.get("descripcion")
        Palabra = request.POST.get("Palabra")
        imageurl = request.FILES["imageurl"]
        
        nueva_noticia = Noticias(Titulo=Titulo, descripcion=descripcion, Palabra=Palabra, imageurl=imageurl)
        nueva_noticia.save()

        return JsonResponse({"success": True})
    return JsonResponse({"success": False, "error": "Método no permitido"})
