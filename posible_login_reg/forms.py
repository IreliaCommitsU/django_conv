from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import UsuariosPosible

class UsuarioPosibleCreationForm(UserCreationForm):
    ''' Forma que crea un usuario sin privilegios, nombre de usuario y password'''
    
    def __init__(self,*args,**kargs):
        super(UsuarioPosibleCreationForm,self).__init__(*args,**kargs)
        #del self.fields['']
    class Meta:
        model = UsuariosPosible
        fields = ("usuario",)
        

class UsuarioPosibleChangeForm(UserChangeForm):
    ''' Forma que crea un usuario sin privilegios, nombre de usuario y password'''
    
    def __init__(self,*args,**kargs):
        super(UsuarioPosibleChangeForm,self).__init__(*args,**kargs)
        #del self.fields['']
    class Meta:
        model = UsuariosPosible