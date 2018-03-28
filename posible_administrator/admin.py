from django.contrib import admin
from .models import UsersSummary
from django.contrib.admin.options import ModelAdmin
from django.db.models.aggregates import Count, Sum, Min, Max
from posible_controlPanel.models import ModuleAssets, Proyectos, Paneles

from django.contrib.auth.models import Group
from social_django.models import Association, Nonce, UserSocialAuth
from posible_administrator.models import ProjectsSummary
from posible_controlPanel.choices import PS_STATES
from django.db.models import Q
from posible_login_reg.models import Usuarios
from django.utils import timezone
from _datetime import datetime

admin.site.site_header = 'POSiBLE Mini Dashboard'
#First we unregister this tables that they don't make sense
admin.site.unregister(Group)
admin.site.unregister(Association)
admin.site.unregister(Nonce)
admin.site.unregister(UserSocialAuth)

# Register your models here.
class ModuleAssetsAdmin(admin.ModelAdmin):
    list_display = ('title', 'module_id', 'type_content')
admin.site.register(ModuleAssets,ModuleAssetsAdmin)

class PanelesAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'ciudad', 'lugar', 'direccion', 'interior', 'referencias', 'mapa','virtual','id_estado','url_mapa')
admin.site.register(Paneles,PanelesAdmin)

class UsersAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return request.user.usuario=='hugo'
    def has_delete_permission(self, request, obj=None):
        return request.user.usuario=='hugo'
    def has_change_permission(self, request, obj=None):     
        return request.user.usuario=='hugo'
    list_display = ('id',
                    'uuid',
                    'nombre',
                    'apellido',
                    'foto',
                    'password',
                    'nacimiento',
                    'maximo_grado',
                    'escuela',
                    'id_estado',
                    'municipio',
                    'sexo',
                    'email',
                    'email_alt',
                    'tel_1_lada',
                    'tel_1',
                    'tel_2_lada',
                    'tel_2',
                    'como_te_enteraste',
                    'area_experiencia',
                    'fecha_alta',
                    'codigo_seguridad')
admin.site.register(Usuarios,UsersAdmin)

class ProyectosAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return request.user.usuario=='hugo'
    def has_delete_permission(self, request, obj=None):
        return request.user.usuario=='hugo'
    def has_change_permission(self, request, obj=None):     
        return request.user.usuario=='hugo'
    list_display = ('id',
                    'uuid_usuario',
                    'email',
                    'fecha_creacion',
                    'status',
                    'avance_modulo_1',
                    'avance_modulo_2',
                    'avance_modulo_3',
                    'avance_modulo_4',
                    'avance_modulo_5',
                    'avance_modulo_6',
                    'avance_modulo_7',
                    'avance_total'
                   )
admin.site.register(Proyectos,ProyectosAdmin)

def makeDict(lista,grouper,categories):
    newDict=dict()
    for elem in lista:
        #print(elem.get('deit'),elem.get('metodo_alta'),elem.get('total'))
        if not str(elem.get(grouper)) in newDict:
            newDict[str(elem.get(grouper))] = {elem.get(categories):elem.get('total')}
        else:
            newDict[str(elem.get(grouper))].update({elem.get(categories):elem.get('total')})
    return newDict

@admin.register(UsersSummary)
class UsersSummaryAdmin(ModelAdmin):
    change_list_template = 'admin/users_summary_change_list.html'
    list_filter = ('sexo','fecha_alta',)
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    def time_seconds(self, obj):
        return obj.timefield.strftime("%d %b %Y")
    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )
        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response
        
        metrics = {
            'total': Count('id'),
        }
        response.context_data['summary'] = list(
            qs
            .extra({"deit": "date(fecha_alta)"})
            .values('deit')
            .annotate(**metrics)
            .order_by('-deit')
        )
        response.context_data['summaryTest'] = makeDict(
            qs
            .extra({"deit": "date(fecha_alta)"})
            .values('deit','metodo_alta')
            .annotate(**metrics)
            .order_by('-deit'), 'deit','metodo_alta'
        )
        
        response.context_data['edo_summary'] = list(
            qs
            .values('id_estado')
            .annotate(**metrics)
            .order_by('id_estado')
        )
        
        response.context_data['edo_vals'] = dict(PS_STATES)
        
        response.context_data['summary_total'] = dict(
            qs.aggregate(**metrics)
        )
        now = timezone.now()
        nau = '%s-%s-%s' % (str(now.year) ,str(now.month) , str(now.day))
        response.context_data['summary_today'] = list(
            qs
            .extra({"deit": "CONCAT_WS('',date(fecha_alta),' ',hour(fecha_alta))", "hours":"hour(fecha_alta)"})
            .values('deit')
            .filter(fecha_alta__date = nau )
            .annotate(**metrics)
            .order_by('hours')
        )
        response.context_data['summary_today_total'] = dict(
            qs.filter(fecha_alta__date = nau ).aggregate(**metrics)
        )
        
        response.context_data['is_ale'] = request.user.usuario == 'ale.guerrero'
        return response
    
@admin.register(ProjectsSummary)
class ProjectsSummaryAdmin(ModelAdmin):
    change_list_template = 'admin/project_summary_change_list.html'
    
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )
        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response
        
        metrics = {
            'total': Count('id'),
        }
        
        response.context_data['summary_borrador'] = qs.filter(status='borrador').count()
        response.context_data['summary_revision'] = qs.filter(status='revision').count()
        response.context_data['summary_asignados'] = qs.filter(status='asignados').count()
        response.context_data['summary_evaluados'] = qs.filter(status='evaluados').count()
        
        response.context_data['summary_0_25'] = qs.filter(avance_total__gte=0,avance_total__lte=25).count()
        response.context_data['summary_25_50'] = qs.filter(avance_total__gt=25,avance_total__lte=50).count()
        response.context_data['summary_50_75'] = qs.filter(avance_total__gt=50,avance_total__lte=75).count()
        response.context_data['summary_75_90'] = qs.filter(avance_total__gt=75,avance_total__lte=90).count()
        response.context_data['summary_90_100'] = qs.filter(avance_total__gt=90,avance_total__lte=100,status='borrador').count()
        
        response.context_data['summary_total'] = dict(
            qs.aggregate(**metrics)
        )
        response.context_data['edo_vals'] = dict(PS_STATES)
        
        response.context_data['edo_summary'] = list(
            qs
            .values('id_estado')
            .annotate(**metrics)
            .order_by('id_estado')
        )
        response.context_data['summaryProyectosFecha'] = list(
            qs
            .extra({"deit": "date(fecha_envio_a_revision)"})
            .values('deit')
            .annotate(**metrics)
            .order_by('-deit')
        )
        response.context_data['summaryEdoTest'] = makeDict(
            qs
            .values('id_estado','status')
            .annotate(**metrics)
            .order_by('id_estado'), 'id_estado','status'
        )
        return response
