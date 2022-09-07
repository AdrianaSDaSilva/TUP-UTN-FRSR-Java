# Ejercicio 2: Operaciones de conjuntos con listas
# Escriba un programa que tenga 2 listas y que a continuación
# cree las siguientes listas (en las que no deben haber repeticiones)
# 1 lista de palabras que aparecen en las listas
# 2 lista de palabaras que aparecen en la primera lista, pero no en la segunda
# 3 lista de palabras que aparecen en la segunda lista, pero no en la primera
# 4 lista de palabras que aparecen en ambas listas

# creamos una lista Esto lo hice yo
colores = ["negro", "azul", "rosa", "rojo", "blanco", "gris", "negro", "negro,"]
coloresPrimarios = ["rojo", "amarillo", "azul","rojo"]
coloresTotal = colores + coloresPrimarios # concatenamos
print(coloresTotal) # punto 1
print(colores) # punto 2
print(coloresPrimarios) # punto 3
conjunto = set(colores) # convierto en conjunto la primer lista
conjunto1 = set(coloresPrimarios) # convierto en conjunto la segunda lista
conjunto2 = conjunto & conjunto1 # comparo para mostrar los elementos que hay en ambas
lista = list(conjunto2) # vuelvo a lista el conjunto
print(conjunto2) # muestro la lista

# RESOLUCION PROFE
lista1 = [1, 2, 3, 4, 5, 4, 3, 2, 1, 5, 5]
lista2 = [4, 5, 6, 7, 8, 4, 5, 6, 7, 7, 8]
# eliminamos los elementos repetidos en ambas listas con conjuntos
conjunto1 = set(lista1)
conjunto2 = set(lista2)

union = list(conjunto1 | conjunto2) # unimos los donjuntos
solo1 = list(conjunto1 - conjunto2) #solo muestra el conjunto1
solo2 = list(conjunto2 - conjunto1) # solo muestra el conjunto2
interseccion = list(conjunto1 & conjunto2)
print(f"lista de palabras que aparecen en las listas: {union}")
print(f"Lista de palabras que aparecen en la primera lista: {solo1}")
print(f"Lista de palabras que aparecen en la segunda lista: {solo2}")
print(f"Lista de palabras que coinciden en ambas listas: {interseccion}")
