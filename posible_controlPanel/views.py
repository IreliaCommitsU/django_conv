from django.shortcuts import render,redirect
from django.core.files.base import ContentFile
from django.utils import timezone
from django.http.response import Http404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from posible_controlPanel.helpers import progressCalculator, is_mine, validateModules
from posible_login_reg.models import Estados as es, Estados
from posible_controlPanel.models import Proyectos, ModuleAssets, Encuesta,\
    Paneles, PanelAgenda
from posible_controlPanel.forms import ProfileForm, PageOne, PageTwo, PageThree, PageFour, PageFive, PageSix, PageSeven, EncuestaForm,ProfileClosed,\
    PanelAgendaForm
from posible_controlPanel.pdfLibrary import PdfPrint
from django.contrib.auth import logout
from base64 import b64decode
from django.views import View
from _io import BytesIO
from django.template.loader import get_template
import bcrypt
from django.contrib.auth.mixins import LoginRequiredMixin

conv_stage = 3 # THIS VARIABLE CONTROLS THE DISPLAY OF THE CONVOCATORIA CURRENT STATE: 1- Conv registry of ideas, 2- StandBy Before Panels, 3.- People selected for panels, etc.

# Create your views here.
@login_required(login_url='/login/')
def control_panel(request):
    if request.user.is_staff: #HACK TO LOGOUT ADMINS WHEN VISITING SITE TO PREVENT ERROR 500
        logout(request)
        return redirect('/login/')
    
    vid = request.user.porcentaje_perfil == None #FIRST TIME LOGIN -> REDIRECT TO PROFILE 
    if vid:
        return redirect('/principal/perfil/')
    
    res = request.GET.get('p','0') # CONTROLS REVISION EXITO POPUP DISPLAY.
    res = int(res) == 606
    
    us =request.user   #GET USER STATE NAME
    if us.id_estado:
        est = es.objects.get(id_estado=us.id_estado)
        est = est.estado
    else:
        est = None

    pUser = Proyectos.objects.filter(email=us.email) # GET PROJECTS OF USER, NEVER PROJECT GIVEN ID
    cPro = pUser.count()
    
    lista_p = None
    lista_w = None
    progreso_usr = round(progressCalculator(us))
    if us.porcentaje_perfil != 100:
        us.porcentaje_perfil = progreso_usr
    
    has_encuesta = Encuesta.objects.filter(email=us.email).count() > 0 # False "no ha llenado encuesta" True "ya llenó encuesta"
    ya_envio = False
    winner = False
    if conv_stage == 1:
        lista_p=[]
        for ps in pUser:
            if ps.status != 'borrador':
                ya_envio = True
            rem_mods = validateModules(ps)
            lista_p.append( {
                             'type':'project',
                             'name':ps.modulo_2_1 ,
                             'idn':ps.id,
                             'status':ps.status,
                             'f_rev' :ps.fecha_envio_a_revision,
                             'img_url':ps.modulo_2_5.url, 
                             'avance':ps.avance_total,
                             'mod_faltan':rem_mods
                            } 
                           )
        if cPro < 3: #REMAINING 'EMPTY' PROJECTS MUST RENDER AN OBJECT
            for _ in range(0,3-cPro):
                lista_p.append({'type':'EMPTY'})
        enc = EncuestaForm()
    elif conv_stage == 2:
        ya_envio = True
        lista_p = [{'type':'project',
                    'name':ps.modulo_2_1, 
                    'idn':ps.id,
                    'status':ps.status,
                    'f_rev' :ps.fecha_envio_a_revision,
                    'img_url':ps.modulo_2_5.url, 
                    } for ps in pUser if ps.status != 'borrador']
        enc = None
    elif conv_stage == 3:
        ya_envio = True
        pa = PanelAgenda.objects.filter(email = us.email)
        ya_agendados = [e.id_proyecto for e in pa]
        lista_p = [{'type':'project',
            'name':ps.modulo_2_1, 
            'idn':ps.id,
            'status':ps.status,
            'f_rev' :ps.fecha_envio_a_revision,
            'img_url':ps.modulo_2_5.url, 
            } for ps in pUser if ps.status != 'borrador']
        lista_w = [{'type':'project',
            'name':ps.modulo_2_1, 
            'idn':ps.id,
            'status':ps.status,
            'f_rev' :ps.fecha_envio_a_revision,
            'img_url':ps.modulo_2_5.url, 
            'cita':ps.id in ya_agendados,
            } for ps in pUser if ps.status == 'paneles']
        winner = len(lista_w) > 0
        enc = None
           
    return render(request,'controlPanel/controlPanel.html',{'estado':est,
                                                            'pAvance':progreso_usr,
                                                            'lista_p': lista_p,
                                                            'lista_w':lista_w,
                                                            'form_encuesta':enc,
                                                            'tiene_encuesta':has_encuesta,
                                                            'ya_envio':ya_envio,
                                                            'info_box':res,
                                                            'etapa_convocatoria': conv_stage,
                                                            'winner':winner,
                                                            })

