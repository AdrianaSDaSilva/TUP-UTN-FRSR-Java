# Lista = nombres, números, cualquier tipo de dato
# A cada elemento de la lista se le agrega un indice, comenzando por el 0

# Creamos una lista, usamos corchetes
nombres = ["Naty","Osvaldo","Lily","Ariel"]
print(nombres)

# Como accedemos a la lista de manera individual
print(nombres[0])
print(nombres[1])

# Como acceder de manera inversa
print(nombres[3])

# Como ver el ultimo elemento sin saber el numero de indice
print(nombres[-1])
# penultimo
print(nombres[-2])

# Como recuperar un rango de la lista
print(nombres[0:2]) # va a recorrer el 0 y el 1, el 2 no lo recorre. Muestra las 2 primeras posiciones del indice

# Ir al inicio de la lista al indice (sin incluirlo)
print(nombres[ :3]) # Muestra desde el indice 0 en adelante

# ir desde el indice hasta el final
print(nombres[1: ])

# Modificar un valor
nombres[2] = "Liliana"
nombres[0] = "Natalia"
print(nombres)

# Iteramos nuestra lista
for nombre in nombres: #nombre es singular, la lista es plural
    print(nombre) # nos muestra cada elemento con salto de linea
else:
    print("Se acabaron los elementos de la lista")

    # Para ver cuantos elementos tenemos en la lista
print(len(nombres)) # Le pasamos un parametro

# Agregamos un elemento a la lista, se agrega al final
nombres.append("Marcelo")
print(nombres)

# Insertar un elemento en un indice especifico
nombres.insert(1,"Alberto")
print(nombres)
nombres.insert(3, "Debora")
print(nombres)

# Eliminar un elemento de la lista
nombres.remove("Alberto")
print(nombres)

# Eliminar el ultimo elemento de la lista
nombres.pop()
print(nombres)

# Eliminar un indice especifico
del nombres[2] # del es eliminar
print(nombres)

# Eliminar, borrar o limpiar todos los elementos
nombres.clear()
print(nombres)

# Eliminar la lista
del nombres
#print(nombres)

# Definicion de Tupla
cocina =("cuchara", "cuchillo", "tenedor") #va entre parentesis, noentre corchetes
print(cocina)

# para saber la cantidad de elementos que tiene la tupla
print(len(cocina))

# Como acceder a un elemento
# utilizamos corchetes en este caso, no parentesis
print(cocina[0])

# mostrar de manera inversa la tupla cuando no sabemos cuantos elementos tiene
print(cocina[-1])

# como acceder a un rango
print(cocina[0:1]) #el 1 no lo imprime, muestra un numero menos del 1

# ejemplo
verduras = ("papa",) # va con coma xq sino es una cadena

# Recorremos los elementos de una tupla
for cocinar in cocina:
    # print(cocinar) # Print esta usando \n nos muestra cada elemento con salto de linea
    print(cocinar, end= " ") # usamos end= para elmininar los saltos de linea

# la unica manera de modificar una tupla es hacer una conversion a lista y luesgo volvemos a tupla
cocinaLista = list(cocina) # convierte tupla en lista
cocinaLista[0] = "Plato"
cocina = tuple(cocinaLista) # conversion de lista a tupla
print("\n", cocina) # para que haga el salto de linea con el for

# eliminar la tupla
# del cocina
# print(cocina)







