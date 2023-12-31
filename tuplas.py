mitupla = ("juan",13,1,1995)
print(mitupla)
print(mitupla[1])
#tupla a lista
lista = list(mitupla)
print(lista)
#lista a tupla
milista=["alex",89,67]
mitupla1=tuple(milista)
print(milista)
print(mitupla1)
#para buscar un elemento en la tupla "in"
print("alex" in mitupla1)
#numero de veces que se encuentra un elemento en una tupla "count"
print(mitupla.count(13))
#longitud de  un tupla "lent"
print(len(mitupla))
#tupla unitaria 
mitupla2 =("pedro",)
print(len(mitupla2))
#tupla sin parentisis (empaquetado de tuplas)
mitupla3 = "juan",13,1,2015
print(mitupla3)
#desespaquetado de tuplas 
nombre, dia, mes, año = mitupla3
print(nombre)
print(dia)
print(mes)
print(año)

