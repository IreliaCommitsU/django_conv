from django import forms

from posible_login_reg.models import Usuarios, CodigosPostales
from posible_controlPanel.models import Proyectos, Encuesta
from django.utils.translation import gettext_lazy as _
from posible_controlPanel.custom_widgets import NonClearableImageInput, SociosMultiWidget
from posible_controlPanel.choices import *
from posible_controlPanel.labels import *
from posible_controlPanel.helpers import jsonify

MULTI_OPTION_MESSAGE = '* Puedes seleccionar más de una opción.'
WORDS_30_MESSAGE = '* Máximo 30 palabras.'


class ProfileForm(forms.ModelForm):
    id_estado = forms.ChoiceField(required = True,choices = PS_STATES)
    nacimiento = forms.DateField(required = False,
                                widget=forms.TextInput(attrs={'class':'datepicker'}),
                                 label = 'Fecha de Nacimiento')
    como_te_enteraste = forms.MultipleChoiceField(required = False,
                                widget= forms.CheckboxSelectMultiple ,
                                choices = ENTERASTE,
                                                 )
    sexo = forms.ChoiceField(required = False,widget = forms.RadioSelect, 
                                      choices = GENDER, 
                                      label='Género')
    maximo_grado = forms.ChoiceField(required = False,choices = GRADE_STUDIES)
    email = forms.CharField(disabled = True, 
                            widget=forms.TextInput(),
                            )
    municipio = forms.ModelChoiceField(required= False, queryset=None,
                                       empty_label="")
    tel_1_lada = forms.CharField(required = False,label='',  max_length=4,
                    widget=forms.TextInput(attrs={'placeholder': 'LADA'}))
    tel_2_lada = forms.CharField(required = False,label='', max_length=4,
                    widget=forms.TextInput(attrs={'placeholder': 'LADA'}))
    tel_1= forms.CharField(required = False,label='',  max_length=12,
                    widget=forms.TextInput())
    tel_2 = forms.CharField(required = False,label='', max_length=12,
                    widget=forms.TextInput())
    area_experiencia = forms.CharField(required=False, max_length=140,
                                       widget=forms.TextInput(attrs={'placeholder': '140 caracteres máximo'})
                                       )
    socios = forms.CharField(required=False,widget = SociosMultiWidget(attrs={'class': 'size_inputs'}))
    class Meta:
        model = Usuarios
        fields = [
            'nombre',
            'apellido',
            'foto',
            'nacimiento',
            'maximo_grado',
            'escuela',
            'id_estado',
            'municipio',
            'sexo',
            'email',
            'email_alt',
            'tel_1_lada',
            'tel_1',
            'tel_2_lada',
            'tel_2',
            'como_te_enteraste',
            'area_experiencia',
            'socios', #ITS A JSON WITH THE NAME, EMAIL AND EXPERTISE
        ]
        labels = {
            'nacimiento' : _('Fecha de nacimiento'),
            'maximo_grado': _('Máximo grado de estudios'),
            'escuela' : _('Institución educativa'),
            'id_estado' : _('Estado'),
            'email' : _('Correo'),
            'email_alt' : _('Correo alterno'),
            'tel_1' : _('Teléfono 1'),
            'tel_1_lada' : _('lada 1'),
            'tel_2' : _('Teléfono 2'),
            'tel_2_lada' : _('lada 2'),
        }
    
    def __init__(self, *args, **kwargs):
        super(ProfileForm,self).__init__(*args, **kwargs)
        self.fields['municipio'].queryset = CodigosPostales.objects.filter(id_estado=self.instance.id_estado).order_by('municipio').values_list('municipio',flat=True).distinct()
        if self.instance:
            obj_data = self.instance.__dict__
            if obj_data.get('_wrapped') and obj_data['_wrapped'].como_te_enteraste:
                self.initial['como_te_enteraste'] =jsonify(obj_data['_wrapped'].como_te_enteraste) #KEEP AN EYE ON THIS CODE ¬¬
    def clean(self):
        super(ProfileForm, self).clean() #if necessary
        if 'socios' in self._errors:
            del self._errors['socios']
        if 'municipio' in self._errors:
            del self._errors['municipio']
        listSocios = [
            {"nombre":''.join(self.data.getlist('socios_0')),
             "email" :''.join(self.data.getlist('socios_1')),
             "area": ''.join(self.data.getlist('socios_2')),
            },
            {"nombre":''.join(self.data.getlist('socios_3')),
             "email" :''.join(self.data.getlist('socios_4')),
             "area": ''.join(self.data.getlist('socios_5')),
            },
            {"nombre":''.join(self.data.getlist('socios_6')),
             "email" :''.join(self.data.getlist('socios_7')),
             "area": ''.join(self.data.getlist('socios_8')),
            },
            {"nombre":''.join(self.data.getlist('socios_9')),
             "email" :''.join(self.data.getlist('socios_10')),
             "area": ''.join(self.data.getlist('socios_11')),
            },
        ]
        if listSocios[0].get('nombre').strip() == '' and listSocios[1].get('nombre').strip() =='' and \
        listSocios[2].get('nombre').strip() =='' and listSocios[3].get('nombre').strip() =='':
            listSocios=''
        self.cleaned_data['socios']=str(listSocios)
        self.cleaned_data['municipio']=str(''.join(self.data.getlist('municipio')))
        return self.cleaned_data 

