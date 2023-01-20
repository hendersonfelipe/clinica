from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

admin.site.register(Especialidades)
admin.site.register(Medico)
admin.site.register(Agenda)
admin.site.register(Cliente)
admin.site.register(Consulta )
# Register your models here.
