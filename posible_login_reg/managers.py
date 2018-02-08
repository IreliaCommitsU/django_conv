from django.utils import timezone
from django.contrib.auth.base_user import BaseUserManager
from posible_login_reg.helpers import randomPSWcode
from django.template.loader import render_to_string,get_template

class UsuarioPosibleManager(BaseUserManager):
    def _create_user(self, usuario,password,is_staff,is_superuser,**extra_fields):
        now = timezone.now()
        if not usuario:
            raise ValueError('No hay nombre de usuario especificado')
        user = self.model(usuario=usuario,is_staff=is_staff,activo=True,
                          is_superuser=is_superuser,last_login = now,
                          fecha_alta = now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self,usuario,password=None,**extra_fields):
        return self._create_user(usuario, password, False, False, **extra_fields)
    
    def create_superuser(self,usuario,password=None,**extra_fields):
        return self._create_user(usuario, password, True, True, **extra_fields)
   
class UsuarioManager(BaseUserManager):
    def _create_user(self, email,nombre,**extra_fields):
        now = timezone.now()
        code = randomPSWcode()
        code2= randomPSWcode()
        if not email:
            raise ValueError('No hay email especificado')
        user = self.model(email=email,nombre=nombre,is_staff=False,activo=True,
                          is_superuser=False,last_login = now,
                          fecha_alta = now, codigo_seguridad = code, **extra_fields)
        password = self.make_random_password(length=8)
        message = get_template('welcome_template.html').render({'name':nombre,'url':'https://posible.org.mx/cambiarClave/?ref=%s&email=%s' % (code+code2 ,email)})
        user.set_password(password)
        user.save(using=self._db)
        #user.email_user('Posible - Bienvenido',message, 'hola@posible.org.mx',)
        return user
    
    def create_user(self,email,nombre='sin_nombre',**extra_fields):
        return self._create_user(email, nombre, **extra_fields)
    
    def create_superuser(self,usuario,nombre='sin nombre',**extra_fields):
        return self._create_user(usuario, nombre, **extra_fields)