class PageOne(forms.ModelForm):
    class Meta:
        model = Proyectos
        fields = [
            'modulo_1_1',
            'modulo_1_2',
        ]
        labels = {
            'modulo_1_1':LABELS_QUESTIONS.get('modulo_1_1'),
            'modulo_1_2':LABELS_QUESTIONS.get('modulo_1_2'),
        }
        help_texts= {
            'modulo_1_1': '* Máximo 70 palabras',
            'modulo_1_2': '* Máximo 70 palabras',
        }


class PageTwo(forms.ModelForm):
    modulo_2_1 = forms.CharField(required = False,widget=forms.TextInput(),
                                 label= LABELS_QUESTIONS.get('modulo_2_1'),
                                 help_text = '* Máximo 15 palabras.',
                                 )
    modulo_2_2 = forms.ChoiceField(widget = forms.CheckboxSelectMultiple,
                                   choices = P_S,
                                   label = LABELS_QUESTIONS.get('modulo_2_2'),
                                   help_text=MULTI_OPTION_MESSAGE,
                                   )
    modulo_2_3 = forms.ChoiceField(widget = forms.CheckboxSelectMultiple,
                                   choices = IDEA_CATEGORIES,
                                   label = LABELS_QUESTIONS.get('modulo_2_3'),
                                   help_text = '* Puedes seleccionar máximo dos opciones.',
                                   )
    modulo_2_4 = forms.ChoiceField(required = False,widget = forms.RadioSelect,
                                   choices = DEV_STAGE,
                                   label = LABELS_QUESTIONS.get('modulo_2_4'),
                                   )
    modulo_2_4_otro = forms.DateField(required = False,
                                      widget=forms.TextInput(attrs={'class':'datepicker','placeholder': 'Indica la fecha de inicio de operación'}),
                                      label='', 
                                      )
    modulo_2_5 = forms.ImageField(required = False,widget=NonClearableImageInput(),
                                  label= LABELS_QUESTIONS.get('modulo_2_5'),
                                  help_text='* Opcional',)
    modulo_2_5_1 = forms.ImageField(required = False,widget=NonClearableImageInput(),
                                  label= "",
                                  help_text='* Opcional',)
    modulo_2_5_2 = forms.ImageField(required = False,widget=NonClearableImageInput(),
                                  label= "",
                                  help_text='* Opcional',)
    modulo_2_6 = forms.ChoiceField(required = False,widget = forms.CheckboxSelectMultiple,
                                   choices = DEVELOPMENTS_TECH,
                                   label = LABELS_QUESTIONS.get('modulo_2_6'), 
                                   help_text = '* De ser el caso, puedes seleccionar más de 1 opción',
                                   )
    modulo_2_7 = forms.ChoiceField(required = False,widget = forms.CheckboxSelectMultiple,
                               choices = DEVELOPMENTS_SCIENCE,
                               label = LABELS_QUESTIONS.get('modulo_2_7'),
                               help_text = '* De ser el caso, puedes seleccionar más de 1 opción',
                               )
    modulo_2_8 = forms.ChoiceField(required = False,widget = forms.RadioSelect,
                                   choices = INNOVATION,
                                   label = LABELS_QUESTIONS.get('modulo_2_8'),
                                   help_text = '* Puedes seleccionar sólo una opción.',
                                   )
    class Meta:
        model = Proyectos
        fields = [
            'modulo_2_1',
            'modulo_2_2',
            'modulo_2_3',
            'modulo_2_4',
            'modulo_2_4_otro',
            'modulo_2_5',
            'modulo_2_5_1',
            'modulo_2_5_2',
            'modulo_2_6',
            'modulo_2_7',
            'modulo_2_8',
            'modulo_2_9',
        ]
        labels = {
            'modulo_2_9': LABELS_QUESTIONS.get('modulo_2_9'),
        }
        help_texts = {
            'modulo_2_9' : '* Máximo 100 palabras'
        }
    def clean(self):
        super(PageTwo, self).clean() #if necessary
        if 'modulo_2_2' in self._errors:
            del self._errors['modulo_2_2']
        if 'modulo_2_3' in self._errors:
            del self._errors['modulo_2_3']
        if 'modulo_2_6' in self._errors:
            del self._errors['modulo_2_6']
        if 'modulo_2_7' in self._errors:
            del self._errors['modulo_2_7']
        self.cleaned_data['modulo_2_2']=str(self.data.getlist('modulo_2_2'))
        self.cleaned_data['modulo_2_3']=str(self.data.getlist('modulo_2_3'))
        self.cleaned_data['modulo_2_6']=str(self.data.getlist('modulo_2_6'))
        self.cleaned_data['modulo_2_7']=str(self.data.getlist('modulo_2_7'))
        return self.cleaned_data 
    
    def __init__(self, *args, **kwargs):
        super(PageTwo,self).__init__(*args, **kwargs)
        if self.instance:
            obj_data = self.instance.__dict__
            if obj_data.get('modulo_2_2'):
                self.initial['modulo_2_2'] = jsonify(obj_data['modulo_2_2']) #KEEP AN EYE ON THIS CODE ¬¬
            if obj_data.get('modulo_2_3'):
                self.initial['modulo_2_3'] = jsonify(obj_data['modulo_2_3']) #KEEP AN EYE ON THIS CODE ¬¬
            if obj_data.get('modulo_2_6'):
                self.initial['modulo_2_6'] = jsonify(obj_data['modulo_2_6']) #KEEP AN EYE ON THIS CODE ¬¬
            if obj_data.get('modulo_2_7'):
                self.initial['modulo_2_7'] = jsonify(obj_data['modulo_2_7']) #KEEP AN EYE ON THIS CODE ¬¬
                
