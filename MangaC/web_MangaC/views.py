from django.shortcuts import render, redirect, HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout


# Página principal
def home_view (request):
    mangas = tabla_mangas.objects.all()
    return render(request, "web_MangaC/index.html", {
        'mangas': mangas,
    })

# Inicio de sesión
class CustomLoginView(LoginView):
    template_name = "registration/login.html"
    form_class = login_form

# Cerrar sesión
def logout_view(request):
    logout(request)
    return redirect('/home')

# Registro de usuarios
def signup_view (request):
    return render(request, "registration/signup.html", {
        'form': signup_form()
    })

# Acerca de"
def about_view (request):
    return render(request, "web_MangaC/about.html")

# Capítulos de manga
@login_required
def manga_capitulos_view (request):
    capitulos = tabla_capitulos.objects.all()
    mangas = tabla_mangas.objects.all()
    return render(request,"web_MangaC/Chapter.html", {
        'capitulos': capitulos,
        'mangas': mangas, 
    })