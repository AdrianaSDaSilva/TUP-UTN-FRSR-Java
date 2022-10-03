# Ejercicio 2: Funcion con *args para multiplicar
# Crear una funcon para multiplicar los valores recibidos
# de tipo numérico, utilizando argumentos variables *args
# como parametro de la funcion y regresar como resultado
# la multiplicacion de todos los valores pasados como argumentos

# definimos la funcion para multiplicar
def multiplicar_valores(*args): # el mas utilizado es *args
    resultado = 1 # le asignamos el 1 porque con 0 no se puede mulplicar
    for numero in args:
        resultado *= numero
    return resultado


# llamamos a la funcion
print(multiplicar_valores(3, 5, 15, 3)) # le pasamos argumentos