class PageThree(forms.ModelForm):
    modulo_3_1 = forms.ChoiceField(widget = forms.CheckboxSelectMultiple,
                                   choices = TYPE_CLIENTS,
                                   label = LABELS_QUESTIONS.get('modulo_3_1'),
                                   help_text = MULTI_OPTION_MESSAGE,
                                   )
    modulo_3_1_2 = forms.ChoiceField(widget = forms.CheckboxSelectMultiple,
                                    choices = AGE,
                                    label = LABELS_QUESTIONS.get('modulo_3_1_2'),
                                    )
    modulo_3_1_3 = forms.ChoiceField(widget = forms.CheckboxSelectMultiple, 
                                    choices = GENDER, 
                                    label=LABELS_QUESTIONS.get('modulo_3_1_3'),
                                    )
    modulo_3_1_4  = forms.ChoiceField(widget = forms.CheckboxSelectMultiple, 
                                    choices = INCOME, 
                                    label=LABELS_QUESTIONS.get('modulo_3_1_4'),
                                    )
    modulo_3_1_5  = forms.ChoiceField(widget = forms.CheckboxSelectMultiple, 
                                    choices = POPULATION, 
                                    label=LABELS_QUESTIONS.get('modulo_3_1_5'),
                                    )
    
    modulo_3_2_2 = forms.ChoiceField(widget = forms.CheckboxSelectMultiple,
                                   choices = ENTERPRISE_SIZE,
                                   label = LABELS_QUESTIONS.get('modulo_3_2_2'),)
    modulo_3_3 = forms.ChoiceField(required = False,widget = forms.RadioSelect,
                                   choices = YES_NO,
                                   label = LABELS_QUESTIONS.get('modulo_3_3'),)
    modulo_3_4 = forms.ChoiceField(required = False,widget = forms.RadioSelect,
                                   choices = CLIENT_VOLUME,
                                   label = LABELS_QUESTIONS.get('modulo_3_4'),)
    class Meta:
        model = Proyectos
        fields = [
            'modulo_3_1',
            'modulo_3_1_2',
            'modulo_3_1_3',
            'modulo_3_1_4',
            'modulo_3_1_5',
            'modulo_3_1_6',
            'modulo_3_2_2',
            'modulo_3_2_3',
            'modulo_3_3',
            'modulo_3_4',
            'modulo_3_5',
        ]
        labels = {
            'modulo_3_1_6' : LABELS_QUESTIONS.get('modulo_3_1_6'),
            'modulo_3_2_3' : LABELS_QUESTIONS.get('modulo_3_2_3'),
            'modulo_3_5' : LABELS_QUESTIONS.get('modulo_3_5'),
        }
        help_texts = {
            'modulo_3_1_6': _('* Máximo 150 palabras'),
            'modulo_3_2_3': _('* Máximo 200 palabras'),
            'modulo_3_5': _('* Máximo 150 palabras'),
        }
    def clean(self):
        super(PageThree, self).clean() #if necessary
        def eraseErrorAddValue(fieldName,ob_self):
            if fieldName in ob_self._errors:
                del ob_self._errors[fieldName]
            return str(ob_self.data.getlist(fieldName))  
        self.cleaned_data['modulo_3_1'] = eraseErrorAddValue('modulo_3_1',self)
        self.cleaned_data['modulo_3_1_2'] = eraseErrorAddValue('modulo_3_1_2',self)
        self.cleaned_data['modulo_3_1_3'] = eraseErrorAddValue('modulo_3_1_3',self)
        self.cleaned_data['modulo_3_1_4'] = eraseErrorAddValue('modulo_3_1_4',self)
        self.cleaned_data['modulo_3_1_5'] = eraseErrorAddValue('modulo_3_1_5',self)
        self.cleaned_data['modulo_3_2_2'] = eraseErrorAddValue('modulo_3_2_2',self)    
        return self.cleaned_data 
    def __init__(self, *args, **kwargs):
        super(PageThree,self).__init__(*args, **kwargs)
        if self.instance:
            obj_data = self.instance.__dict__
            if obj_data.get('modulo_3_1'):
                self.initial['modulo_3_1'] = jsonify(obj_data['modulo_3_1']) #KEEP AN EYE ON THIS CODE ¬¬
            if obj_data.get('modulo_3_1_2'):
                self.initial['modulo_3_1_2'] = jsonify(obj_data['modulo_3_1_2']) #KEEP AN EYE ON THIS CODE ¬¬
            if obj_data.get('modulo_3_1_3'):
                self.initial['modulo_3_1_3'] = jsonify(obj_data['modulo_3_1_3']) #KEEP AN EYE ON THIS CODE ¬¬
            if obj_data.get('modulo_3_1_4'):
                self.initial['modulo_3_1_4'] = jsonify(obj_data['modulo_3_1_4']) #KEEP AN EYE ON THIS CODE ¬¬
            if obj_data.get('modulo_3_1_5'):
                self.initial['modulo_3_1_5'] = jsonify(obj_data['modulo_3_1_5']) #KEEP AN EYE ON THIS CODE ¬¬
            if obj_data.get('modulo_3_2_2'):
                self.initial['modulo_3_2_2'] = jsonify(obj_data['modulo_3_2_2']) #KEEP AN EYE ON THIS CODE ¬¬
                
        
