import csv
from django.views import View
from django.http import HttpResponse
from django.shortcuts import render
from django.http.response import Http404
from posible_controlPanel.models import Encuesta, Proyectos
from datetime import date, timedelta, datetime
from posible_login_reg.models import Usuarios
from posible_login_reg.helpers import gen_psw, randomPSWcode
from django.template.loader import get_template
import time
from django.utils import timezone
# Create your views here.

class customer_service(View):
    def get(self,request): 
        if not request.user.is_staff or not request.user.is_superuser:
            raise Http404
            
        email = request.GET.get('email','')
        if email == '':
            return render(request,'administrator/ss_changerPSW.html')
        else:
            users = Usuarios.objects.filter(email__iexact=email)
            num_acc = users.count()
            proys = Proyectos.objects.filter(email__iexact=email).count()
            
            if num_acc > 0:
                single = users.first()
                #print(single.codigo_seguridad != '0')
                return render(request,'administrator/ss_changerPSW.html',{  'show': 1,
                                                                            'nombre':single.nombre,
                                                                            'apellido': single.apellido,
                                                                            'foto': single.foto.url,
                                                                            'nacimiento': single.nacimiento,
                                                                            'maximo_grado': single.maximo_grado,
                                                                            'escuela': single.escuela,
                                                                            'id_estado': single.id_estado,
                                                                            'municipio': single.municipio,
                                                                            'sexo': single.sexo,
                                                                            'email': single.email,
                                                                            'email_alt': single.email_alt,
                                                                            'tel_1_lada': single.tel_1_lada,
                                                                            'tel_1': single.tel_1,
                                                                            'tel_2_lada': single.tel_2_lada,
                                                                            'tel_2': single.tel_2,
                                                                            'como_te_enteraste': single.como_te_enteraste,
                                                                            'area_experiencia': single.area_experiencia,
                                                                            'socios': single.socios,
                                                                            
                                                                            'has_block_pswRESET' : single.codigo_seguridad!='0',
                                                                            'num_acc' : num_acc,
                                                                            'numproys' : proys,
                                                                          })
            else:
                return render(request,'administrator/ss_changerPSW.html',{'show': 2,'email':email})
    
    def post(self,request):
        if not request.user.is_staff or not request.user.is_superuser:
            raise Http404
        psw_rst = request.POST.get('psw_rst','')
        forgot_rst = request.POST.get('forgot_rst','')
        cuenta = request.POST.get('cuenta','')
        msg = ''
        show = 0
        psw = 'XXXXXX'
        name = 'No tiene nombre'
        if cuenta == '':
            msg = 'La cuenta llegó vacía por alguna razón rara: ' + cuenta
        else:   
            if psw_rst == "1":
                users = Usuarios.objects.filter(email__iexact=cuenta)
                psw = randomPSWcode()
                db_hash = gen_psw(psw).decode('utf_8')
                u = users.first()
                u.password = db_hash
                u.codigo_seguridad = 0
                u.save()
                msg = 'Se le cambio la contraseña a la cuenta: ' + cuenta
                if u.nombre is not None:
                    name = u.nombre
                show = 4
            elif forgot_rst == "1":
                msg = 'La cuenta ' + cuenta +' ahora puede volver a solicitar un cambio de contraseña'
                users = Usuarios.objects.filter(email__iexact=cuenta)
                u = users.first()
                u.codigo_seguridad = 0
                u.save()
                show = 3
            else:
                raise Http404
        return render(request,'administrator/ss_changerPSW.html',{'show': show,
                                                                  'email': cuenta,
                                                                  'msg': msg,
                                                                  'nombre': name,
                                                                  'psw':psw})
