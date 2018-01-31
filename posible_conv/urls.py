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
from posible_login_reg.views import landing,log_in,register,log_out,\
    change_PS_page, forgot_PSW, aviso
from posible_controlPanel.views import control_panel, profileEditor, \
    changePSW, pdf_generation,projectCreator, projectEditor,send_revision,\
    encuesta_send
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse

urlpatterns = [
    #DASHBOARD ADMIN
    url(r'^admin/', admin.site.urls),
    
    #LANDING PAGE BEFORE STARTING
    url(r'^$', register),
    #PRIVACY NOTICE FACEBOOK COMPLIANCE
    url(r'^aviso_privacidad/$',aviso),
    #LOGIN URLS
    url(r'^login/$', log_in),
    url(r'^logout/$', log_out),
    url(r'^login/forgotPSW/$', forgot_PSW),
    url('', include('social_django.urls', namespace='social')),
    #THANKYOU
    url(r'^thanks/$', landing),
    
    #REGISTER URLS
    url(r'^registro/$',register),
    url(r'^cambiarClave/$',change_PS_page),
    #url(r'^dashboard/$',register),
    
    url(r'^principal/$',control_panel),
    url(r'^principal/perfil/$',profileEditor),
    url(r'^principal/nuevoProyecto/$',projectCreator),
    url(r'^principal/proyecto/(\d{1,6})/(\d)/',projectEditor),
    url(r'^principal/proyecto/(\d{1,6})/revision/',send_revision),
    url(r'^principal/proyecto/(\d{1,6})/pdf/',pdf_generation),
    url(r'^principal/cambiar/', changePSW),
    url(r'^principal/encuesta/', encuesta_send ),
    #url(r'^google9994b74c9bd93b22\.html$', lambda r: HttpResponse("google-site-verification: google9994b74c9bd93b22.html"))
]
#BEWARE THIS ONLY IS FOR DEVELOPMENT LOOK FOR CDN IMPLEMENTATION FOR SERVER
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
