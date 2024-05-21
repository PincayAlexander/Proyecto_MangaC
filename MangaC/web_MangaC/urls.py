
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from .views import CustomLoginView

urlpatterns = [
    path('', views.home, name="home"),
#    path('login/', views.login, name="login"),
    path("login/", CustomLoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name="logout"),
    path('signup/', views.signup, name="signup"),
    path('capitulos/', views.manga_capitulos, name="capitulos"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
]