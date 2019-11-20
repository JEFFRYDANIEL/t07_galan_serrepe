import os
#declarar variables
estacion=""

#pedir la variable via argumento
estacion=os.sys.argv[1]
estacion_invalida=True

#si la estacion es invalida volver a pedir la estacion
while(estacion_invalida):
    estacion=input("Ingrese la estacion verano/invierno/otoño/primavera):"
    estacion_invalida=(estacion != "verano" and estacion != "invierno" and
                       estacion !="otoño" and estacion !="primavera")
#fin while
print("fin del bucle")
print("la estacion es:",estacion)