class PageFour(forms.ModelForm):
    modulo_4_1 = forms.ChoiceField(widget = forms.CheckboxSelectMultiple, 
                                      choices = PRODUCT_BENEFITS, 
                                      label=LABELS_QUESTIONS.get('modulo_4_1'),
                                      help_text = MULTI_OPTION_MESSAGE,)
    modulo_4_1_otro = forms.CharField(required = False,label='', 
                                      widget=forms.TextInput(attrs={'class':'other_input'}),
                                      help_text = WORDS_30_MESSAGE)
    class Meta:
        model = Proyectos
        fields = [
            'modulo_4_1',
            'modulo_4_1_otro',
            'modulo_4_2',
            'modulo_4_3',
        ]
        labels = {
            'modulo_4_2' : LABELS_QUESTIONS.get('modulo_4_2'),
            'modulo_4_3' : LABELS_QUESTIONS.get('modulo_4_3'), 
        }
        help_texts = {
            'modulo_4_2' : _('* Máximo 150 palabras'),
            'modulo_4_3' : _('* Máximo 200 palabras'),
        }
    def clean(self):
        super(PageFour, self).clean() #if necessary
        if 'modulo_4_1' in self._errors:
            del self._errors['modulo_4_1']
        self.cleaned_data['modulo_4_1']=str(self.data.getlist('modulo_4_1'))
        return self.cleaned_data 
    
    def __init__(self, *args, **kwargs):
        super(PageFour,self).__init__(*args, **kwargs)
        if self.instance:
            obj_data = self.instance.__dict__
            if obj_data.get('modulo_4_1'):
                self.initial['modulo_4_1'] = jsonify(obj_data['modulo_4_1']) #KEEP AN EYE ON THIS CODE ¬¬
    
