from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.core.mail import send_mail
from posible_login_reg.managers import UsuarioPosibleManager, UsuarioManager
from django.utils.translation import ugettext_lazy as _
from posible_login_reg.helpers import gen_psw as g



class CodigosPostales(models.Model):
    cp = models.IntegerField(blank=True, null=True)
    id_estado = models.IntegerField(blank=True, null=True)
    estado = models.CharField(max_length=250, blank=True, null=True)
    id_municipio = models.IntegerField(blank=True, null=True)
    municipio = models.CharField(max_length=250, blank=True, null=True)
    id_ciudad = models.IntegerField(blank=True, null=True)
    ciudad = models.CharField(max_length=250, blank=True, null=True)
    id_asentamiento = models.IntegerField(blank=True, null=True)
    asentamiento = models.CharField(max_length=250, blank=True, null=True)
    id_asentamiento_tipo = models.IntegerField(blank=True, null=True)
    asentamiento_tipo = models.CharField(max_length=250, blank=True, null=True)
    zona = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        db_table = 'codigos_postales'


class Configs(models.Model):
    param = models.CharField(unique=True, max_length=250, blank=True, null=True)
    value = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'configs'


class Estados(models.Model):
    id_estado = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        db_table = 'estados'


class Logs(models.Model):
    uuid = models.CharField(max_length=250, blank=True, null=True)
    sitio = models.CharField(max_length=20)
    evento = models.CharField(max_length=250, blank=True, null=True)
    datos = models.CharField(max_length=250, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    ip = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        db_table = 'logs'


class Newletters(models.Model):
    newsletter_html = models.TextField()
    newsletter_title = models.CharField(max_length=255)
    newsletter_segments = models.CharField(max_length=13, blank=True, null=True)

    class Meta:
        db_table = 'newletters'


class Referencias(models.Model):
    ip = models.CharField(max_length=20, blank=True, null=True)
    referencia = models.CharField(max_length=20, blank=True, null=True)
    sitio = models.CharField(max_length=30, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'referencias'

class UsuariosPosible(AbstractBaseUser):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    apellido = models.CharField(max_length=120, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    usuario = models.CharField(max_length=100, blank=False, null=False,unique=True,default="UserDummy")
    password = models.CharField(max_length=100, blank=True, null=True)
    permisos = models.TextField(blank=True, null=True)
    is_staff= models.IntegerField(blank=True, null=True)
    is_superuser=models.IntegerField(blank=True, null=True)
    activo = models.IntegerField(blank=True, null=True)
    fecha_alta = models.DateTimeField(blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    
    objects = UsuarioPosibleManager()
    #username = models.CharField(max_length=100, blank=True, null=True)

    USERNAME_FIELD = 'usuario'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        db_table = 'usuarios_posible'

    def get_full_name(self): #Returns the first_name plus the last_name, with a space in between.
        return self.usuario

    def get_short_name(self): #Returns the short name for the user.
        return self.usuario

    def email_user(self, subject, message, from_email=None, **kwargs): #Sends an email to this User.
        send_mail(subject, message, from_email, [self.email], **kwargs)
        
    def set_password(self, raw_password):
        self.password = g(raw_password).decode('utf8')


    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser
        

class Usuarios(AbstractBaseUser):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    apellido = models.CharField(max_length=120, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    email_alt = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=250, blank=True, null=True)
    is_staff= models.IntegerField(blank=True, null=True)
    is_superuser=models.IntegerField(blank=True, null=True)
    activo = models.IntegerField(blank=True, null=True)
    fecha_alta = models.DateTimeField(blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    id_emprendedor = models.IntegerField(blank=True, null=True)
    id_alumno = models.IntegerField(blank=True, null=True)
    uuid = models.CharField(max_length=250, blank=True, null=True)
    sexo = models.CharField(max_length=10, blank=True, null=True)
    nacimiento = models.DateField(blank=True, null=True)
    id_estado = models.IntegerField(blank=True, null=True)
    id_municipio = models.IntegerField(blank=True, null=True)
    municipio = models.CharField(max_length=250, blank=True, null=True)
    cp = models.IntegerField(blank=True, null=True)
    ocupacion = models.CharField(max_length=10, blank=True, null=True)
    profesion = models.CharField(max_length=250, blank=True, null=True)
    biografia = models.TextField(blank=True, null=True)
    empresa = models.CharField(max_length=250, blank=True, null=True)
    giro = models.CharField(max_length=250, blank=True, null=True)
    puesto = models.CharField(max_length=250, blank=True, null=True)
    maximo_grado = models.CharField(max_length=250, blank=True, null=True)
    escuela = models.CharField(max_length=250, blank=True, null=True)
    socios = models.TextField(blank=True, null=True)
    tel_1_lada = models.CharField(max_length=10, blank=True, null=True)
    tel_1 = models.CharField(max_length=250, blank=True, null=True)
    tel_2_lada = models.CharField(max_length=10, blank=True, null=True)
    tel_2 = models.CharField(max_length=250, blank=True, null=True)
    tel_casa_lada = models.IntegerField(blank=True, null=True)
    tel_casa = models.CharField(max_length=250, blank=True, null=True)
    tel_of_lada = models.IntegerField(blank=True, null=True)
    tel_of = models.CharField(max_length=250, blank=True, null=True)
    tel_cel_lada = models.IntegerField(blank=True, null=True)
    tel_cel = models.CharField(max_length=250, blank=True, null=True)
    foto = models.ImageField( upload_to='profilePics/usuarios/', default = 'profilePics/usuarios/no-img.png',null=True)
    area_experiencia = models.CharField(max_length=250, blank=True, null=True)
    como_te_enteraste = models.CharField(max_length=250, blank=True, null=True)
    fb_uid = models.CharField(max_length=250, blank=True, null=True)
    fb_uid_pplus = models.CharField(max_length=250, blank=True, null=True)
    li_uid = models.CharField(max_length=250, blank=True, null=True)
    url_perfil_facebook = models.CharField(max_length=250, blank=True, null=True)
    url_perfil_linkedin = models.CharField(max_length=250, blank=True, null=True)
    codigo_seguridad = models.CharField(max_length=8, blank=True, null=True)
    metodo_alta = models.CharField(max_length=100, blank=True, null=True)
    referencia = models.CharField(max_length=50, blank=True, null=True)
    ip_alta = models.CharField(max_length=250, blank=True, null=True)
    ind_emprend = models.IntegerField(blank=True, null=True)
    porcentaje_perfil = models.IntegerField(blank=True, null=True)
    email_activacion = models.IntegerField(blank=True, null=True)
    newsletter = models.IntegerField(blank=True, null=True)
    newsletter_segments = models.CharField(max_length=13, blank=True, null=True)
    inversiones = models.IntegerField(blank=True, null=True)
    rendimientos = models.IntegerField(blank=True, null=True)
    intereses_categorias = models.CharField(max_length=300, blank=True, null=True)
    notas = models.TextField(blank=True, null=True)
    
    objects = UsuarioManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre']
    
    class Meta:
        db_table = 'usuarios'
    def set_password(self, raw_password):
            self.password = g(raw_password).decode('utf8')
            
    def get_full_name(self): #Returns the first_name plus the last_name, with a space in between.
        full_name = '%s %s' % (self.nombre, self.apellido)
        return full_name.strip()

    def get_short_name(self): #Returns the short name for the user.
        return self.nombre

    def email_user(self, subject, message, from_email=None, **kwargs): #Sends an email to this User.
        send_mail(subject,'',from_email, [self.email],html_message =message, **kwargs)
        
    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser
    