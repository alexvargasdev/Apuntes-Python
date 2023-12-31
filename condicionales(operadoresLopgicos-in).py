print("Programa de becas 2023")
distancia= int(input("Intruduce la distancia a la escuela en km. "))
hermanos= int(input("Intruduce el numero de hermanos en el centro. "))
salario_familiar= int(input("Intruduce el salario anual bruto. "))
if distancia>40 or hermanos>2 or salario_familiar<= 20000:
    print("Tienes derecho a beca")
else:
    print("No tienes derecho a beca")

print ("Asignaturas ptativa año 2023")
print("Asignaturas optativas: Informatica gráfica - Pruebas de software - Usabilidad y accesibilidad")
opcion= input("Escribe la asignatura escogida: ")
asignatura=opcion.lower() #lower convierte a minuscula los caracteres de mayuscula
if asignatura in ("informatica gráfica", "pruebas de software", "usabilidad y accesibilidad"):
    print("Asignatura eligida "+ asignatura)
else:
    print("La asignatura escogida no esta contemplda") 