@login_required(login_url='/login/')
def profileEditor(request):
    vid = request.user.porcentaje_perfil == None
    if vid:
        request.user.porcentaje_perfil = 0
        request.user.save() 
    VERTICALES_ID = {2:'1', 20:'2',25:'3'} #1 bc 2 oax 3 sinaloa 0 ninguno
    pUser = Proyectos.objects.filter(email=request.user.email) 
    
    ya_envio = False
    has_soc = request.user.socios != None and request.user.socios!=""  
    for ps in pUser:
        if ps.status != 'borrador':
            ya_envio = True
            break
    if request.method == 'POST':
        image_data = None
        imgBase64 = request.POST.get('dtaImg','')
        pressed_btn = request.POST.get('s_prof','')
        if not ya_envio:
            form = ProfileForm(data=request.POST,files= request.FILES ,instance=request.user)
        else:
            form = ProfileClosed(data=request.POST,files= request.FILES ,instance=request.user)
        vert = VERTICALES_ID.get(form.instance.id_estado)
        if form.is_valid():
            usu = form.save(commit=False)
            if imgBase64.strip() != "":
                _, imgstr = imgBase64.split(';base64,')
                image_data = b64decode(imgstr)
                usu.foto = ContentFile(image_data, str(usu.id)+'.png')
            usu.user = request.user
            usu.save()
            if pressed_btn == "1":
                return redirect('/principal/')
            else:
                if not ya_envio:
                    form = ProfileForm(data=request.POST,files= request.FILES ,instance=request.user)
                else:
                    form = ProfileClosed(data=request.POST,files= request.FILES ,instance=request.user)
                vert = VERTICALES_ID.get(form.instance.id_estado)
                return render(request, 'controlPanel/profile.html', {'form': form,
                                                                 'vert':vert,
                                                                 'img_photo':request.user.foto.url,
                                                                 'has_sh': has_soc,
                                                                 'ya_envio':ya_envio,
                                                                })
        else:
            return render(request, 'controlPanel/profile.html', {'form': form,
                                                                 'vert':vert,
                                                                 'img_photo':request.user.foto.url,
                                                                 'has_sh': has_soc,
                                                                 'ya_envio':ya_envio,
                                                                })
    else:
        if not ya_envio:
            form = ProfileForm(instance=request.user)
        else:
            form = ProfileClosed(instance=request.user)
        vert = VERTICALES_ID.get(form.instance.id_estado)
        return render(request, 'controlPanel/profile.html', {'form': form,
                                                             'vert':vert,
                                                             'img_photo':request.user.foto.url,
                                                             'has_sh': has_soc,
                                                             'ya_envio':ya_envio,
                                                             'ver_video':vid,
                                                             })
    
