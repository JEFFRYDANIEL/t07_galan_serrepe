importar os
# Mostrar operadores de celular de celular (movistar / claro / entel):
# declarar variables
operador = " "

# pedir la variable vía argumento
operador = os.sys.argv [ 1 ]

# validacion
gratis = (operador == " entel " )

# condicion
operador_invalido = True

# si el peso es inavalido (menor a 0) pedir el peso
while (operador_invalido):
    operador = input ( " ingrese el operador que utliza (movistar / claro / entel): " )
    operador_invalido = (operador ! =  " movitar "  y operador ! =  " claro "  y operador ! =  " entel " )
# fin_while
print ( " Fin del bucle " )

# condicion simple
if (gratis ==  verdadero ):
    imprimir ( " GANASTE MEGAS ILIMITADOS " )
print ( " el operador que usted utiliza es: " , operador)