class PageFive(forms.ModelForm):
    modulo_5_1 = forms.ChoiceField(widget = forms.CheckboxSelectMultiple, 
                                      choices = PRODUCT_MARKETING, 
                                      label=LABELS_QUESTIONS.get('modulo_5_1'),
                                      help_text = MULTI_OPTION_MESSAGE
                                      )
    modulo_5_1_otro = forms.CharField(required = False,widget=forms.TextInput(attrs={'class':'other_input'}),
                                      label='', 
                                      help_text = WORDS_30_MESSAGE,
                                      )
    modulo_5_2 = forms.ChoiceField(required = False,widget=forms.RadioSelect,
                                 label=LABELS_QUESTIONS.get('modulo_5_2'), 
                                 choices = YES_WHICH_NO,
                                 help_text = '* Máximo 100 caracteres'
                                 )
    modulo_5_2_otro = forms.CharField(required = False,label='', max_length=100,
                                 widget=forms.TextInput(attrs={'placeholder': 'Escribe aquí página web y/o página de Facebook'})
                                 )
    modulo_5_3 = forms.ChoiceField(widget = forms.CheckboxSelectMultiple, 
                                      choices = PRODUCT_AVAILABILITY, 
                                      label=LABELS_QUESTIONS.get('modulo_5_3'),
                                      help_text = MULTI_OPTION_MESSAGE
                                      )
    modulo_5_3_otro = forms.CharField(required = False,widget=forms.TextInput(attrs={'class':'other_input'}),
                                      label='',
                                      help_text = WORDS_30_MESSAGE,)
    modulo_5_4 = forms.ChoiceField(required = False,widget = forms.RadioSelect,
                                   choices = YES_WHICH_NO,
                                   label = LABELS_QUESTIONS.get('modulo_5_4'),
                                )
    class Meta:
        model = Proyectos
        fields = [
            'modulo_5_1',
            'modulo_5_1_otro',
            'modulo_5_2',
            'modulo_5_2_otro',
            'modulo_5_3',
            'modulo_5_3_otro',
            'modulo_5_4',
            'modulo_5_4_otro',
            'modulo_5_5',
        ]
        labels = {
            'modulo_5_4_otro' : _(''),
            'modulo_5_5' : LABELS_QUESTIONS.get('modulo_5_5'),
        }
        help_texts = {
            'modulo_5_4_otro' : _('Escribe aquí el precio para tu producto o servicio'),
            'modulo_5_5' :_('* Máximo 150 palabras'),
        }

    def clean(self):
        super(PageFive, self).clean() #if necessary
        if 'modulo_5_1' in self._errors:
            del self._errors['modulo_5_1']
        self.cleaned_data['modulo_5_1']=str(self.data.getlist('modulo_5_1'))
        if 'modulo_5_3' in self._errors:
            del self._errors['modulo_5_3']
        self.cleaned_data['modulo_5_3']=str(self.data.getlist('modulo_5_3'))
        return self.cleaned_data 
    
    def __init__(self, *args, **kwargs):
        super(PageFive,self).__init__(*args, **kwargs)
        if self.instance:
            obj_data = self.instance.__dict__
            if obj_data.get('modulo_5_1'):
                self.initial['modulo_5_1'] = jsonify(obj_data['modulo_5_1']) #KEEP AN EYE ON THIS CODE ¬¬
            if obj_data.get('modulo_5_3'):
                self.initial['modulo_5_3'] = jsonify(obj_data['modulo_5_3']) #KEEP AN EYE ON THIS CODE ¬¬

