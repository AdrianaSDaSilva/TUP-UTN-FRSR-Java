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
nombres.append("Marcelo") # String
nombres.append([1, 2, 3]) # Lista dentro de la lista
nombres.append(True) # Booleano
nombres.append(10.45) # Float
nombres.append([4, 5]) # Lista
nombres.append(7) # entero
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

# Tipo Set, imprime de forma aleatoria
planetas = {"Marte", "Jupiter", "Venus"}
print(planetas)
print(len(planetas)) # nos muestra la cantidad o largo del set

# Revisar si un elemento esta en el set
print("Marte" in planetas) # booleano, nos dice si el elemento esta en el set
print("Jupiter" not in planetas) # nos dice si no esta en el set

# Agregar elemento
planetas.add("Tierra") # add es una funcion para agregar
print(planetas)
# En el tipo set no se pueden agregar elementos duplicados, si repito no pasa nada
# La coleccion del tipo set nos puede servir para evitar elementos duplicados

# Eliminar elementos, puede arrojar un error si el elemento no existe
# planetas.remove("Saturno")
planetas.remove("Jupiter")
print(planetas)
planetas.discard("Tierra") # Si no existe el elemento o esta mal escrito no pasa nada, no tira error
print(planetas)

# Limpiar set
planetas.clear()
print(planetas)

# Eliminar set
# del planetas
print(planetas)

# Diccionario en Phyton
# Son colecciones
# "Maradona" es la llave. : 10 es el valor
# Un diccionario esta compuesto por dos elementos
# una llave y un valor asociado
# dict(key,value)
diccionario = {
    "IDE":"Integrated Development Environment",
    "POO": "Programación Orientada a Objetos",
    "SABD": "Sistema de Administración de Base de Datos"
}
#print(diccionario)

 # Para conocer el largo de los elementos o la cantidad de elementos
print(len(diccionario))
print(diccionario)

# acceder a un diccionario con la llave (key)
print(diccionario['IDE'])
# o tambien puede ser
print(diccionario.get('POO'))
# o tambien
print(diccionario.get('SABD'))

# Modificar elementos del diccionario
diccionario['IDE'] = 'Entorno de Desarrollo Integrado'
print(diccionario)

# como recorrer los elementos
for termino in diccionario: # muestra las llaves
    print(termino)

# para recorrer los valores del diccionario
for termino, valor in diccionario.items():
    print(termino, valor)

# otras maneras de acceder a un diccionario
for termino in diccionario.keys():
    print(termino) # muestra solo las llaves

for valor in diccionario.values():
    print(valor) # nos muestra solo los valores

# Comprobar la existencia de un elemento
print('IDE' in diccionario) # booleano
print('IDEA' not in diccionario) # si no esta

# Agregar un elemento
diccionario['PK'] = 'Primary Key'
print(diccionario)

# Eliminar un elemento
diccionario.pop('SABD')
print(diccionario)

# Vaciar un diccionario
diccionario.clear()
print(diccionario)

# Borrar un diccionario
del diccionario # El diccionario se borró

# Listas y Tuplas pertenecen a colecciones en Phyton
# se conocen en otros lenguajes como arreglos o vectores

# Concatenamos Listas
lista1 = [1, 2, 3, 1]
lista2 = [4, 5, 6, 1]
lista3 = lista1 + lista2
print(lista3)

# Para agregar varios elementos a una lista
lista3.extend([7, 8, 9])
print(lista3)

# Funcion para saber en que indice esta un elemento
print(lista3.index(5))

# Para ver cuantos valores repetidos hay en una lista
print(lista3.count(1))

# para poner la lista al reves
lista3.reverse()
print(lista3)

# Multiplicar la lista repitiendo sus elementos
lista = [1, 2, 3] * 2
print(lista)

# Métodos de ordenamientos por defecto de manero ascendente
lista3.sort()
print(lista3)
# de manera descendente
lista3.sort(reverse = True)
print(lista3)

# Repaso Tuplas
# Las tuplas son lista inmutables, no se pueden modificar
# Pueden tambien tener valores diferentes, cadenas, float, bolleanos
tupla = (4, 'Hola', 6.78, [1, 2, 78, 4], 4, 'Hola')
print(tupla)

print(4 in tupla) # preguntamos si esta el elemento 4
print(5 not in tupla) # preguntamos si no esta
# Lo que podemos hacer dentro de tuplas son: index, count, len
# En tuplas se puede convertir de tupla a lista y de lista a tupla

# Repaso de set o conjunto
# para definir un conjunto
# Conjunto: elementos desordenados
conjunto = set() # Lo inicializamos
conjunto1 = {'bye'} # lo inicializamos, tiene que tener un elemento al menos si o si para que luego al agregar elementos no tire error
conjunto.add(7) # añadir datos
conjunto.add('Hola') # añadimos otro elemento
print(conjunto)
conjunto1.add('Hola')
print(conjunto1)

# Preguntamos si el número 3 está en el conjunto1
print(3 not in conjunto1) # nos devuelve un valor booleano

# Como hacer la igualdad de los conjuntos
print(conjunto1 == conjunto) # nos devuelve un valor bolleano

# Operaciones en conjuntos
# Union de conjuntos
conjunto3 = conjunto1 | conjunto # La linea une los conjuntos
print(conjunto3)

