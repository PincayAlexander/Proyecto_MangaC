import os
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
        return f"{self.Nombre} {self.Apellido}"


#Tabla "generos"
class tabla_generos(models.Model):
    Nombre = models.CharField(max_length=100)
    Descripcion = models.TextField(null=True)
    class Meta:
        verbose_name = 'Género'
        verbose_name_plural = 'Géneros'
    def __str__(self):
        return f"{self.Nombre}"


#Tabla "manga_comic"
class tabla_manga_comic(models.Model):
    OPCIONES_ESTADO = [
        ('Emision', 'Emisión'),
        ('Pausa', 'Pausa'),
        ('Finalizado', 'Finalizado'),
    ]
    Nombre = models.CharField(max_length=100)
    Genero = models.ManyToManyField(tabla_generos)
    Autor = models.ForeignKey(tabla_autores, on_delete=models.CASCADE, null=True)
    Fech_publicacion = models.DateField(auto_now_add=True, verbose_name='Fecha de Publicación')
    Estado = models.CharField(
        max_length=10,
        choices=OPCIONES_ESTADO,
        blank=True,
    )
    Portada = models.ImageField(upload_to='portadas/', null=True)
    Descripcion = models.TextField(null=True)
    class Meta:
        verbose_name = 'Manga/Comic'
        verbose_name_plural = 'Manga/Comic'
    def __str__(self):
        genero_principal = self.Genero.first().Nombre if self.Genero.exists() else 'Sin género'
        autor = f"{self.Autor.Nombre}, {self.Autor.Apellido}"
        return f"{self.Nombre} - {genero_principal} - {autor}"


#Construir la ruta para los capitulos
def obtener_ruta_subida(instance, filename):
    ruta = instance.Manga.Nombre.replace(' ', '_').lower()
    return os.path.join('capitulos', ruta, filename)
#Tabla "capitulos"
class tabla_capitulos(models.Model):
    Manga = models.ForeignKey(tabla_manga_comic, on_delete=models.CASCADE)
    capitulo = models.FileField(upload_to=obtener_ruta_subida, null=True)
    Num_capitulo = models.PositiveSmallIntegerField(verbose_name='Número de Capitulo')
    Titulo = models.CharField(max_length=100, null=True, blank=True)
    Detalle = models.CharField(max_length=20, null=True)
    Fech_publicacion = models.DateField(auto_now=True, verbose_name='Fecha de Publicación')
    class Meta:
        verbose_name = 'Capítulo'
        verbose_name_plural = 'Capítulos'
        ordering = ['Manga', 'Num_capitulo']
    def save(self, *args, **kwargs):
        self.Detalle = f'doc_{self.Detalle}_{self.Num_capitulo}' if self.Detalle else f"doc_manga_{self.Num_capitulo}"
        super().save(*args, **kwargs)
    def __str__(self):
        titulo = self.Titulo if self.Titulo else '[Sin título]'
        return f"{self.Manga.Nombre} - Capitulo {str(self.Num_capitulo)}: {titulo}"


#Tabla "historial_lectura"
class tabla_historial_lectura(models.Model):
    ID_Usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    Capitulo = models.ForeignKey(tabla_capitulos, on_delete=models.CASCADE)
    Fecha_de_lectura = models.DateField(auto_now_add=True, verbose_name='Fecha de lectura')
    class Meta:
        verbose_name = 'Historial de Lectura'
        verbose_name_plural = 'Historial de Lectura'
    def __str__(self):
        return f"{self.ID_Usuario.username} - Manga: {self.Capitulo.Manga.Nombre} - Capitulo #{str(self.Capitulo.Num_capitulo)}"