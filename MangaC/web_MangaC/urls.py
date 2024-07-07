from django.urls import path
from . import views
from .views import CustomLoginView
from django.conf.urls import handler404, handler500

handler404 = 'web_MangaC.views.error_404_view'
handler500 = 'web_MangaC.views.error_500_view'


urlpatterns = [
    path('', views.home_view, name="home"),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name="logout"),
    path('signup/', views.signup_view, name="signup"),
    path('chapter/<str:mangaNombre>/', views.chapter_view, name="chapter"),
    path('about/', views.about_view, name="about"),
]