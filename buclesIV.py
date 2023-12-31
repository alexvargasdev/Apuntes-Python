import math
i = 1
while i <= 10:
    print("ejecucución "+ str(i))
    i = i + 1
print("Termino la ejecución ")
edad = int(input("Intruduce  tu edad por favor: "))
while edad <0 or edad > 100:
    print ("Has intruducido una edad incorrecta. Vuelve a intentarlo")
    edad= int(input("Intruduce tu edad por favor: "))
print("Gracias por colaborar. Puedes pasar")
print("Edad del aspirante es "+str(edad))

print("Programa de cálculo de Raíz cuadrada")
numero= int(input("Intruduce un numero por favor: "))
intentos=0
while numero <0:
    print ("No se puede hallar la raíz cuadrada de un número negativo")
    if intentos ==2:
        print("Has consumido demasiados intentos. EL progrma ha finalizado")
        break
    numero = int(input("Intruduce un número por favor: "))
    if numero<0:
        intentos= intentos + 1
if intentos<2:
    solucion=math.sqrt(numero)
    #solucion=int(solucion)
    print ("La raiz cuadrda de "+ str(numero)+ " es "+ str( solucion))