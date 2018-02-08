from posible_controlPanel.models import Proyectos
from posible_login_reg.models import Usuarios
import json
#HELPER FUNCTIONS
def jsonify(data):
    return json.loads(data.replace("u'","'").replace("'",'"'))

def is_mine(us_e, id_project):
    p_proy = None
    pUser = Proyectos.objects.filter(email=us_e) 
    for ps in pUser:
        if ps.id == id_project:
            p_proy = ps
            break
    return p_proy

def validateModules(pInstance=None):
    if pInstance is None or not isinstance(pInstance, Proyectos):
        return []
    rem_mods = []  
    if pInstance.avance_modulo_1 < 100:
        rem_mods.append({'value':'Módulo 1'})
    if pInstance.avance_modulo_2 < 100:
        rem_mods.append({'value':'Módulo 2'})
    if pInstance.avance_modulo_3 < 100:
        rem_mods.append({'value':'Módulo 3'})
    if pInstance.avance_modulo_4 < 100:
        rem_mods.append({'value':'Módulo 4'})
    if pInstance.avance_modulo_5 < 100:
        rem_mods.append({'value':'Módulo 5'})
    if pInstance.avance_modulo_6 < 100:
        rem_mods.append({'value':'Módulo 6'})
    if pInstance.avance_modulo_7 < 100:
        rem_mods.append({'value':'Módulo 7'})
    return rem_mods 

def progressCalculator(project,module=1):
    answ = 0
    total = 0
    if isinstance(project, Proyectos):
        modules ={2:[['modulo_2_1',True],
                     ['modulo_2_2', True],
                     ['modulo_2_3', True],
                     ['modulo_2_4', True],
                     ['modulo_2_4_otro', ['modulo_2_4','operacion']],
                     ['modulo_2_5',False],
                     ['modulo_2_6', True],
                     ['modulo_2_7', True],
                     ['modulo_2_8', True]],
                  3:[['modulo_3_1',True],
                     ['modulo_3_1_2',['modulo_3_1','personas']],
                     ['modulo_3_1_3',['modulo_3_1','personas']],
                     ['modulo_3_1_4',['modulo_3_1','personas']],
                     ['modulo_3_1_5',['modulo_3_1','personas']],
                     ['modulo_3_1_6',['modulo_3_1','personas']],
                     ['modulo_3_2_2',['modulo_3_1','empresas']],
                     ['modulo_3_2_3',['modulo_3_1','empresas']],
                     ['modulo_3_3',True],
                     ['modulo_3_4',True],
                     ['modulo_3_5',True]],
                  4:[['modulo_4_1',True],
                     ['modulo_4_1_otro',['modulo_4_1','otro']],
                     ['modulo_4_2',True],
                     ['modulo_4_3',True]],
                  5:[['modulo_5_1',True],
                     ['modulo_5_1_otro',['modulo_5_1','otro']],
                     ['modulo_5_2',True],
                     ['modulo_5_2_otro',['modulo_5_2','si_cuales']],
                     ['modulo_5_3',True],
                     ['modulo_5_3_otro',['modulo_5_3','otro']],
                     ['modulo_5_4',True],
                     ['modulo_5_4_otro',['modulo_5_4','si_cuales']],
                     ['modulo_5_5',True]],
                  6:[['modulo_6_1',True],
                     ['modulo_6_2',True],
                     ['modulo_6_2_otro',['modulo_6_2','otro']],
                     ['modulo_6_3',True],
                     ['modulo_6_3_otro',['modulo_6_3','otro']]],
                }
        if module == 1:
            answ = 1 if project.modulo_1_1.strip() != "" else 0 
            answ += 1 if project.modulo_1_2.strip() != "" else 0
            total = 2
        elif module == 7:
            seven_2 = 0
            answ = 5 if project.modulo_7_1.strip() != "" else 0
            seven_2 += 1 if project.modulo_7_2_1.strip() != "" else 0 
            seven_2 += 1 if project.modulo_7_2_2.strip() != "" else 0 
            seven_2 += 1 if project.modulo_7_2_3.strip() != "" else 0 
            seven_2 += 1 if project.modulo_7_2_4.strip() != "" else 0 
            seven_2 += 1 if project.modulo_7_2_5.strip() != "" else 0
            if seven_2 >= 3:
                answ += 5 
            total = 10
        elif module >= 2 and module <= 6:
            m = modules.get(module)
            for mod_obj in m:
                if not isinstance(mod_obj[1],list):
                    if mod_obj[1]: #Req TRUE
                        total += 1
                        if getattr(project, mod_obj[0]) and str(getattr(project, mod_obj[0])).strip() != "":
                            answ += 1
                else:
                    parent_m = mod_obj[1]
                    var = getattr(project, parent_m[0]) #Obtain parent value
                    if parent_m[1] in var.strip(): #VALUE OF PARENT IS WHAT WE REQUESTED
                        total += 1
                        if getattr(project, mod_obj[0]) and str(getattr(project, mod_obj[0])).strip() != "":
                            answ += 1
        else:
            return 0    
        return (answ / total) * 100
    elif isinstance(project, Usuarios):
        fields_to_check = [
                            ['nombre',True],
                            ['apellido',True],
                            ['foto',False],
                            ['nacimiento',True],
                            ['maximo_grado',True],
                            ['escuela',True],
                            ['id_estado',True],
                            ['municipio',True],
                            ['sexo',True],
                            ['email',True],
                            ['email_alt',True],
                            ['tel_1_lada',True],
                            ['tel_1',True],
                            ['tel_2_lada',True],
                            ['tel_2',True],
                            ['area_experiencia',True],
                            ['como_te_enteraste',True],
                            ['socios',False], 
                          ]
        for mod_obj in fields_to_check: #WE KNOW NONE IS A LIST
            if mod_obj[1]: #Req TRUE
                total += 1
                if getattr(project, mod_obj[0]) and str(getattr(project, mod_obj[0])).strip() != "":
                    answ += 1
        return (answ / total) * 100
    else:
        return 0