from django.template.defaulttags import register

@register.filter
def get_item(dictionary, key): 
    edo = str(key)
    return dictionary.get(edo)