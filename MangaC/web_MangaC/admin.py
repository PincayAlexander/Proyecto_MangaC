from django.contrib import admin
from .models import tabla_autores, tabla_generos, tabla_manga_comic, tabla_capitulos, tabla_historial_lectura

# Register your models here.
admin.site.register(tabla_autores)
admin.site.register(tabla_generos)
admin.site.register(tabla_manga_comic)
admin.site.register(tabla_capitulos)
admin.site.register(tabla_historial_lectura)