class PageSix(forms.ModelForm):
    modulo_6_1 = forms.ChoiceField(required = False,widget = forms.RadioSelect,
                                   choices = YES_NO,
                                   label = LABELS_QUESTIONS.get('modulo_6_1'),)
    modulo_6_2 = forms.ChoiceField(widget = forms.CheckboxSelectMultiple, 
                                    choices = INCOME_GENERATION, 
                                    label=LABELS_QUESTIONS.get('modulo_6_2'),
                                    help_text = MULTI_OPTION_MESSAGE,
                                    )
                                        
    modulo_6_2_otro = forms.CharField(required = False,widget=forms.TextInput(attrs={'class':'other_input'}),
                                    label='', 
                                    help_text = WORDS_30_MESSAGE
                                    )
    modulo_6_3 = forms.ChoiceField(widget = forms.CheckboxSelectMultiple, 
                                      choices = FINANCIAL_SUPPORT, 
                                      label=LABELS_QUESTIONS.get('modulo_6_3'),
                                      help_text = MULTI_OPTION_MESSAGE,
                                      )
    modulo_6_3_otro = forms.CharField(required = False,widget=forms.TextInput(attrs={'class':'other_input'}),
                                      label='', 
                                      help_text = WORDS_30_MESSAGE
                                      )

    class Meta:
        model = Proyectos
        fields = [
            'modulo_6_1',
            'modulo_6_2',
            'modulo_6_2_otro',
            'modulo_6_3',
            'modulo_6_3_otro',
        ]

    def clean(self):
        super(PageSix, self).clean() #if necessary
        if 'modulo_6_2' in self._errors:
            del self._errors['modulo_6_2']
        self.cleaned_data['modulo_6_2']=str(self.data.getlist('modulo_6_2'))
        if 'modulo_6_3' in self._errors:
            del self._errors['modulo_6_3']
        self.cleaned_data['modulo_6_3']=str(self.data.getlist('modulo_6_3'))
        return self.cleaned_data 
    
    def __init__(self, *args, **kwargs):
        super(PageSix,self).__init__(*args, **kwargs)
        if self.instance:
            obj_data = self.instance.__dict__
            if obj_data.get('modulo_6_2'):
                self.initial['modulo_6_2'] = jsonify(obj_data['modulo_6_2']) #KEEP AN EYE ON THIS CODE ¬¬
            if obj_data.get('modulo_6_3'):
                self.initial['modulo_6_3'] = jsonify(obj_data['modulo_6_3']) #KEEP AN EYE ON THIS CODE ¬¬


