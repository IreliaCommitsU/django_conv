from posible_login_reg.models import Usuarios
from posible_controlPanel.models import Proyectos

# Create your models here.
class UsersSummary(Usuarios):
    class Meta:
        proxy = True
        verbose_name = 'Resumen Usuario'
        verbose_name_plural = 'Resumen Usuarios'

class ProjectsSummary(Proyectos):
    class Meta:
        proxy = True
        verbose_name = 'Resumen Proyectos'
        verbose_name_plural = 'Resumen Proyectos'