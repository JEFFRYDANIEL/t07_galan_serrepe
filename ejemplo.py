edad=int(input("Ingrese edad:"))
print(edad)

edad_invalida=(edad < 0 or edad >100)

#Validar que la edad este entre 0 y 100
while (edad_invalida == True ):
   edad=int(input("Ingrese edad:"))
   edad_invalida=(edad<0 or edad>100)

#fin while

print("fin del bucle")