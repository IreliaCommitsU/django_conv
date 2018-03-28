from posible_login_reg.models import Usuarios
from posible_controlPanel.models import Proyectos

# Create your models here.
class UsersSummary(Usuarios):
    class Meta:
        proxy = True
        verbose_name = '1 Resumen Registro'
        verbose_name_plural = '1 Resumen Registros'

class ProjectsSummary(Proyectos):
    class Meta:
        proxy = True
        verbose_name = '2 Resumen Proyectos'
        verbose_name_plural = '2 Resumen Proyectos'