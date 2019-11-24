importar os
# Mostrar peso entre 1 y 100
# declarar variables
peso = 0.0

# pedir la variable vía argumento
peso = float (os.sys.argv [ 1 ])

# validacion
sobrepeso = (peso > 100 )

# condicion
peso_invalido = Verdadero

# si el peso es inavalido (menor a 0) pedir el peso
while (peso_invalido):
    peso = float ( input ( " ingrese el peso: " ))
    peso_invalido = (peso < 0 )
# fin_while
print ( " Fin del bucle " )

# condicion simple
if (sobrepeso ==  True ):
    imprimir ( " TIENES SOBREPESO " )
print ( " el peso es: " , peso)