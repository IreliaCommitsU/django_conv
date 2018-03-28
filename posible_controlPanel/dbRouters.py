from .models import Proyectos, ModuleAssets, Encuesta, Paneles, PanelAgenda
from posible_administrator.models import ProjectsSummary



class ProjectDBRouter(object):

    def db_for_read(self, model, **hints):
        """ reading SomeModel from otherdb """
        if model == Proyectos or model == ModuleAssets or model == Encuesta or model == ProjectsSummary or model == Paneles or model == PanelAgenda:
            return 'projects'
        return None

    def db_for_write(self, model, **hints):
        """ writing SomeModel to otherdb """
        if model == Proyectos or model == ModuleAssets or model == Encuesta  or model == ProjectsSummary or model == Paneles or model == PanelAgenda:
            return 'projects'
        return None