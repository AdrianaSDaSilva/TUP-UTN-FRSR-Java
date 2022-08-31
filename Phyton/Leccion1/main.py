'''
# CLASE 2 # VARIABLES ###########################################################################################

miVariable = 3
print(miVariable)
miVariable = "Hola a todos los alumnos de la tecnicatura"
print(miVariable)
miVariable = 3.5
print(miVariable)
x = 10  # x se llaman literales #
y = 2  # y literales #
z = x + y  # z literales #
print(id(x))
# Las literales se escriben x992, variabley x736, variablez x256
print(id(y))
print(id(z))

# CLASE3 # TIPOS DE DATOS ######################################################################################

a = "Hola Alumnos"  # tipo de dato strem" es cuando hay palabras#
print(type(a))  ## aprendimos una nueva funcion = Type (), poner entre parentesis la variable, en este caso es la (a)#
b = 10.78  # tipo de dato "float" cuando decimales#
print(type(b))
c = 20
print(type(c))  # tipo de dato "int" caundo hay numeros enteros#
d = True  # tipo de dato "clase literal booleana" OJO va la T mayuscula #
print(type(d))
e = False  # tipo de dato "clase literal booleana"
print(type(e))

## Repaso ##

x = 10
print(x)
print(type(x))
x = 14.5
print(x)
print(type(x))
x = "Hola alumnos"
print(x)
print(type(x))
x = True
print(x)
print(type(x))
x = False
print(x)
print(type(x))

## MANEJO DE CADENAS ## "STRING"

# 1 CONCATENACIÓN #
miGrupoFavorito = "Soda Stereo"
print("Mi crupo favorito es: " + miGrupoFavorito)
# El Signo "+" sirve para concatenar y no para sumar. #

# 2 CONCATENACION DENTRO DE LA ASIGANACIÓN#
miGrupoFavorito = "Soda Stereo" + " " + "y " + "Redonditos de Ricota"  # Agrego comillas y operador + para hacer espacio.
print("Mi crupo favorito es: " + miGrupoFavorito)

# 3 CARACTERISTICAS # "otra forma de contatenar"
miGrupoFavorito = "Soda Stereo: "
caracteristicas = " Los Redonditos de Ricota"
print("Mi crupo favorito es: " + miGrupoFavorito + " " + caracteristicas)

# 4 FORMAS DE IMPRMIR CADENAS # "Con comas"
miGrupoFavorito = "Soda Stereo: "
caracteristicas = " Los Redonditos de Ricota"
print("Mi crupo favorito es: ", miGrupoFavorito, caracteristicas)

# EJEMPLO CON OTRAS VARIABLES , tipos cadenas #
# A:
numero1 = "7"
numero2 = "8"
print(numero1 + numero2)  # no suma, solo los junta.
# B: ahora lo vamos a sumar
numero1 = "7"
numero2 = "8"
print(int(numero1) + int(numero2))  # ahora suma.
# Se puede sumar en cadena siempre que sean dos numeros.

## TIPOS BOOLEANOS (bool)
# permite saber si un dato es verdadero o falso.

# A:
miBooleano = 3 > 2
print(miBooleano)

if miBooleano:
    print("El resultado es Verdadero")
else:
    print("El resultado es Falso")

## PROCESAR LOS DATOS DEL USUARIO ##
# Función INPUT

resultado = input("Digite un número: ")  # funcion que regresa un dato tipo string#
print(resultado)

## CONVERSIÓN DE LA ENTRADA DE DATOS
codigo1 = int(input("Escribe el primer número: "))
codigo2 = int(input("Escribe el segundo número: "))
resultados = codigo1 + codigo2
print("El resultado de la suma es: ", resultados)

## HACER EJERCICIOS " COMO ESTA TU DÍA" Y "AUTOR DE LIBROS"
# VER ULTIMOS MINUTOS DE LA CLASE 3.

# Ejercicio nro 1

miDia = input("Como estuvo tu día hoy? : ")
print(miDia)

# Ejercicio nro 2
elTitulo = input("Escriva el título del libro: ")
print(elTitulo)
miAutor = input("Escriva el autor: ")
print(miAutor)
print(elTitulo,  "fue escrito por  ", miAutor)
'''

