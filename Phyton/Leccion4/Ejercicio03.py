# Ejercicio 3: Insertar elementos y ordeanrlos
# Pedir números y meterlos en una lista, cuando el usuario
# introduzca un número 0, nuestro programa dejaria de insertar
# Por ultimo, mostrar los números ordenados de menor a mayor

# Funcion sort
lista = []
salir = False # asignamos una bandera
while not salir:
    numero = int(input('Digite un número: '))
    if numero == 0:
        salir = True
    else:
        lista.append(numero) # se va ingresando el numero a nuestra lista
lista.sort() # la lista esta ordenada con esta función
print(f'\nLista ordenada: \n{lista}')
