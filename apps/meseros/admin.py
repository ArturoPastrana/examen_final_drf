from django.contrib import admin

from apps.meseros.models import Meseros
from .models import Meseros
# Register your models here.


@admin.register(Meseros)
class MeserosAdmin(admin.ModelAdmin):
    list_display = ('dni', 'nombre', 'apellido', 'nacionalidad', )
