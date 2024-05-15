from django.shortcuts import render, HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.models import User
#from django.contrib.auth.decorators import login_required
#from django.contrib.auth import logout, login, authenticate

# Create your views here.
def home (request):
    mangas = tabla_manga_comic.objects.all()
    return render(request, "web_MangaC/index.html", {
        'mangas': mangas,
    })

def login (request):
    return render(request, "web_MangaC/login.html", {
        'form': login_form()
    })

def signup (request):
#    User.objects.create(last_name=request.GET['apellido'], first_name=request.GET['nombre'],
#                       email=request.GET['correo'], password=request.GET['contraseña'], is_superuser=False)
    return render(request, "web_MangaC/signup.html", {
        'form': signup_form()
    })

def about (request):
    return render(request, "web_MangaC/about.html")

def contact (request):
    return render(request, "web_MangaC/contact.html")
