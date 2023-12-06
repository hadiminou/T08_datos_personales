from datos_personales import *
personas=[Persona('12345678A','JUAN','AFAN POSTIGO',22,'SEVILLA','SEVILLA'),
Persona('12345678B','NICOLAS','AGUILAR SAUCEDO',20,'DOS HERMANAS','SEVILLA'),
Persona('12345678C','LUCAS','ACEJO GARCÍA',20,'UTRERA','SEVILLA'),
Persona('12345678D','CLAUDIA','ÁLVAREZ GARCÍA',21,'VISO DEL ALCOR','SEVILLA'),
Persona('12345678E','PAULA','ALBENDÍN CAMINO',19,'TOMARES','SEVILLA'),
Persona('12345678F','ANA','LOBATO ÁLVAREZ',18,'PUNTA UMBRÍA','HUELVA'),
Persona('12345678G','ANTONIO','DÍAZ NARANJO',18,'CHIPIONA','CADIZ'),
Persona('12345678H','SOFÍA','GUERRERO CANTARERO',20,'CHIPIONA','CADIZ')]

edad=21
print ("los menores de",edad,"son:")
for p in filtra_por_edad(personas,edad):
    print (p)

print("\nla lista con el nombre y el dni es:")
for l in obtiene_dni_y_nombres(personas):
    print (l)

print("edades distintas son: ", obtiene_numero_edades_distintas(personas))
#print("\nNumero de edades distintas:"
# ,obtiene_numero_edades_distintas(personas) )