""""
########################################################
#CLASE 4
#OPERADORES DE PYTHON PARTE 1

operandoA = 8
operandoB = 5

suma: int = operandoA + operandoB
#print ("Resultado de la suma: ", suma)
print(f'EL reaultado de la suma es: {suma}')
# Interpolación, incluir la variable dentro de la misma cadena, no hace falta concatenar

resta = operandoA - operandoB
print(f"El resultado de la resta es: {resta}")
#  la f => formato.

multiplicacion = operandoA * operandoB
print(f"El resultado de la multiplicacion es: {multiplicacion}")

division = operandoA / operandoB
print(f"El resultado de la division es: {division}")
# haciendo la misma division pero que nos devuelva un numero entero
division = operandoA // operandoB
print(f"El resultado de la division (int) es: {division}")

modulo = operandoA % operandoB
print(f" El reaultado de la deivision o residuo (modulo) es: {modulo}") # se recibe el residuo de la division.

exponente = operandoA ** operandoB
print(f"El resultado del exponente es {exponente}")
############################################################### doc string: es la triple comilla
"""
# RECTANGULO
"""
alto = int(input('Proporciona el alto del rectangulo'))
ancho = int(input('Proporciona el ancho del rectangulo'))
area = alto * ancho
perimetro = (alto + ancho) * 2
print('Area: ', area)
print('Perímetro: ', perimetro)
"""
# OPERADORES DE REASIGNACIÓN:
# operadores aritmétcios con reasignación
"""
miVariable3 = 10
print(miVariable3)

miVariable3 = miVariable3 + 1
print(miVariable3)

miVariable3 += 1
print(miVariable3)

# miVariable3 = miVariable3 - 2
miVariable3 -= 2
print(miVariable3)

# miVariable3 = miVariable3 * 3
miVariable3 *= 3
print(miVariable3)

# miVariable3 = miVariable3 / 2
miVariable3 /= 2
print(miVariable3)

#Operadores de comparación
d = 4
b = 5
resultado = d == b  # Comparamos sin son iguales
print(resultado)

#Operador  Diferente
resultado = d != b
print(resultado)

# Operador mayor que
resultado = d > b
print(resultado)

#Operador Menor que
resultado = d < b
print(resultado)

#Operador Menor o igual que
resultado = d <= b
print(resultado)

#Operador Mayor o igual que
resultado = d >= b
print(resultado)

#Ejercicio: Número par o impar

a = int(input('Digite un número: '))
print(f"El residuo de la division es: {a % 2}")
if a % 2 == 0:
    print(f"El número que digitó es: {a} Par")
else:
    print(f"El número que digitó es: {a} Impar")
"""
'''# Ejercicio: es Mayor de edad

edadAdulto = 18
edadPersona= int(input('Digite su edad: '))
print(f"El residuo de la division es: {edadPersona %2}")

if edadPersona >= edadAdulto:
     print(f"Su edad es: {edadPersona} años, Ud es mayor de edad")
else:
    print(f"Su edad es: {edadPersona} años, Ud es menor de edad")
'''
####################################################################################################
##CLASE 5##
#OPERADORES DE PYTHON PARTE 2#

 #OPERADORES LÓGICOS#
#Operador and
'''a = True
b = True
resultado = a and b
print(resultado)

#Operador or
resultado = a or b
print(resultado)

#Operador not
resultado = not a
print(resultado) ## operador unario'''

#Ejercicio: Valor dentro de un rango
'''valor = int(input("Digite un número: "))
ValorMinimo = 0
ValorMaximo = 5
dentroRoango = (valor >= ValorMinimo and valor <= ValorMaximo)
if dentroRoango:
    print(f'El valor {valor} está dentro del rango')
else:
    print(f'El valor {valor} no está dentro del rango')'''

#################################################
#Ejercicio con operador or
'''vacaciones = False
diaDescanso = False
if vacaciones or diaDescanso:
    print ('Puede asistir al juego')
else:
    print('tiene trabajo que hacer')'''
##################################################
#Ejercicio: Rango entre 20 y 30 años.

'''edad = int(input("Digite su edad:"))
#veinte = edad >= 20 and edad < 30
#print(veinte)
#treinta = edad >= 30 and edad < 40
#print(treinta)'''
'''
# SINTAXI SIMPLIFICADA DEL OPERADOR AND
#if veinte or treinta
if (20 <= edad < 30) or (30 <= edad < 40 ):
    print('Estas dentro del rango de los (20\'0) a (30\' 0) años ')
#    if veinte:
#        print('Estas dentro del rango de los rangos (20\'0) años')
#    elif treinta:
#        print('Estas dentro del rango de los rangos (30\'0) años')
#    else:
#        print('No estas dentro del rango')
else:
    print('No estas dentro del rango de los (20\'0) a (30\' 0) años ')'''

##########################################################################

#Ejercicio: el mayor de dos números

'''numero1 = int(input('Digite el valor para el numero1: '))
numero2 = int(input('Digite el valor para el numero2: '))

if numero1 > numero2:
    print(('El número 1 es mayor'))
else:
    print(('El número 2 es mayor'))'''
###########################################################################
#Ejercicio => Tienda de libros
print('Digite los siguientes datos del libro: ')
nombre = input('Digite el nombre del libro: ')
id = int(input('Digite el ID del libro: '))
precio = float(input('Digite el precio del libro: '))
envioGratuito = input('Indicar si el libro es gratuito (True/Flase): ')

if envioGratuito == 'True':
   envioGratuito = True
elif envioGratuito =='False':
     envioGratuito = False
else:
    emvioGratuito = 'El valor es incorrecto, debe escribir True o False'
print(f'''
        Nombre: {nombre}
        Id: {id}
        Precio: {precio}
        Envio Gratuito?: {envioGratuito}
''')




















