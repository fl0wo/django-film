from django.contrib import admin

# Register your models here.

from . models import Categoria,Film,Immagine,Attore,Lingua

admin.site.register(Film)
admin.site.register(Categoria)
admin.site.register(Attore)
admin.site.register(Immagine)
admin.site.register(Lingua)

