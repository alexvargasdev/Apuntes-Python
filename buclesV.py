for letra in "python":
    if letra =="h":
        continue
    print("Viendo la letra: "+ letra)
nombre = "pildoras informaticas"
contador= 0
for i in nombre:
    if i==" ":
        continue
    contador= contador + 1
print(contador)
#while True:
    #pass 
email=input ("Intruduce tu email: ")
for i in email:
    if i == "@":
        arroba=True
        break
else:
    arroba=False

if arroba ==True:
    print("Su correo es correcto y es "+str(email))
else:
    print("Su correo es incorrecto")
