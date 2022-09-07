import math # importamos la clase math para hacer uso de la funcionsqrt(raiz cuadrada)

# Dada la siguiente tupla
tupla = (13, 1, 8, 3, 2, 5, 8)
# Crear una lista que solo incluya los numeros menores a 5
# e imprimir por consola [1, 3, 2]

lista = [] # definimos la lista
# filtramos los elementos menores a 5 en la tupla
for elemento in tupla:
    if elemento < 5:
        lista.append(elemento)
print(lista)

# Ejercicio matematicas
# Para sacar la raiz cuadrada de un numero positivo
numero = int(input('Digite un número positivo: '))
while numero <0:
    print('Erro -> Debería ser un número positivo')
    numero = int(input('Digite un número positivo: '))
print(f'\nSu raiz cuadrada es: {math.sqrt(numero):.2f}') # el .2f es para que nos de como resultado 2 decimales
