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

# Ejercicio: es Mayor de edad

edadAdulto = 18
edadPersona= int(input('Digite su edad: '))
print(f"El residuo de la division es: {edadPersona %2}")

if edadPersona >= edadAdulto:
     print(f"Su edad es: {edadPersona} años, Ud es mayor de edad")
else:
    print(f"Su edad es: {edadPersona} años, Ud es menor de edad")