@login_required(login_url='/login/')
def projectCreator(request):
    if conv_stage != 1:
        raise Http404
    us = request.user
    pUser = Proyectos.objects.filter(email=us.email).count()
    if pUser == 3:
        return redirect('/principal/') #CHECK VALIDATION FOR USER PROJECTS (NO MORE THAN 3) (MAYBE ADD MESSAGE)
    
    mod_assts = ModuleAssets.objects.filter(module_id=1)
    if request.method == 'POST':
        form = PageOne(data=request.POST)
        se = request.POST.get('save_exit','')
        sc = request.POST.get('next','')
        if form.is_valid(): #TODO: CALCULATE PROGRESS OF THIS PART BY COUNTING GOOD QUESTIONS - EMPTY QUESTIONS - WRONG QUESTIONS
            now = timezone.now()
            pInstance = form.save(commit=False)
            pInstance.uuid_usuario = request.user.uuid
            pInstance.email = request.user.email
            pInstance.status = 'borrador'
            pInstance.privado = 0
            pInstance.fecha_creacion = now
            pInstance.avance_modulo_1=progressCalculator(pInstance) #FOR SOME REASON I STILL DON'T UNDERSTAND ON CREATION DEFAULT VALUES FOR OTHER 'AVANCES' IS NOT TRIGGERING
            pInstance.avance_modulo_2=0
            pInstance.avance_modulo_3=0
            pInstance.avance_modulo_4=0
            pInstance.avance_modulo_5=0
            pInstance.avance_modulo_6=0
            pInstance.avance_modulo_7=0
            pInstance.id_estado = us.id_estado
            pInstance.save()
            if se == "1":
                return redirect('/principal/')
            elif sc=="1":
                id_proy =  pInstance.id
                return redirect('/principal/proyecto/'+str(id_proy)+'/2/')
            else:
                return redirect('/principal/')   #TODO VERIFY POSSIBILITY OF NEITHER OPTION PRESSED AND REDIRECT TO 404 OR SOMETHING
        else:
            return render(request, 'controlPanel/canvas.html', {'form': form,
                                                                'mod_number':1,
                                                                'mod_label':'1. Describe el problema',
                                                                'module_a':mod_assts,
                                                                'url_action':'../nuevoProyecto/',
                                                                'creacion': True
                                                                })
    else:
        form = PageOne()
        return render(request, 'controlPanel/canvas.html', {'form': form, 
                                                            'mod_number':1,
                                                            'mod_label':'1. Describe el problema',
                                                            'module_a':mod_assts,
                                                            'url_action':'../nuevoProyecto/',
                                                            'creacion': True
                                                            })

