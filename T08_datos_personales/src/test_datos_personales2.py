from datos_personales import *
def carga_lista()->list[Persona]:
    personas=[Persona('12345678A','JUAN','AFAN POSTIGO',22,'SEVILLA','SEVILLA'),
    Persona('12345678B','NICOLAS','AGUILAR SAUCEDO',20,'DOS HERMANAS','SEVILLA'),
    Persona('12345678C','LUCAS','ACEJO GARCÍA',20,'UTRERA','SEVILLA'),
    Persona('12345678D','CLAUDIA','ÁLVAREZ GARCÍA',21,'VISO DEL ALCOR','SEVILLA'),
    Persona('12345678E','PAULA','ALBENDÍN CAMINO',19,'TOMARES','SEVILLA'),
    Persona('12345678F','ANA','LOBATO ÁLVAREZ',18,'PUNTA UMBRÍA','HUELVA'),
    Persona('12345678G','ANTONIO','DÍAZ NARANJO',18,'CHIPIONA','CADIZ'),
    Persona('12345678H','SOFÍA','GUERRERO CANTARERO',20,'CHIPIONA','CADIZ')]
    return personas

def test_filtra_por_edad(personas:list[Persona]):
    edad=21
    print ("los menores de",edad,"son:")
    for p in filtra_por_edad(personas,edad):
        print (p)

def test_obtiene_dni_y_nombres(personas:list[Persona]):
    print("\nla lista con el nombre y el dni es:")
    for l in obtiene_dni_y_nombres(personas):
        print (l)

def test_obtiene_numero_edades_distintas(personas:list[Persona]):
#    print("edades distintas son: ", obtiene_numero_edades_distintas(personas,edad))
    print("\nNumero de edades distintas:",
          obtiene_numero_edades_distintas(personas))

def test_calculasumaedades(personas:list[Persona]):
    print("\nla suma de las edades es:",
          calculasumaedades(personas))

def test_calculapromedioedades(personas:list[Persona], prov:str="SEVILLA"):
        print("\npromedio de edades es: ", calculapromedioedades(personas, 'CADIZ'))
        print("\npromedio de edades es: ", calculapromedioedades(personas)) #este nos da valor de sevilla porque es el valor por defecto
        print("\npromedio de edades es: ", calculapromedioedades(personas, 'JAEN'))

if __name__=="__main__":
    lista_personas=carga_lista()
    #test_filtra_por_edad(lista_personas)
    #test_obtiene_dni_y_nombres(lista_personas)
    #test_obtiene_numero_edades_distintas(lista_personas)
    #test_calculasumaedades(lista_personas)
    test_calculapromedioedades(lista_personas)