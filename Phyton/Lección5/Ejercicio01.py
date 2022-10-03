# Ejercicio 01: Crear una función para sumar los valores recibidos de tipo
# numéricos, utilizando argumentos variables *args como parametro de la
# funcion y agregar como resultado la suma de todos los valores pasados
# como argumentos
# Definimos una Funcion
def sumar_valor(*args):  # recibimos una cantidad de parametros indefinidos
  #  pass  # Se usa pass para que no tire error al no agregar detalle a la funcion
    resultado = 0
  # Iteramos cada elemento
    for valor in args:
        resultado += valor
    return resultado


# Llamamos a la funcion
print(sumar_valor(3, 5, 9))
