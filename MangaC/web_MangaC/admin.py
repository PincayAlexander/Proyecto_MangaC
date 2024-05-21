from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(tabla_autores)
admin.site.register(tabla_generos)
admin.site.register(tabla_manga_comic)
admin.site.register(tabla_capitulos)
admin.site.register(tabla_historial_lectura)