"""posible_conv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from posible_administrator.views import encuestas_csv, envio_correos,\
    customer_service
from posible_login_reg.views import landing,log_out,\
    change_PS_page, forgot_PSW, aviso, log_in_class, register_class,\
    offline_registry, info_graphic
from posible_controlPanel.views import control_panel, profileEditor, \
    changePSW, pdf_generation,projectCreator, projectEditor,send_revision,\
    encuesta_send, agendeo, resumen
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse

urlpatterns = [
    #DASHBOARD ADMIN
    url(r'^admin/', admin.site.urls),
    url(r'^encuestas/$',encuestas_csv),
    url(r'^mailersend/$',envio_correos.as_view()),
    url(r'^servicio/$',customer_service.as_view()),
    #LANDING PAGE BEFORE STARTING
    url(r'^$', register_class.as_view()),
    url(r'^convocatoria/$',info_graphic),
    #PRIVACY NOTICE FACEBOOK COMPLIANCE
    url(r'^aviso_privacidad/$',aviso),
    #LOGIN URLS
    url(r'^login/$', log_in_class.as_view()),
    url(r'^logout/$', log_out),
    #OFFLINE URLS
    #url(r'^offline/$', offline_registry.as_view()),
    #VERTICAL SINALOA
    url(r'^sinaloa/$', register_class.as_view(template_name='login_reg/sinaloaLR.html')),
    #VERTICAL OAXACA
    url(r'^oaxaca/$', register_class.as_view(template_name='login_reg/oaxaca.html')),
    #VERTICAL BAJA CALIFORNIA
    url(r'^bajacalifornia/$', register_class.as_view(template_name='login_reg/bajacalifornia.html')),
    
    url(r'^login/forgotPSW/$', forgot_PSW),
    url(r'^forgotPSW/$', forgot_PSW),
    url(r'^registro/forgotPSW/$', forgot_PSW),
    url('', include('social_django.urls', namespace='social')),
    #THANKYOU
    url(r'^thanks/$', landing),

    #REGISTER URLS
    url(r'^registro/$',register_class.as_view()),
    url(r'^cambiarClave/$',change_PS_page),
    #url(r'^dashboard/$',register),
    
    url(r'^principal/$',control_panel, name='principal'),
    url(r'^principal/perfil/$',profileEditor),
    url(r'^principal/nuevoProyecto/$',projectCreator),
    url(r'^principal/proyecto/(\d{1,6})/(\d)/',projectEditor),
    url(r'^principal/proyecto/(\d{1,6})/revision/',send_revision),
    url(r'^principal/proyecto/(\d{1,6})/pdf/',pdf_generation),
    url(r'^principal/proyecto/(\d{1,6})/cita/',agendeo.as_view()),
    url(r'^principal/proyecto/(\d{1,6})/resumen/',resumen.as_view()),
    url(r'^principal/cambiar/', changePSW),
    url(r'^principal/encuesta/', encuesta_send ),

    #url(r'^google9994b74c9bd93b22\.html$', lambda r: HttpResponse("google-site-verification: google9994b74c9bd93b22.html"))
]
#BEWARE THIS ONLY IS FOR DEVELOPMENT LOOK FOR CDN IMPLEMENTATION FOR SERVER
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
