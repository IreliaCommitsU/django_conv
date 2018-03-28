from random import SystemRandom
import bcrypt

def gen_psw(word):
    sha='./1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    salt = '$2a$10$'
    for _ in range(0,25):
        salt = salt + SystemRandom().choice(sha)
    salt = salt + '$'
    
    word = word.encode('utf_8')
    salt = salt.encode(encoding='utf_8')
    result = bcrypt.hashpw(word, salt)
    return result

def print_name(**kwargs):
    try:
        f_name = kwargs['details']['first_name']
        l_name = kwargs['details']['last_name']
        #kwargs['user'] = User.objects.get(email=email)
        #print("Su nombre es ", f_name,l_name)
    except:
        #print('POS NO ENTRE')
        pass
    return kwargs


def randomPSWcode():
    code = ''
    for _ in range(0,8):
        code += SystemRandom().choice('1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
    return code

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
    