@login_required(login_url='/login/')
def projectEditor(request, proyID, page):
    if conv_stage != 1:
        raise Http404
    #TO ENTER THIS VIEW EXISTENCE OF PROJECT IS MANDATORY
    proyID = int(proyID)
    page = int(page)
    swtch = {
        1: PageOne,
        2: PageTwo,
        3: PageThree,
        4: PageFour,
        5: PageFive,
        6: PageSix,
        7: PageSeven,
    }
    lblswtch = {
        1: '1. Describe el problema',
        2: '2. Explica tu idea de negocio',
        3: '3. Describe a tus clientes',
        4: '4. Explica tu propuesta de valor',
        5: '5: Define tu publicidad y distribución',
        6: '6: Explica cómo generas ingresos',
        7: '7: Describe tu plan de crecimiento'
    }
    #DOUBLE CHECK THAT THE PROY.USER.ID REALLY BELONGS TO USER.ID IF NOT 404()
    us = request.user
    loadP = is_mine(us.email,proyID)
    if not loadP: #PROJECT ID DOES NOT BELONG TO USER OR (PROY ID SIMPLY DOESN'T EXIST)
        raise Http404
    #IF PROJECT ALREADY 'ON REVISION' CAN'T ENTER HERE
    if loadP.fecha_envio_a_revision:
        return redirect('/principal/')
    mod_assts = ModuleAssets.objects.filter(module_id=page)
    if request.method == 'POST':
        se = request.POST.get('save_exit','')
        sc = request.POST.get('next','')
        ss = request.POST.get('go_revision','')
        so = request.POST.get('save_only','')
        form = swtch[page](data=request.POST,files= request.FILES,instance=loadP) 
        if form.is_valid():
            pInstance = form.save(commit=False)
            #CALCULATE PROGRESS OF SECTION EVERY TIME
            if page == 1:
                pInstance.avance_modulo_1 = progressCalculator(pInstance)
            if page == 2:
                pInstance.avance_modulo_2 = progressCalculator(pInstance,2)
            if page == 3:
                pInstance.avance_modulo_3 = progressCalculator(pInstance,3)
            if page == 4:
                pInstance.avance_modulo_4 = progressCalculator(pInstance,4)
            if page == 5:
                pInstance.avance_modulo_5 = progressCalculator(pInstance,5)
            if page == 6:
                pInstance.avance_modulo_6 = progressCalculator(pInstance,6)
            if page == 7:
                pInstance.avance_modulo_7 = progressCalculator(pInstance,7)
            suma = pInstance.avance_modulo_1 + \
                   pInstance.avance_modulo_2 + \
                   pInstance.avance_modulo_3 + \
                   pInstance.avance_modulo_4 + \
                   pInstance.avance_modulo_5 + \
                   pInstance.avance_modulo_6 + \
                   pInstance.avance_modulo_7
            pInstance.avance_total = round(suma / 7)
            
            if se == "1":
                pInstance.save()
                return redirect('/principal/')
            elif sc=="1":
                pInstance.save()
                return redirect('/principal/proyecto/'+str(proyID)+'/'+str(page+1)+'/')
            elif so == "1":
                pInstance.save()
                return redirect('/principal/proyecto/'+str(proyID)+'/'+str(page)+'/')
            elif ss == "1":
                pInstance.save()
                rem_mods = validateModules(pInstance)
                progreso_usr = round(progressCalculator(us))
                pro_values ={'name':pInstance.modulo_2_1,
                             'mod_faltan':rem_mods,
                             'avance':pInstance.avance_total,
                             'idn':pInstance.id,
                            } 
                return render(request,'controlPanel/canvas.html',{'form':form,
                                                              'mod_number':page,
                                                              'proy_id': proyID,
                                                              'mod_label':lblswtch[page],
                                                              'module_a':mod_assts,
                                                              'url_action':'../../../proyecto/'+str(proyID)+'/'+str(page)+'/',
                                                              'saveRev': True,
                                                              'p':pro_values,
                                                              'pAvance':progreso_usr
                                                              })
            else:
                return redirect('/principal/') #NO BUTTON WAS PRESSED THIS BEHAVIOUR WEIRD MAYBE: 404?
        else: #THIS MUST NOT HAPPEN A LOT :S
            return render(request,'controlPanel/canvas.html',{'form':form,
                                                              'mod_number':page,
                                                              'proy_id': proyID,
                                                              'mod_label':lblswtch[page],
                                                              'module_a':mod_assts,
                                                              'url_action':'../../../proyecto/'+str(proyID)+'/'+str(page)+'/'})
    else:
        if page >=1 and page <=7:
            #PAGE OF PROJECT ALREADY HAS VALUES? Y: LOAD IT N: RENDER QUESTIONS EMPTY
            form = swtch[page](instance = loadP)
            return render(request,'controlPanel/canvas.html',{'form':form,
                                                              'mod_number':page,
                                                              'proy_id': proyID,
                                                              'mod_label':lblswtch[page],
                                                              'module_a':mod_assts,
                                                              'url_action':'../../../proyecto/'+str(proyID)+'/'+str(page)+'/'})
        else: #PAGE DON'T EXIST
            return redirect('/principal/') #TODO: DISPLAY ERROR MESSAGE OR 404() MAYBE... FOR THE TIME BEING LEAVING LIKE THAT

@login_required(login_url='/login/')
def send_revision(request,proyID):
    if conv_stage != 1:
        raise Http404
    result = 404
    if request.method != 'POST':
        proyID = int(proyID)
        us = request.user
        loadP = is_mine(us.email,proyID)
        if not loadP: #PROJECT ID DOES NOT BELONG TO USER OR (PROY ID SIMPLY DOESN'T EXIST)
            raise Http404
        if loadP.status != 'borrador':
            raise Http404 #PROJECT HAS ALREADY BEING SEND TO REVISION
        result=303
        if loadP.avance_total < 100:
            return redirect('/principal/?p=%s' % result )
        else: #AVANCE_TOTAL IS GOOD THEN REVISION 
            result= 606
            now = timezone.now()
            loadP.fecha_envio_a_revision = now
            loadP.status = 'revision'
            loadP.id_estado=us.id_estado
            loadP.save()
            message = get_template('controlPanel/folio_template.html').render({'name':us.nombre,'folio':now ,'id':loadP.id})
            us.email_user('Posible - Envio proyecto exitoso',message, 'hola@posible.org.mx')
            return redirect('/principal/?p=%s' % result )
    return redirect('/principal/?p=%s' % result )

