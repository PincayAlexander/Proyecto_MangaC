from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import logout
from .models import *
from .forms import *
from django.shortcuts import render


# Página principal
def home_view (request):
    # raise Exception("Forzando un error 500 para probar la vista de error")
    mangas = tabla_mangas.objects.all()
    return render(request, "web_MangaC/index.html", {
        'mangas': mangas,
    })

# Inicio de sesión
class CustomLoginView(LoginView):
    template_name = "registration/login.html"
    AuthenticationForm = login_form

# Cerrar sesión
class CustomLogoutView(LogoutView):
    next_page = 'home'

# Registro de usuarios
def signup_view (request):
    return render(request, "registration/signup.html", {
        'form': signup_form()
    })

# Acerca de
def about_view (request):
    return render(request, "web_MangaC/about.html")

def error_404_view(request, exception):
    return render(request, '404.html', status=404)

def error_500_view(request):
    return render(request, '500.html', status=500)

# Capítulos de manga
@login_required
def chapter_view (request, mangaNombre):
    manga = get_object_or_404(tabla_mangas, nombre=mangaNombre)
    capitulos = tabla_capitulos.objects.filter(manga=manga.id)
    return render(request,"web_MangaC/chapter.html", {
        'manga': manga, 
        'capitulos': capitulos,
    })