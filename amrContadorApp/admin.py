from django.contrib import admin
from .models import AMRContador, Datos


# Register your models here.

class AMRContadorAdmin(admin.ModelAdmin):
    list_display = ('region', 'numeroCuenta',
                    'numeroCliente', 'direccionDispositivo',
                    'numeroContador', 'nombreContador',
                    'latitude', 'longitude', 'email', 'telefono')
    search_fields = ['region', 'numeroCuenta',
                     'numeroCliente', 'direccionDispositivo',
                     'numeroContador', 'nombreContador',
                     'latitude', 'longitude', 'email', 'telefono']

    # def has_delete_permission(self, request, obj=None):
    #     if obj and obj.delete:
    #         return False
    #     return True


class DatosAdmin(admin.ModelAdmin):
    list_display = ('amrContador', 'tmpLectura',
                    'totalImpEnerg', 't1ImpEnerg', 't2ImpEnerg', 't3ImpEnerg',
                    'totalExpEnerg', 't1ExpEnerg', 't2ExpEnerg', 't3ExpEnerg',
                    'totalImpReacEnerg', 't1ImpMaxDeman', 't2ImpMaxDeman', 't3ImpMaxDeman',
                    't1ExpMaxDeman', 't2ExpMaxDeman', 't3ExpMaxDeman', 'imporActPoder',
                    'exporActPoder', 'factPoder', 'faceAVolt', 'faceBVolt', 'faceCVolt',
                    'faceACurr', 'faceBCurr', 'faceCCurr')
    search_fields = ['amrContador__nombreContador', 'tmpLectura',
                     'totalImpEnerg', 't1ImpEnerg', 't2ImpEnerg', 't3ImpEnerg',
                     'totalExpEnerg', 't1ExpEnerg', 't2ExpEnerg', 't3ExpEnerg',
                     'totalImpReacEnerg', 't1ImpMaxDeman', 't2ImpMaxDeman', 't3ImpMaxDeman',
                     't1ExpMaxDeman', 't2ExpMaxDeman', 't3ExpMaxDeman', 'imporActPoder',
                     'exporActPoder', 'factPoder', 'faceAVolt', 'faceBVolt', 'faceCVolt',
                     'faceACurr', 'faceBCurr', 'faceCCurr']


admin.site.register(AMRContador, AMRContadorAdmin)
admin.site.register(Datos, DatosAdmin)

admin.site.site_header = 'Gestión AMR - Administración'
admin.site.site_title = 'Gestión AMR - Administración'
