edad_usuario= int(input("Ingrese tu edad: "))
if 0<edad_usuario<100:
    print("Edad correcta")
else:
    print("Edad incorrecta")

salario_presidente= int(input("Intruduce el salario del presidente. "))
print("Salario presidente"+ str(salario_presidente))
salario_director= int(input("Intruduce el salario del director. "))
print("Salario presidente"+ str(salario_director))
salario_jefe_area=int(input("Intruduce el salario del jefe de area. "))
print("Salario del jefe de area "+ str(salario_jefe_area))
salario_administrativo=int(input("Intruduce el salario del administrativo. "))
print("Salario del administrativo "+str(salario_administrativo))
if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
    print("Todo funciona correctamente")
else:
    print("Algo falla en esta emoresa")