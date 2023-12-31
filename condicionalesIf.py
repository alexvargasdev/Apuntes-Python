def evaluacion (nota):
    valoracion = "Aprobado"
    if nota <5:
        valoracion = "Suspenso"
    return valoracion
print("Programa de evaluación de notas de alumnos")
nota=int(input("Ingrese la nota"))
print (evaluacion(nota))