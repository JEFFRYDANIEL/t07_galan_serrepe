# Sumar los x primeros numeros
import os
i=0
suma=0
x=int(os.sys.argv[1])
while(i<=x):
    print(i)
    suma += i
    i += 1
#fin_while

print("La suma de los x primeros numeros es:", suma)

print("fin del bucle")