'''class envio_correos(View):
    template_name="ss_dash.html"
    def sender(self, proys):
        msg = 'Envio proyecto exitoso'
        cont = 0
        now = timezone.now()
        for p in proys:
            u = Usuarios.objects.filter(email__iexact = p.email).first()
            if u is not None:
                message = get_template('controlPanel/folio_template.html').render({'name':u.nombre,'folio':p.fecha_envio_a_revision ,'id':p.id})
                u.email_user('Posible - ' + msg ,message, 'hola@posible.org.mx',)
                cont += 1
                if cont%145 == 0: #WE HAVE A CUOTA OF 14 MAILS PER SECOND :/
                    time.sleep(1)
        
        u1 = Usuarios.objects.filter(email__iexact = 'hugo.huipet@fundaciontelevisa.org').first()
        message = get_template('controlPanel/folio_template.html').render({'name':u1.nombre,'folio':now ,'id':'000000'})
        u1.email_user('Posible - ' + msg ,message, 'hola@posible.org.mx',)
        u2 = Usuarios.objects.filter(email__iexact = 'alejandra.guerrero@fundaciontelevisa.org').first()
        message = get_template('controlPanel/folio_template.html').render({'name':u2.nombre,'folio':now ,'id':'000000'})
        u2.email_user('Posible - ' + msg ,message, 'hola@posible.org.mx',) 
        return cont
    def get(self, request):
        if not request.user.is_staff and not request.user.is_superuser and request.user.usuario != 'hugo':
            raise Http404
        t_min = date(2018,2,26)
        t_max = date(2018,3,2)
        p_email_folio = Proyectos.objects.filter(fecha_envio_a_revision__gte=str(t_min),fecha_envio_a_revision__lte=str(t_max)).count()
        return render(request, 'administrator/ss_dash.html',{'total_mails':p_email_folio,
                                                             
                                                            })
    def post(self, request):
        if not request.user.is_staff and not request.user.is_superuser and request.user.usuario != 'hugo':
            raise Http404
        t_min = date(2018,2,26)
        t_max = date(2018,3,2)
        p_email_folio = Proyectos.objects.filter(fecha_envio_a_revision__gte=str(t_min),fecha_envio_a_revision__lte=str(t_max))
        tot = self.sender(p_email_folio)
        return render(request, 'administrator/ss_dash.html',{'total_mails':p_email_folio, 'total' : tot, 'sending': True
                                                             
                                                            })'''
