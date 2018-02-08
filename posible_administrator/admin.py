from django.contrib import admin
from .models import UsersSummary
from django.contrib.admin.options import ModelAdmin
from django.db.models.aggregates import Count, Sum
from posible_controlPanel.models import ModuleAssets

from django.contrib.auth.models import Group
from social_django.models import Association, Nonce, UserSocialAuth
from posible_administrator.models import ProjectsSummary

#First we unregister this tables that they don't make sense
admin.site.unregister(Group)
admin.site.unregister(Association)
admin.site.unregister(Nonce)
admin.site.unregister(UserSocialAuth)
admin.site.site_header = 'POSiBLE Mini Dashboard'

# Register your models here.
class ModuleAssetsAdmin(admin.ModelAdmin):
    list_display = ('title', 'module_id', 'type_content')
admin.site.register(ModuleAssets,ModuleAssetsAdmin)

@admin.register(UsersSummary)
class UsersSummaryAdmin(ModelAdmin):
    change_list_template = 'admin/users_summary_change_list.html'
    list_filter = ('sexo','fecha_alta',)
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
        response.context_data['summary'] = list(
            qs
            .values('id_estado')
            .annotate(**metrics)
            .order_by('-total')
        )
        response.context_data['summary_total'] = dict(
            qs.aggregate(**metrics)
        )
        
        
        return response
    
@admin.register(ProjectsSummary)
class ProjectsSummaryAdmin(ModelAdmin):
    change_list_template = 'admin/project_summary_change_list.html'
    list_filter = ('avance_total','status','avance_modulo_1','avance_modulo_2','avance_modulo_3','avance_modulo_4','avance_modulo_5','avance_modulo_6','avance_modulo_7')
    
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
        response.context_data['summary'] = list(
            qs
            .values('email')
            .annotate(**metrics)
            
        )
        response.context_data['summary_total'] = dict(
            qs.aggregate(**metrics)
        )
        
        
        return response
