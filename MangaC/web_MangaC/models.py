import os
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

#Tabla "autores"
class tabla_autores(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre', default='Anonimo',)
    apellido = models.CharField(max_length=100, verbose_name='Apellido', null=True, blank=True,)
    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
    def __str__(self):
        apellido = self.apellido if self.apellido else ''
        return f"{self.nombre} {apellido}"
    

#Tabla "generos"
class tabla_generos(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre', default='')
    descripcion = models.TextField(verbose_name='Descripcion', null=True, blank=True,)
    class Meta:
        verbose_name = 'Género'
        verbose_name_plural = 'Géneros'
    def __str__(self):
        return f"{self.nombre}"


#Tabla "manga_comic"
class tabla_mangas(models.Model):
    OPCIONES_ESTADO = [
        ('Emision', 'Emisión'),
        ('Pausa', 'Pausa'),
        ('Finalizado', 'Finalizado'),
    ]
    nombre = models.CharField(max_length=100)
    genero_principal = models.ForeignKey(tabla_generos, null=True, on_delete=models.CASCADE, verbose_name='Genero Principal')
    subgenero = models.ManyToManyField(tabla_generos, blank=True, related_name='sub_mangas_set', verbose_name='Subgenero')
    autor = models.ForeignKey(tabla_autores, on_delete=models.CASCADE, null=True)
    fech_publicacion = models.DateField(auto_now_add=True, verbose_name='Fecha de Publicación')
    estado = models.CharField(max_length=10, choices=OPCIONES_ESTADO)
    portada = models.ImageField(upload_to='portadas/', null=True)
    descripcion = models.TextField(null=True)
    class Meta:
        verbose_name = 'Manga/Comic'
        verbose_name_plural = 'Manga/Comic'
    def __str__(self):
        autor = f"{self.autor.nombre}, {self.autor.apellido}"
        generoPrincipal = self.genero_principal if self.genero_principal else 'Sin genero'
        return f"{self.nombre} - {generoPrincipal} - {autor}"


#Construir la ruta para los capitulos
def obtener_ruta_subida(instance, filename):
    ruta = instance.manga.nombre.replace(' ', '_').lower()
    return os.path.join('capitulos', ruta, filename)
#Tabla "capitulos"
class tabla_capitulos(models.Model):
    manga = models.ForeignKey(tabla_mangas, on_delete=models.CASCADE)
    capitulo = models.FileField(upload_to=obtener_ruta_subida, null=True)
    num_capitulo = models.PositiveSmallIntegerField(verbose_name='Número de Capitulo')
    titulo = models.CharField(max_length=100, null=True)
    Fech_upload = models.DateField(auto_now=True, verbose_name='Fecha de Publicación')
    class Meta:
        verbose_name = 'Capítulo'
        verbose_name_plural = 'Capítulos'
        ordering = ['manga', 'num_capitulo']
    def __str__(self):
        titulo = self.titulo if self.titulo else '[Sin título]'
        return f"{self.manga.nombre} - Capitulo {str(self.num_capitulo)}: {titulo}"


#Tabla "historial_lectura"
class tabla_historial_lectura(models.Model):
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    capitulo = models.ForeignKey(tabla_capitulos, on_delete=models.CASCADE)
    fech_lectura = models.DateField(auto_now_add=True, verbose_name='Fecha de lectura')
    class Meta:
        verbose_name = 'Historial de Lectura'
        verbose_name_plural = 'Historial de Lectura'
    def __str__(self):
        return f"{self.id_usuario.username} - Manga: {self.capitulo.manga.nombre} - Capitulo #{str(self.capitulo.num_capitulo)}"