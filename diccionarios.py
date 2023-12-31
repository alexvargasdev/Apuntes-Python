midiccionario ={'nombre':'Alex', 'apellidos':'Vargas', 'direccion':'26 de enero Ayacucho'}
print(midiccionario['nombre'])
#para acceder a todo el diccionario
print(midiccionario)

#para agregar un elemento a un diccionario 
midiccionario['nombre'] = 'Juan'
print(midiccionario)

#corregir una clave de un elemento del diccionario 
midiccionario['apellidos'] ='Tinco'
print(midiccionario)

#eliminar un elemento de un diccionario
del   midiccionario['apellidos']
print(midiccionario)

#diccionario mixto
midiccionrio1={'edad':24 , 'fecha':15}
print(midiccionrio1)

#diccionrio y tuplas como valores
mitupla=('España','Inglaterra','Fancia')
midiccionario2={mitupla[0]:'Madrid',mitupla[1]:'Londres',mitupla[2]:'Paris'}
print(midiccionario2)

#diccionario y tuplas como claves
midiccionario3={23:'Jordan','nombre':'Michael','Equipo':'Chicago','anillos':(1991,1992,1993,1996,1997,1998)}

#para imprimir el valor
print(midiccionario3.valuesJ())

#para imprimir el valor de una llave o clave
print(midiccionario3.keys())

#para imprimir el tamaño de un diccionario
print(len(midiccionario3))