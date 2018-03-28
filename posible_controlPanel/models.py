# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Proyectos(models.Model):
    uuid_usuario = models.CharField(max_length=250, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=8, blank=True, null=True)
    fecha_envio_a_revision = models.DateTimeField(blank=True, null=True)
    privado = models.IntegerField()
    visitas = models.IntegerField(blank=True, null=True)
    comparticiones = models.IntegerField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    
    modulo_1_1 = models.TextField(blank=True, null=True)
    modulo_1_2 = models.TextField(blank=True, null=True)
    
    modulo_2_1 = models.CharField(max_length=250,blank=True,default = 'sin_nombre' ,null=True)
    modulo_2_2 = models.TextField(blank=True, null=True)
    modulo_2_3 = models.CharField(max_length=250, blank=True, null=True)
    modulo_2_4 = models.CharField(max_length=250, blank=True, null=True)
    modulo_2_4_otro = models.DateField(blank=True, null=True)
    modulo_2_5 = models.ImageField(upload_to='projectPics/proyectos/', default = 'projectPics/proyectos/no-img.png',null=True)
    modulo_2_5_1 = models.ImageField(upload_to='projectPics/proyectos/', default = 'projectPics/proyectos/no-img.png',null=True)
    modulo_2_5_2 = models.ImageField(upload_to='projectPics/proyectos/', default = 'projectPics/proyectos/no-img.png',null=True)
    modulo_2_6 = models.CharField(max_length=250, blank=True, null=True)
    modulo_2_7 = models.CharField(max_length=250, blank=True, null=True)
    modulo_2_8 = models.CharField(max_length=250, blank=True, null=True)
    modulo_2_9 = models.TextField(blank=True, null=True)
    
    modulo_3_1 = models.CharField(max_length=250, blank=True, null=True)
    modulo_3_1_2 = models.CharField(max_length=250, blank=True, null=True)
    modulo_3_1_3 = models.CharField(max_length=250, blank=True, null=True)
    modulo_3_1_4 = models.CharField(max_length=250, blank=True, null=True)
    modulo_3_1_5 = models.CharField(max_length=250, blank=True, null=True)
    modulo_3_1_6 = models.TextField(blank=True, null=True)
    modulo_3_2_2 = models.CharField(max_length=250, blank=True, null=True)
    modulo_3_2_3 = models.TextField(blank=True, null=True)
    modulo_3_3 = models.CharField(max_length=250, blank=True, null=True)
    modulo_3_4 = models.CharField(max_length=250, blank=True, null=True)
    modulo_3_5 = models.TextField(blank=True, null=True)
    
    modulo_4_1 = models.CharField(max_length=250, blank=True, null=True)
    modulo_4_1_otro = models.TextField(blank=True, null=True)
    modulo_4_2 = models.TextField(blank=True, null=True)
    modulo_4_3 = models.TextField(blank=True, null=True)
    
    modulo_5_1 = models.CharField(max_length=250, blank=True, null=True)
    modulo_5_1_otro = models.TextField(blank=True, null=True)
    modulo_5_2 = models.CharField(max_length=250, blank=True, null=True)
    modulo_5_2_otro = models.TextField(blank=True, null=True)
    modulo_5_3 = models.CharField(max_length=250, blank=True, null=True)
    modulo_5_3_otro = models.TextField(blank=True, null=True)
    modulo_5_4 = models.CharField(max_length=250, blank=True, null=True)
    modulo_5_4_otro = models.CharField(max_length=250, blank=True, null=True)
    modulo_5_5 = models.TextField(blank=True, null=True)
    
    modulo_6_1 = models.CharField(max_length=250, blank=True, null=True)
    modulo_6_2 = models.CharField(max_length=250, blank=True, null=True)
    modulo_6_2_otro = models.TextField(blank=True, null=True)
    modulo_6_3 = models.CharField(max_length=250, blank=True, null=True)
    modulo_6_3_otro = models.TextField(blank=True, null=True)
    
    modulo_7_1 = models.CharField(max_length=250, blank=True, null=True)
    modulo_7_2_1 = models.TextField(blank=True, null=True)
    modulo_7_2_2 = models.TextField(blank=True, null=True)
    modulo_7_2_3 = models.TextField(blank=True, null=True)
    modulo_7_2_4 = models.TextField(blank=True, null=True)
    modulo_7_2_5 = models.TextField(blank=True, null=True)
    
    avance_modulo_1 = models.IntegerField(blank=True, null=True)
    avance_modulo_2 = models.IntegerField(blank=True, null=True)
    avance_modulo_3 = models.IntegerField(blank=True, null=True)
    avance_modulo_4 = models.IntegerField(blank=True, null=True)
    avance_modulo_5 = models.IntegerField(blank=True, null=True)
    avance_modulo_6 = models.IntegerField(blank=True, null=True)
    avance_modulo_7 = models.IntegerField(blank=True, null=True)
    avance_total = models.IntegerField(blank=True, null=True)
    tags = models.CharField(max_length=255, blank=True, null=True)
    id_estado = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proyectos'

class EmprendedoresNotificaciones(models.Model):
    uuid_usuario = models.CharField(max_length=36)
    tipo_notificacion = models.IntegerField()
    id_proyecto = models.IntegerField()
    fecha = models.DateTimeField()
    visto = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'emprendedores_notificaciones'