@login_required(login_url='/login/')
def pdf_generation(request,proyID):
    proyID = int(proyID)
    us = request.user
    loadP = is_mine(us.email,proyID)
    if not loadP: #PROJECT ID DOES NOT BELONG TO USER OR (PROY ID SIMPLY DOESN'T EXIST)
        raise Http404 
    if loadP.status == 'borrador': #CAN'T PRINT PDFS OF INCOMPLETE PROJECTS
        raise Http404
    fileName = loadP.fecha_envio_a_revision.strftime("%Y%m%d")+str(loadP.id)
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="'+fileName+'.pdf"'
    buffer = BytesIO()
    report = PdfPrint(buffer, 'Letter')
    pdf = report.report('POSiBLE - Modelo de Negocio',fileName,loadP)
    response.write(pdf)
    return response

@login_required(login_url='/login/')
def changePSW(request):     
    if request.method == 'POST':
        current = request.POST.get('p','')
        new = request.POST.get('np','')
        us = request.user
        if bcrypt.checkpw(current.encode('utf8'), us.password.encode('utf8')):
            us.set_password(new)
            us.save()
            result = 'yes' #TODO PASSWORD CHANGE
        else: # Current password is not correct
            result = 'no' #TODO PASSWORD NOT CHANGE
    return redirect('/login/?pcd=%s' % result)

@login_required(login_url='/login/')
def encuesta_send(request):
    if conv_stage != 1:
        raise Http404
    if request.method == 'POST':
        form = EncuestaForm(data=request.POST)
        if form.is_valid():
            eInstance = form.save(commit=False)
            eInstance.uuid = request.user.uuid 
            eInstance.email = request.user.email
            eInstance.save()
        return redirect('/principal/')
    

class agendeo(LoginRequiredMixin,View):
    login_url = '/login/'
    def get(self,request, proyID):
        us = request.user
        proyID = int(proyID)
        pUser = Proyectos.objects.filter(email=us.email,status='paneles',pk = proyID)
        if pUser.count() == 0:
            raise Http404
        
        has_agenda = PanelAgenda.objects.filter(id_proyecto = proyID,email=us.email).count() > 0 
        if has_agenda:
            return redirect('/principal/proyecto/'+str(proyID)+'/resumen/')
        
        datos_paneles = Paneles.objects.filter(id_estado=us.id_estado)
        fAgenda_panel = PanelAgendaForm()
        pUser = pUser.first()
        proyecto_agendar = {
                             'type':'project',
                             'name':pUser.modulo_2_1 ,
                             'idn':pUser.id,
                             'f_rev': pUser.fecha_envio_a_revision,
                            }  # ONLY RETURNS ONE PROJECT DEFINED BY PROYID
        return render(request, 'controlPanel/agenda.html', {'form': fAgenda_panel, 
                                                            'proyecto': proyecto_agendar, 
                                                            'datos':datos_paneles,
                                                            'etapa_convocatoria':conv_stage,
                                                            'ya_envio':True
                                                            })
    def post(self,request,proyID):
        form = PanelAgendaForm(data = request.POST)
        if form.is_valid():
            us = request.user
            pa = form.save(commit = False)
            proyID = int(proyID)
            pUser = Proyectos.objects.filter(email=us.email,status = 'paneles', pk=proyID)
            datos_paneles = Paneles.objects.filter(id_estado=us.id_estado)
            
            if pUser.count() == 0:
                raise Http404
            proyecto_agendado = pUser.first()
            pa.id_panel = datos_paneles.first().pk # change to validation of panel
            pa.id_proyecto = proyecto_agendado.id
            pa.uuid = us.uuid
            pa.email = us.email
            pa.nombre_proyecto = proyecto_agendado.modulo_2_1
            pa.save()
        else:
            print('no es valido')
            print(form.errors)
        return redirect('/principal/')

class resumen(LoginRequiredMixin,View):
    login_url = '/registro/'
    def get(self, request,proyID):
        us = request.user
        proyID = int(proyID)
        panel = None
        try:
            pa = PanelAgenda.objects.get(id_proyecto__iexact = proyID, email=us.email)
            panel = Paneles.objects.get(pk = pa.id_panel)
            estadoname = Estados.objects.get(pk = panel.id_estado)
        except PanelAgenda.DoesNotExist:
            raise Http404
        return render(request,'controlPanel/resumen.html',{'pa':pa,'panel':panel,'estado':estadoname.estado, 'ya_envio':True})

#TODO IN THE FUTURE
@login_required(login_url='/login/')
def travel_tickets_selection(request):
    #FUTURE
    return 0