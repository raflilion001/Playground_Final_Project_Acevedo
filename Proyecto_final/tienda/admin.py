from django.contrib import admin

from . import models

admin.site.register(models.Comprador)
admin.site.register(models.Vendedor)
admin.site.register(models.Producto)