from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

#Tabla "autores"
class tabla_autores(models.Model):
    Nombre = models.CharField(max_length=100)
    Apellido = models.CharField(max_length=100, null=True)
    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
    def __str__(self):
        return self.Nombre + ' ' + self.Apellido

#Tabla "generos"
class tabla_generos(models.Model):
    Nombre = models.CharField(max_length=100)
    Descripcion = models.TextField(null=True)
    class Meta:
        verbose_name = 'Género'
        verbose_name_plural = 'Géneros'
    def __str__(self):
        return self.Nombre

#Tabla "manga_comic"
class tabla_manga_comic(models.Model):
    Nombre = models.CharField(max_length=100)
    Genero = models.ForeignKey(tabla_generos, on_delete=models.CASCADE)
    Autor = models.ForeignKey(tabla_autores, on_delete=models.CASCADE, null=True, blank=True)
    Fech_publicacion = models.DateField(auto_now_add=True, verbose_name='Fecha de Publicación')
    Estado = models.CharField(max_length=20)
    Descripcion = models.TextField(null=True)
    class Meta:
        verbose_name = 'Manga/Comic'
        verbose_name_plural = 'Manga/Comic'
    def __str__(self):
        return self.Nombre + ' - ' + self.Genero.Nombre + ' - ' + self.Autor.Nombre

#Tabla "capitulos"
class tabla_capitulos(models.Model):
    Manga = models.ForeignKey(tabla_manga_comic, on_delete=models.CASCADE)
    Num_capitulo = models.IntegerField(verbose_name='Numero de capitulo')
    titulo = models.CharField(max_length=100, default='[titulo]')
    Fech_publicacion = models.DateField(auto_now=True, verbose_name='Fecha de Publicación')
    class Meta:
        verbose_name = 'Capítulo'
        verbose_name_plural = 'Capítulos'
    def __str__(self):
        return self.Manga.Nombre + ' - Capitulo ' + str(self.Num_capitulo) + ': ' + self.titulo

#Tabla "historial_lectura"
class tabla_historial_lectura(models.Model):
    ID_Usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    Capitulo = models.ForeignKey(tabla_capitulos, on_delete=models.CASCADE)
    Fecha_de_lectura = models.DateField(auto_now_add=True, verbose_name='Fecha de lectura')
    class Meta:
        verbose_name = 'Historial de Lectura'
        verbose_name_plural = 'Historial de Lectura'
    def __str__(self):
        return self.ID_Usuario.username + ' - Capitulo ' + self.Capitulo.Num_capitulo

#Tabla "contenido"
class tabla_contenido(models.Model):
    contenido = models.FileField(upload_to='Mairimashita!_Iruma-kun')
    capitulo = models.ForeignKey(tabla_capitulos, on_delete=models.CASCADE)
    detalle = models.CharField(max_length=30, default='[doc_name]')
    class Meta:
        verbose_name = 'Contenido'
        verbose_name_plural = 'Contenidos'
    def __str__(self):
        return self.capitulo.titulo + ': ' + self.detalle