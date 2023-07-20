from django.contrib import admin
from .models import Empleado, habilidades

# Register your models here.


admin.site.register(habilidades)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display=(
        'first_name',
        'last_name',
        'departamento',
        'job',
        'full_name',
    )
    search_fields = ('first_name',)
    list_filter=('departamento', 'job','habilidades',)
    #
    filter_horizontal=('habilidades',)

admin.site.register(Empleado,EmpleadoAdmin)