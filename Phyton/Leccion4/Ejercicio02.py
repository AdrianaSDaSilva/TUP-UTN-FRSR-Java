# Ejercicio 2: Modificar los elementos de una lista
# Llenar una lista con los números del 1 al 10, luego modificar los
# elementos de la lista muntiplicandolos por un valor ingresado por el usuario



# RESOLUCION DEL PROFE
lista = list(range(1,11))
print('Lista original')
for i in lista:
    print(i, end='-')
valor = int(input('\nDigite un valor a multiplicar: '))
# Multiplicamos todos los elemtnos de la lista
for indice, i in enumerate(lista): # enumerate recorre la lista y puede ingresar
    lista[indice] *= valor

print(f'Lista final con los elementos multiplicados por {valor}')
for i in lista:
    print(i,end='-')

