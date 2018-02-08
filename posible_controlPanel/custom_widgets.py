from django.shortcuts import render_to_response
from django.utils.safestring import mark_safe
from django.utils.html import  conditional_escape
from django.forms.widgets import TextInput,MultiWidget, FileInput
import ast
import json
from django.template.loader import render_to_string
#ast.literal_eval("{'muffin' : 'lolz', 'foo' : 'kitty'}")


class SociosMultiWidget(MultiWidget):
    def __init__(self, attrs=None, dt=None, mode=0):  
        '''        if dt is not None:
            self.datepos = dt
        else:
            self.datepos = 'Ejemplo'  ''' 

        # bits of python to create days, months, years
        # example below, the rest snipped for neatness.

        #years = [(year, year) for year in year_digits]
        _widgets = (
            TextInput(attrs=attrs,), 
            TextInput(attrs=attrs,),
            TextInput(attrs={'placeholder': '140 caracteres','maxlength':'140',},),
            
            TextInput(attrs=attrs,), 
            TextInput(attrs=attrs,),
            TextInput(attrs={'placeholder': '140 caracteres','maxlength':'140',},),
            
            TextInput(attrs=attrs,), 
            TextInput(attrs=attrs,),
            TextInput(attrs={'placeholder': '140 caracteres','maxlength':'140',},),
            
            TextInput(attrs=attrs,), 
            TextInput(attrs=attrs,),
            TextInput(attrs={'placeholder': '140 caracteres','maxlength':'140',}),
            )
        super(SociosMultiWidget, self).__init__(_widgets, attrs)

    def decompress(self, value):
        if value:
            vDict = ast.literal_eval(value)
            lst = []
            for v in vDict: #AT LEAST 4 ELEMENTS
                lst += [v['nombre'],v['email'],v['area']]
            return lst
        return [None, None, None,None, None, None,None, None, None,None, None, None]

    
    def compress(self, data_list):
        return json.dumps(data_list)
        

    def render(self,name,value,attrs=None):
        # HTML to be added to the output
        widget_labels = [
            'for="id_%s"',
            'for="id_%s"',
            'for="id_%s"',
            
            'for="id_%s"',
            'for="id_%s"',
            'for="id_%s"',
            
            'for="id_%s"',
            'for="id_%s"',
            'for="id_%s"',
            
            'for="id_%s"',
            'for="id_%s"',
            'for="id_%s"',
        ]
        widget_names=[
            '1 Nombre:',
            'Correo:',
            'Área de experiencia:',
            
            '2 Nombre:',
            'Correo:',
            'Área de experiencia:',
            
            '3 Nombre:',
            'Correo:',
            'Área de experiencia:',
            
            '4 Nombre:',
            'Correo:',
            'Área de experiencia:',
        ]
        if self.is_localized:
            for widget in self.widgets:
                widget.is_localized = self.is_localized

        # value is a list of values, each corresponding to a widget in self.widgets
        if not isinstance(value, list):
            value = self.decompress(value)
        output = []
        final_attrs = self.build_attrs(attrs)
        id_ = final_attrs.get('id', None)
        for i, widget in enumerate(self.widgets):
            try:
                widget_value = value[i]
            except IndexError:
                widget_value = None
            if id_:
                final_attrs = dict(final_attrs, id='%s_%s' % (id_, i))
    
            output.append({
                            'for_label':widget_labels[i] % ('%s_%s' % (name, i)),
                            'label_tag':widget_names[i],
                            'input':widget.render(name + '_%s' % i, widget_value, final_attrs)
                        })
        html = render_to_string('controlPanel/widgets/wdgPartners_template.html',{'fields':output})
        return mark_safe(html)

class NonClearableImageInput(FileInput):
    def render(self, name, value, attrs=None):
        template = '%(input)s'
        data = {'input': None, 'url': None}
        data['input'] = super(NonClearableImageInput, self).render(name, value, attrs)

        if hasattr(value, 'url'):
            data['url'] = conditional_escape(value.url)
            template = '<img id="imgZone_'+name+'" src="%(url)s"> <label for="id_'+name+'" class="custom-file-upload"> <i class="fi-upload"></i> Sube tu imagen </label>%(input)s'

        return mark_safe(template % data)


    