class ModuleAssets(models.Model):
    module_id = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=250, blank=True, null=True)
    type_content = models.CharField(max_length=8, blank=True, null=True)
    url = models.CharField(max_length=250, blank=True, null=True)
    texto = models.TextField(blank=True, null=True)
    active = models.IntegerField()
    def __str__(self):
        return self.title
    class Meta:
        managed = False
        db_table = 'module_assets'

class Encuesta(models.Model):
    uuid = models.CharField(max_length=250, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    pregunta1 = models.CharField(max_length=250, blank=True, null=True)
    pregunta2 = models.CharField(max_length=250, blank=True, null=True)
    pregunta3 = models.CharField(max_length=250, blank=True, null=True)
    pregunta4 = models.CharField(max_length=250, blank=True, null=True)
    pregunta5 = models.CharField(max_length=250, blank=True, null=True)
    pregunta6 = models.CharField(max_length=250, blank=True, null=True)
    pregunta7 = models.CharField(max_length=250, blank=True, null=True)
    pregunta8 = models.CharField(max_length=250, blank=True, null=True)
    pregunta9 = models.CharField(max_length=250, blank=True, null=True)
    pregunta10 = models.CharField(max_length=250, blank=True, null=True)
    pregunta11 = models.CharField(max_length=250, blank=True, null=True)
    pregunta12 = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'encuesta'

class InversionistasInversiones(models.Model):
    id_inversionista = models.IntegerField(blank=True, null=True)
    uuid = models.CharField(max_length=250, blank=True, null=True)
    id_proyecto = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    inversion = models.IntegerField(blank=True, null=True)
    referenciado = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=250, blank=True, null=True)
    sospechosa = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inversionistas_inversiones'


class InversionistasSiguiendo(models.Model):
    id_inversionista = models.IntegerField(blank=True, null=True)
    uuid = models.CharField(max_length=250, blank=True, null=True)
    id_proyecto = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inversionistas_siguiendo'



class Paneles(models.Model):
    fecha = models.DateField(db_column='FECHA', blank=True, null=True)  # Field name made lowercase.
    ciudad = models.CharField(db_column='CIUDAD', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lugar = models.CharField(db_column='LUGAR', max_length=40, blank=True, null=True)  # Field name made lowercase.
    direccion = models.TextField(db_column='DIRECCION', blank=True, null=True)  # Field name made lowercase.
    interior = models.TextField(db_column='INTERIOR', blank=True, null=True)  # Field name made lowercase.
    referencias = models.TextField(db_column='REFERENCIAS', blank=True, null=True)  # Field name made lowercase.
    mapa = models.CharField(db_column='MAPA', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    virtual = models.IntegerField(db_column='VIRTUAL', blank=True, null=True)  # Field name made lowercase.
    id_estado = models.IntegerField(db_column='id_Estado', blank=True, null=True)
    url_mapa = models.CharField(db_column='URL_MAPA', max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paneles'


class PanelAgenda(models.Model):
    id_panel = models.IntegerField(db_column='id_panel')
    hora = models.TextField(db_column='hora')
    id_proyecto = models.IntegerField(db_column='id_proyecto')
    uuid = models.TextField(db_column='uuid')
    email = models.TextField(db_column='email')
    nombre_proyecto = models.TextField(db_column='nombre_proyecto')
    link = models.FileField(upload_to='projectsPresentations/',null=True)
    
    class Meta:
        managed = False
        db_table = 'paneles_agenda'

class ProyectosAvances(models.Model):
    id_proyecto = models.IntegerField(blank=True, null=True)
    titulo = models.CharField(max_length=250, blank=True, null=True)
    avance = models.TextField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    video = models.CharField(max_length=250, blank=True, null=True)
    img_1 = models.CharField(max_length=250, blank=True, null=True)
    img_2 = models.CharField(max_length=250, blank=True, null=True)
    img_3 = models.CharField(max_length=250, blank=True, null=True)
    img_4 = models.CharField(max_length=250, blank=True, null=True)
    img_5 = models.CharField(max_length=250, blank=True, null=True)
    img_6 = models.CharField(max_length=250, blank=True, null=True)
    img_7 = models.CharField(max_length=250, blank=True, null=True)
    img_8 = models.CharField(max_length=250, blank=True, null=True)
    img_9 = models.CharField(max_length=250, blank=True, null=True)
    img_10 = models.CharField(max_length=250, blank=True, null=True)
    img_12 = models.CharField(max_length=250, blank=True, null=True)
    img_13 = models.CharField(max_length=250, blank=True, null=True)
    img_14 = models.CharField(max_length=250, blank=True, null=True)
    img_16 = models.CharField(max_length=250, blank=True, null=True)
    img_11 = models.CharField(max_length=250, blank=True, null=True)
    img_17 = models.CharField(max_length=250, blank=True, null=True)
    img_18 = models.CharField(max_length=250, blank=True, null=True)
    img_19 = models.CharField(max_length=250, blank=True, null=True)
    img_20 = models.CharField(max_length=250, blank=True, null=True)
    img_15 = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proyectos_avances'


class ProyectosComentarios(models.Model):
    id_proyecto = models.IntegerField(blank=True, null=True)
    uuid = models.CharField(max_length=250, blank=True, null=True)
    id_remitente = models.IntegerField(blank=True, null=True)
    parent = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    comentario = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proyectos_comentarios'