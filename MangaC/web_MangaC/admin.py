from django.contrib import admin
from .models import *

# Autores
class adminAutor(admin.ModelAdmin):
    search_fields = ('nombre','apellido')
    list_per_page = 15
admin.site.register(tabla_autores, adminAutor)

# Generos
class adminGenero(admin.ModelAdmin):
    search_fields = ('nombre',)
    list_per_page = 15
admin.site.register(tabla_generos, adminGenero)

# Mangas
class adminManga(admin.ModelAdmin):
    search_fields = ('nombre','genero_principal__nombre','autor__nombre','autor__apellido')
    list_display = ('nombre', 'genero_principal', 'autor', 'estado')
    list_filter = ('genero_principal', 'estado')
    list_per_page = 15
admin.site.register(tabla_mangas, adminManga)

# Capitulos
class adminCapitulo(admin.ModelAdmin):
    ordering = ('manga', 'num_capitulo')
    readonly_fields =('Fech_upload',)
    search_fields = ('manga__nombre',)
    list_per_page = 15

admin.site.register(tabla_capitulos, adminCapitulo)

# Historial Lectura
admin.site.register(tabla_historial_lectura)