class PageSeven(forms.ModelForm):
    modulo_7_1 = forms.ChoiceField(required = False,widget = forms.RadioSelect,
                                   choices = NUMBER_EMPLOYEES,
                                   label = LABELS_QUESTIONS.get('modulo_7_1'),
                                )
    modulo_7_2_1 = forms.CharField(required = False,widget=forms.TextInput(),
                                   label=LABELS_QUESTIONS.get('modulo_7_2_1'), 
                                   help_text = '* Te pedimos que listes mínimo 3 actividades.',
                                   )
    modulo_7_2_2 = forms.CharField(required = False,widget=forms.TextInput(),
                                   label='', 
                                   )
    modulo_7_2_3 = forms.CharField(required = False,widget=forms.TextInput(),
                                   label='', 
                                   )
    modulo_7_2_4 = forms.CharField(required = False,widget=forms.TextInput(),
                                   label='', 
                                   )
    modulo_7_2_5 = forms.CharField(required = False,widget=forms.TextInput(),
                                   label='', )
    class Meta:
        model = Proyectos
        fields = [
            'modulo_7_1',
            'modulo_7_2_1',
            'modulo_7_2_2',
            'modulo_7_2_3',
            'modulo_7_2_4',
            'modulo_7_2_5',
        ]
        
        
class EncuestaForm(forms.ModelForm):
    pregunta1 =  forms.ChoiceField(widget = forms.RadioSelect,
                                   choices = NUMBERS_CHOICE,
                                   label = _('1. ¿La explicación de los videos animados te ayudó a contestar las preguntas de los módulos?'),)
    pregunta2 =  forms.ChoiceField(widget = forms.RadioSelect,
                                   choices = NUMBERS_CHOICE,
                                   label = _('2. ¿La explicación de la mini clase (segundo video) de cada módulo te ayudó a conocer más sobre el tema?'),)
    
    pregunta3 =  forms.ChoiceField(widget = forms.RadioSelect,
                                   choices = NUMBERS_CHOICE,
                                   label = _('3.  ¿El glosario te fue útil para entender el significado de las palabras que desconocías?'),)
    
    pregunta4 =  forms.ChoiceField(widget = forms.RadioSelect,
                                   choices = NUMBERS_CHOICE,
                                   label = _('4. ¿El modelo de negocio POSiBLE te ayudó a estructurar tu idea de manera clara y sencilla?'),)
    
    pregunta5 =  forms.ChoiceField(widget = forms.RadioSelect,
                                   choices = YES_NO,
                                   label = _('5. ¿Leíste alguno de los artículos que se dieron como referencia?'),)
    pregunta6 =  forms.ChoiceField(widget = forms.RadioSelect,
                                   choices = YES_NO,
                                   label = _('6. Si contestaste que sí ¿Te fueron útiles los artículos que se dieron como referencia?'))
    pregunta7 = forms.CharField(required = False,widget=forms.TextInput(attrs={'class':'other_input'}),
                                   label=_('7. ¿Deseas realizar alguna observación o sugerencia?'), )
    class Meta:
        model = Encuesta
        fields = [
            'pregunta1',
            'pregunta2',
            'pregunta3',
            'pregunta4',
            'pregunta5',
            'pregunta6',
            'pregunta7',
        ]


