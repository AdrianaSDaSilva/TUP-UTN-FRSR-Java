# Ejercicio 1: eliminar duplicados de una lista
# Escriba un programa donde tenga una lista y que a continuacion
# elimine los elementos repetidos, por ultimo mostrar la lista

# creamos la lista
lista = [1, 2, 3, "Ariel", 7, 8, 9, 5, 5, 7, 8, 1, 2, "Alberto"]
# pasamos la lista a conjunto y como alli no puede haber elementos repetidos se eliminan
# conjunto = set(lista)
# print(conjunto)
# lista = list(lista)
lista = list(set(lista))
print(lista)

