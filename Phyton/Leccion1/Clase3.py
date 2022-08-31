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