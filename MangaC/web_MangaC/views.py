from django.shortcuts import render, HttpResponse
from .models import *
from .forms import *
from django.shortcuts import redirect
#from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout

# Create your views here.
def home (request):
    mangas = tabla_manga_comic.objects.all()
    return render(request, "web_MangaC/index.html", {
        'mangas': mangas,
    })
"""
def login (request):
    return render(request, "web_MangaC/registration/login.html", {
        'form': login_form()
    })
"""
class CustomLoginView(LoginView):
    form = login_form

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/home')
    return redirect('/home')

def signup (request):
    return render(request, "web_MangaC/signup.html", {
        'form': signup_form()
    })

def about (request):
    return render(request, "web_MangaC/about.html")

def contact (request):
    return render(request, "web_MangaC/contact.html")

@login_required
def manga_lect (request):
    capitulos = tabla_capitulos.objects.all()
    mangas = tabla_manga_comic.objects.all()
    return render(request,"web_MangaC/lectura.html", {
        'capitulos': capitulos,
        'mangas': mangas, 
    })