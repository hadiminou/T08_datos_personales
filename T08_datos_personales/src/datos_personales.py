from collections import namedtuple
Persona=namedtuple('persona','dni, nombre, apellidos, edad, localidad, provincia')
def filtra_por_edad(personas:list[Persona],edad:int)->list[Persona]:
    res=list()
    for persona in personas:
        if persona.edad<edad:
            res.append(persona)
    return res        

def obtiene_dni_y_nombres(personas:list[Persona])->list:
    res=list()
    for p in personas:
        #tupla=(p.nombre,p.dni) en el lugar de dos parentesis
        res.append((p.nombre,p.dni))
    return res

'''def obtiene_numero_edades_distintas(personas:list[Persona],edad:int)->list:
    res=list()
    for edad_distinta in personas:
        res.append(edad_distinta.edad)
    res=set(res)
    a=len(res)
    return a'''

def obtiene_numero_edades_distintas(personas:list[Persona])->int:
    res=set()
    for persona in personas:
        res.add(persona.edad)
    return len(res)

def calculasumaedades(personas:list[Persona])->int:
    res=0
    for p in personas:
        res=res+p.edad #res+=p.edad
    return res

def calculapromedioedades(personas:list[Persona],prov:str="SEVILLA")->float:
    res=None
    suma=0
    contador=0
    for p in personas:
        if p.provincia==prov:
            suma+=p.edad
            contador+=1
    if contador>0:
        res=suma/contador
    return res