class envio_correos (View):
    day7 = date.today() - timedelta(days=7)
    
    def sender(self, proys,tipo):
        msg = '¡Te invitamos a concluir tu modelo de negocio!'
        if tipo == '50':
            temp = '050_template'
            msg = '¡Te invitamos a avanzar tu modelo de negocio!'
        elif tipo == '75':
            temp = '5075_template'
        elif tipo == '90':
            temp = '7590_template'
        elif tipo == '100':
            temp = '90100_template'
        message = get_template('administrator/'+temp+'.html').render()
        cont = 0
        for p in proys:
            #print(tipo+' enviando a: ' + p.email)
            u = Usuarios.objects.filter(email__iexact = p.email).first()
            if u is not None:
                u.email_user('Posible - ' + msg ,message, 'hola@posible.org.mx',)
                cont += 1
                if cont%14 == 0: #WE HAVE A CUOTA OF 14 MAILS PER SECOND :/
                    time.sleep(1)
        u1 = Usuarios.objects.filter(email__iexact = 'hugo.huipet@fundaciontelevisa.org').first()
        u1.email_user('Posible - ' + msg ,message, 'hola@posible.org.mx',)
        u2 = Usuarios.objects.filter(email__iexact = 'alejandra.guerrero@fundaciontelevisa.org').first()
        u2.email_user('Posible - ' + msg ,message, 'hola@posible.org.mx',) 
        return cont
    def get(self, request):
        if not request.user.is_staff and not request.user.is_superuser and request.user.usuario != 'hugo':
            raise Http404
        p_0_50 = Proyectos.objects.filter(avance_total__gte=0,avance_total__lte=50)
        p_0_50_7 = Proyectos.objects.filter(avance_total__gte=0,avance_total__lte=50,fecha_creacion__lte=self.day7)
        
        p_50_75 = Proyectos.objects.filter(avance_total__gt=50,avance_total__lte=75)
        p_50_75_7 = Proyectos.objects.filter(avance_total__gt=50,avance_total__lte=75,fecha_creacion__lte=self.day7)
        
        p_75_90 = Proyectos.objects.filter(avance_total__gt=75,avance_total__lte=90)
        p_75_90_7 = Proyectos.objects.filter(avance_total__gt=75,avance_total__lte=90,fecha_creacion__lte=self.day7)
        
        p_90_100 = Proyectos.objects.filter(avance_total__gt=90,avance_total__lte=100,status='borrador')
        p_90_100_7 = Proyectos.objects.filter(avance_total__gt=90,avance_total__lte=100,status='borrador',fecha_creacion__lte=self.day7)
        return render(request, 'administrator/ss_dash.html',{'p_0_50_7':p_0_50_7,
                                                             'p_0_50':p_0_50,
                                                             'p_50_75' : p_50_75,
                                                             'p_50_75_7':p_50_75_7,
                                                             'p_75_90':p_75_90,
                                                             'p_75_90_7':p_75_90_7,
                                                             'p_90_100':p_90_100,
                                                             'p_90_100_7':p_90_100_7
                                                            })
    def post(self,request):
        if not request.user.is_staff and not request.user.is_superuser and request.user.usuario != 'hugo':
            raise Http404
        op_0_50 = request.POST.get('0_50_op','1')
        op_50_75 = request.POST.get('50_75_op','1')
        op_75_90 = request.POST.get('75_90_op','1')
        op_90_100 = request.POST.get('90_100_op','1')
        
        if op_0_50 == '1':
            p_0_50 = Proyectos.objects.filter(avance_total__gte=0,avance_total__lte=50)
        else: 
            p_0_50 = Proyectos.objects.filter(avance_total__gte=0,avance_total__lte=50,fecha_creacion__lte=self.day7)
        if op_50_75 == '1':
            p_50_75 = Proyectos.objects.filter(avance_total__gt=50,avance_total__lte=75)
        else: 
            p_50_75 = Proyectos.objects.filter(avance_total__gt=50,avance_total__lte=75,fecha_creacion__lte=self.day7)
        if op_75_90 == '1':
            p_75_90 = Proyectos.objects.filter(avance_total__gt=75,avance_total__lte=90)
        else:
            p_75_90 = Proyectos.objects.filter(avance_total__gt=75,avance_total__lte=90,fecha_creacion__lte=self.day7)
        if op_90_100 == '1':
            p_90_100 = Proyectos.objects.filter(avance_total__gt=90,avance_total__lte=100,status='borrador')
        else:
            p_90_100 = Proyectos.objects.filter(avance_total__gt=90,avance_total__lte=100,status='borrador',fecha_creacion__lte=self.day7)
        
        env_50 = self.sender(p_0_50, '50')
        env_75 = self.sender(p_50_75, '75')
        env_90 = self.sender(p_75_90, '90')
        env_100 = self.sender(p_90_100, '100')
        return render(request, 'administrator/ss_dash2.html' ,{'sending': True,
                                                              'env_50' : str(env_50)+ ' de ' + str(p_0_50.count()) +' correos',
                                                              'env_75' : str(env_75) + ' de ' + str(p_50_75.count()) +' correos',
                                                              'env_90' : str(env_90) + ' de ' + str(p_75_90.count()) +' correos',
                                                              'env_100' : str(env_100) + ' de ' + str(p_90_100.count()) +' correos',
                                                              })

def encuestas_csv(request):
    if request.user.is_staff and request.user.is_superuser:
        # Create the HttpResponse object with the appropriate CSV header.
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="Encuestas.csv"'
        listEncuesta = Encuesta.objects.all()
        writer = csv.writer(response)
        writer.writerow(['email','Videos animados','Mini clase','Glosario','Modelo Negocio Posible','Leíste Articulos','Te fueron útiles los artículos','Observación o sugerencia'])
        for elem in listEncuesta:          
            writer.writerow([elem.email, elem.pregunta1,elem.pregunta2,elem.pregunta3,elem.pregunta4,elem.pregunta5,elem.pregunta6,elem.pregunta7])
        return response
    else:
        raise Http404