# Intersección: es el elemento que tienen en comun
conjunto3 = conjunto1 & conjunto # que elemento tienen en comun?
print(conjunto3) # imprime el elemento que tienen en comun

conjunto3 = conjunto1 - conjunto # visualizar los elementos del conjunto 1 y no del otro
print(conjunto3)
conjunto3 = conjunto - conjunto1 # que elemento esta en el dos pero no en el 1
print(conjunto3)

# que elemento no compartem
conjunto3 = conjunto1 ^ conjunto
print(conjunto3)

# como determinar si un conjunto es un subconjunto de otro
conjunto3 = conjunto1 | conjunto
print(conjunto1.issubset(conjunto3)) # no da un valor booleano
print(conjunto.issubset(conjunto3))
print(conjunto3.issubset(conjunto1))

# como saber si ambos conjuntos son inconexos, no comparten ningun elemento
print(conjunto3.issuperset(conjunto1))
print(conjunto3.issuperset(conjunto))
print(conjunto.issuperset(conjunto3))

# como saber si no compartes ningun elemento, disconexos
print(conjunto1.isdisjoint(conjunto))

# convertir un conjunto en totalmente inmutable
conjunto1 = frozenset
# ahora no se puede modificar nda, ni agregar, ni eliminar ningun elemento del conjunto

# Repaso Diccionarios
diccionarioNuevo = {'Azul' : 'Blue',
                    'Rojo':'Red',
                    'Verde':'Green',
                    'Amarillo' : 'Yellow'
                    }
# Como eliminar un elemento
del(diccionarioNuevo['Azul'])
print(diccionarioNuevo)
# Los diccionarios pueden almacenar diferentes tipos de datos
diccionario2 = {'Ariel': {'edad' : 40, 'Altura': 1.83},'Osvaldo':[45, 1.85],'Natalia': [35, 1.65]}
print(diccionario2)

seleccionArgentina = {
    10: {'Nombre': 'Lionel Messi', 'Edad': 35, 'Altura': 1.70, 'Precio': '50 millones', 'Posicion': 'extremo'},
    11:{'Nombre': 'Ángel Di María', 'Edad':34, 'Altura':1.80, 'Precio':'12 millones','Posición':'Extremos derecho'},
    9:{'Nombre':'Julián Álvarez', 'Edad':22, 'Altura':1.70, 'Precio': '23 millones','Posición':'Delantero central'},
    21:{'Nombre':'Paulo Dybala','Edad':28,'Altura':1.77, 'Precio':'35 millones','Posición':'Mediapunta'},
    22:{'Nombre':'Lautaro Martínez','Edad':25,'Altura':1.74,'Precio':'75 millones','Posición':'Deltantero centro'},
    23:{'Nomnbre': 'Emiliano Martínez','Edad':30,'Altura':1.95,'Precio':'28 millones','Posición':'Portero'},
    12:{'Nombre':'Gerónimo Rulli','Edad':30,'Altura':1.89,'Precio':'6 millones','Posición':'Portero'},
    1:{'Nombre':'Franco Armani','Edad':35,'Altura':1.89,'Precio':'3,50 millones','Posición':'Portero'},
    13:{'Nombre':'Cristian Romero','Edad':24,'Altura':1.85,'Precio':'48 millones','Posición':'Defensa Central'}
     }
print(seleccionArgentina[10]) # Nos muestra el 10
print(seleccionArgentina.values()) # para ver solo los valores del diccionario

# recorremos nuestro arreglo con un ciclo for
for llave in seleccionArgentina:
    print(llave)

for valor in seleccionArgentina.values():
    print(valor)

# Para ver todo
for llave, valor in seleccionArgentina.items():
    print(llave,valor)

# Ver el tamaño, la cantidad de elementos que tiene nuestro diccionario
print('Tenemos cargados en el diccionario la cantidad de jugadores: ')
print(len(seleccionArgentina))

# METODO CON LISTAS LLAMADO PILAS
pila = [1,2,3]
# en una pila no podemos sacar el primer elemento puesto, siempre trabajamos con el ultimo elemento agregado
# agregar elementos a la pila por el final
# el primer elemento queda abajo

# Agregamos
pila.append(4)
pila.append(5)
print(pila)

# Sacando elementos por el final
pila.pop() # saca y retorna, podemos capturar el elemento que se elimina
print(pila)

# como retornar el elemento borrado
elementoBorrado = pila.pop()
print(f'Sacamos el elemento: {elementoBorrado}')
print(f'La pila ahora quedó asi: {pila}')

# METODO CON LISTAS LLAMADO COLA
# Estructuras de datos de tipo FIFO
# First input(primero en entrar)/first output(primero en salir)
# esto quiere decir que el primero que llega es el primero que atienden por ejemplo y sale
# el que llega se agrega al final
cola = ['Ariel','Osvaldo','Liliana','Pilar']

# Agregamos elementos a la cola
cola.append('Natalia')
cola.append('José')
print(cola)

# Sacamos elementos de la cola
seRetira = cola.pop(0)
print(f'Atendido: {seRetira}')
print(cola)
seRetira = cola.pop(0)
print(f'Atendido: {seRetira}')
print(cola)












