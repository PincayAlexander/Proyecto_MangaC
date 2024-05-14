from django.shortcuts import render, HttpResponse
from .models import *

# Create your views here.
def home (request):
    mangas = tabla_manga_comic.objects.all()
   # genero = list(tabla_generos.objects.values())
    return render(request, "web_MangaC/index.html", {
        'mangas': mangas,
    })

def login (request):
    return render(request, "web_MangaC/login.html")

def signup(request):
    return render(request, "web_MangaC/signup.html")

def about (request):
    return render(request, "web_MangaC/about.html")

def contact (request):
    return render(request, "web_MangaC/contact.html")