class ProfileClosed(forms.ModelForm):
    nombre = forms.CharField(disabled = True,
                            widget=forms.TextInput(),)
    apellido = forms.CharField(disabled = True,
                            widget=forms.TextInput(),)
    id_estado = forms.ChoiceField(disabled = True,choices = PS_STATES)
    municipio = forms.CharField(disabled = True,
                            widget=forms.TextInput(),)
    nacimiento = forms.DateField(disabled = True,required = False,
                                widget=forms.TextInput(attrs={'class':'datepicker'}),
                                 label = 'Fecha de Nacimiento')
    
    sexo = forms.ChoiceField(disabled = True,widget = forms.RadioSelect, 
                                      choices = GENDER, 
                                      label='Género')
    #foto = forms.ImageField(required = False,widget=NonClearableImageInput())
    maximo_grado = forms.ChoiceField(disabled = True,choices = GRADE_STUDIES)
    escuela = forms.CharField(disabled = True,
                            widget=forms.TextInput(),)
    email = forms.CharField(disabled = True, 
                            widget=forms.TextInput(),)
    tel_1_lada = forms.CharField(disabled = True,label='', 
                    widget=forms.TextInput(attrs={'placeholder': 'LADA'}))
    tel_1 = forms.CharField(disabled = True,
                            widget=forms.TextInput(),)
    tel_2_lada = forms.CharField(label='', 
                    widget=forms.TextInput(attrs={'placeholder': 'LADA'}))
    como_te_enteraste = forms.MultipleChoiceField(disabled = True,
                                widget= forms.CheckboxSelectMultiple ,
                                choices = ENTERASTE,
                                                 )
    municipio = forms.CharField(disabled = True,
                            widget=forms.TextInput(),)
    area_experiencia = forms.CharField(disabled = True,required=False,
                                       widget=forms.TextInput())
    socios = forms.CharField(disabled = True,required=False,widget = SociosMultiWidget(attrs={'class': 'size_inputs'}))
    class Meta:
        model = Usuarios
        fields = [
            'nombre',
            'apellido',
            'foto',
            'nacimiento',
            'maximo_grado',
            'escuela',
            'id_estado',
            'municipio',
            'sexo',
            'email',
            'email_alt',
            'tel_1_lada',
            'tel_1',
            'tel_2_lada',
            'tel_2',
            'como_te_enteraste',
            'area_experiencia',
            'socios', #ITS A JSON WITH THE NAME, EMAIL AND EXPERTISE
        ]
        labels = {
            'nacimiento' : _('Fecha de nacimiento'),
            'maximo_grado': _('Máximo grado de estudios'),
            'escuela' : _('Institución educativa'),
            'id_estado' : _('Estado'),
            'email' : _('Correo'),
            'email_alt' : _('Correo alterno'),
            'tel_1' : _('Teléfono 1'),
            'tel_1_lada' : _('lada 1'),
            'tel_2' : _('Teléfono 2'),
            'tel_2_lada' : _('lada 2'),
        }
    
    def __init__(self, *args, **kwargs):
        super(ProfileClosed,self).__init__(*args, **kwargs)
        if self.instance:
            obj_data = self.instance.__dict__
            if obj_data.get('_wrapped') and obj_data['_wrapped'].como_te_enteraste:
                self.initial['como_te_enteraste'] =jsonify(obj_data['_wrapped'].como_te_enteraste) #KEEP AN EYE ON THIS CODE ¬¬

    def clean(self):
        super(ProfileClosed, self).clean() #if necessary
        if 'socios' in self._errors:
            del self._errors['socios']
        listSocios = [
            {"nombre":''.join(self.data.getlist('socios_0')),
             "email" :''.join(self.data.getlist('socios_1')),
             "area": ''.join(self.data.getlist('socios_2')),
            },
            {"nombre":''.join(self.data.getlist('socios_3')),
             "email" :''.join(self.data.getlist('socios_4')),
             "area": ''.join(self.data.getlist('socios_5')),
            },
            {"nombre":''.join(self.data.getlist('socios_6')),
             "email" :''.join(self.data.getlist('socios_7')),
             "area": ''.join(self.data.getlist('socios_8')),
            },
            {"nombre":''.join(self.data.getlist('socios_9')),
             "email" :''.join(self.data.getlist('socios_10')),
             "area": ''.join(self.data.getlist('socios_11')),
            },
        ]
        if listSocios[0].get('nombre').strip() == '' and listSocios[1].get('nombre').strip() =='' and \
        listSocios[2].get('nombre').strip() =='' and listSocios[3].get('nombre').strip() =='':
            listSocios=''
        self.cleaned_data['socios']=str(listSocios)
        return self.cleaned_data 