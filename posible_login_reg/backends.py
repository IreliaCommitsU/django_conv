from posible_login_reg.models import UsuariosPosible as US, Usuarios as NUS
from django.contrib.auth.backends import ModelBackend
import bcrypt

class UsuariosPosibleBackendAuth(ModelBackend): #Backend for custom ADMIN users
    """Allows a user to sign in to runeterra using a username/password pair."""
    def check_password(self,psw,user):
        return bcrypt.checkpw(psw.encode('utf8'), user.password.encode('utf8'))
    def authenticate(self, username=None, password=None):
        """ Authenticate a user based on USERNAME """
        if username and password:
            try:
                user = US.objects.get(usuario__iexact=username)
                if self.check_password(password, user):
                    return user
                return None
            except US.DoesNotExist:
                return None
        return None

    def get_user(self, user_id):
        """ Get a User object from the user_id. """
        try:
            user =  US.objects.get(pk=user_id)
            if user.is_active:
                return user
            return None
        except  US.DoesNotExist:
            return None
#        except US.MultipleObjectsReturned:
#            return None


class UsuariosBackendAuth(ModelBackend): #Backend for custom ADMIN users
    """Allows a user to sign in to runeterra using a email/password pair. (NORMAL_USERS)"""
    def check_password(self,psw,user):
        return bcrypt.checkpw(psw.encode('utf8'), user.password.encode('utf8'))
    def authenticate(self, email=None, password=None):
        """ Authenticate a user based on EMAIL ADDRESS """
        if email and password:
            try:
                user = NUS.objects.get(email__iexact=email)
                if self.check_password(password, user):
                    return user
                return None
            except NUS.DoesNotExist:
                return None
        return None

    def get_user(self, user_id):
        """ Get a User object from the user_id. """
        try:
            user =  NUS.objects.get(pk=user_id)
            if user.is_active:
                return user
            return None
        except  NUS.DoesNotExist:
            return None
        