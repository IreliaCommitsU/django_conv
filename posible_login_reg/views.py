from django.shortcuts import render,redirect
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from posible_login_reg.models import Usuarios, Referencias
from posible_login_reg.helpers import randomPSWcode, get_client_ip
from django.http.response import Http404
from django.template.loader import get_template
from django.views import View
import re

EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
class log_in_class(View):
    template_name='login_reg/loginReg.html'
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/principal/')
        has_pcd = request.GET.get('pcd','') !=''
        is_good = request.GET.get('good','') !=''
        is_bad = request.GET.get('bad','') !=''
        return render(request, self.template_name,{'is_register':False,
                                                              'has_pcd': has_pcd,
                                                              'good': is_good,
                                                              'bad': is_bad,
                                                              })
    def post(self,request):
        if request.user.is_authenticated:
            return redirect('/principal/')
        correo = request.POST.get('e', '')
        password = request.POST.get('p', '')
        user = authenticate(request, email=correo, password=password)
        if user is not None:
            login(request, user,user.backend)   #LOG THE USER
            return redirect('/principal/')      # Redirect to a success page.
        else:
            return render(request,self.template_name,{'is_register':False,'status_login':-3})# Return an 'invalid login' error message.

class register_class(View):
    template_name="login_reg/loginReg.html"
    def get(self,request):
        if request.user.is_authenticated:
            return redirect('/principal/')
        fb = request.GET.get('fb','')
        al = request.GET.get('al','')
        nw = request.GET.get('nw','')
        tw = request.GET.get('tw','')
        ip = get_client_ip(request)
        now = timezone.now()
        refer = 'web'
        if fb == '1':
            refer = 'fb_org_2018'
        if fb == 'p':
            refer = 'fb_pauta_2018'
        if al == '1':
            refer = 'aliados_2018'
        if tw == '1':
            refer = 'tw_2018'
        if nw == '1':
            refer = 'news_2018'
        ref_obj = Referencias(ip=ip,referencia=refer,sitio='posible',fecha=now)
        ref_obj.save()
        return render(request,self.template_name,{'is_register':True})    
    def post(self,request):
        if request.user.is_authenticated:
            return redirect('/principal/')
        email = request.POST.get('e', '')
        correoConf = request.POST.get('ce', '')
        nombre = request.POST.get('n','')
        m_alta = request.POST.get('ma','')
        clave = request.POST.get('pw','')
        if email == '' or correoConf == '' or nombre == '':
            return render(request,self.template_name,{'status':-1}) #A FIELD IS EMPTY
        else:
            if email != correoConf:
                return render(request,self.template_name,{'is_register':True,'status':-2}) #EMAILS NOT EQUAL
            else:
                #TODO:
                if not EMAIL_REGEX.match(email):
                    return  render(request,self.template_name,{'is_register':True,"status":-3}) #EMAIL IN BAD FORMAT
                try:
                    Usuarios.objects.get(email__iexact=email)
                    return render(request,self.template_name,{'is_register':True,'status':-4}) #ALREADY HAS ACCOUNT
                except Usuarios.DoesNotExist:
                    Usuarios.objects.create_user(email,clave, nombre,m_alta)
                    return redirect('/thanks/')
        
# Create your views here.
def aviso(request):
    return render(request,'aviso_privacidad.html')

def landing(request):
    return render(request, "login_reg/landing.html",{})

def log_out(request):
    logout(request)
    return redirect('/login/')


def change_PS_page(request):
    if request.method != 'POST':
        ref = request.GET.get('ref','')
        us_e = request.GET.get('email','')
        if ref=='' or us_e=='': #EMAIL CANNOT BE EMPTY
            raise Http404
        return render(request,'login_reg/changePWD.html',{'reference':ref,
                                                          'correo': us_e
                                                          })
    else:
        n_p = request.POST.get('p','')
        n_pc = request.POST.get('p_conf','')
        acc = request.POST.get('c','')
        reference = request.POST.get('r','')
        if len(n_p) < 6:
            return render(request,'login_reg/changePWD.html',{'reference':reference,
                                                          'correo': acc,
                                                          'error': -1
                                                          })
        if n_p != n_pc:
            return render(request,'login_reg/changePWD.html',{'reference':reference,
                                                          'correo': acc,
                                                          'error': -2
                                                          })
        #HERE CAN BE ADD MORE RULES FOR STRONG PSW
        cs = reference[:8]
        try:
            us = Usuarios.objects.get(email__iexact=acc,codigo_seguridad__iexact=cs)
        except Usuarios.DoesNotExist:
            return render(request,'login_reg/changePWD.html',{'reference':reference,
                                                          'correo': acc,
                                                          'error': -3
                                                          })
        us.set_password(n_p)
        us.codigo_seguridad = 0
        us.save()
        return redirect('/login/?pcd=yes' )

def forgot_PSW(request):
    if request.method == 'POST':
        corr = request.POST.get('c','')
        try:
            us = Usuarios.objects.get(email__iexact=corr, codigo_seguridad=0)
            code = randomPSWcode()
            code2 = randomPSWcode()
            us.codigo_seguridad = code
            message = get_template('forgot_template.html').render({'name':us.nombre,'url':'https://posible.org.mx/cambiarClave/?ref=%s&email=%s' % (code+code2 ,us.email)})
            us.email_user('Posible - Contraseña Olvidada',message, 'hola@posible.org.mx')
            us.save()
            return redirect('/login/?good=1')
        except Usuarios.DoesNotExist:
            return redirect('/login/?bad=1')
        except Usuarios.MultipleObjectsReturned:
            return redirect('/login/?bad=1')
    return redirect('/login/')

def info_graphic(request):
    return render(request, 'login_reg/infog.html')

class offline_registry(View):
    template_name="login_reg/offlinetv.html"
    def get(self,request):
        return render(request,self.template_name)
        



        