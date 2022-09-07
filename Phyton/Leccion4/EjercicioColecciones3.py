# Ejercicio 3: Agregar personajes a una lista
# Escriba un programa que cree una lista con los siguientes personajes del Señor de los Anillos

# Nombre: Aragon
# Clase: Guerrero
# Raza: Dúnadan del norte

# Nombre: Gandalf
# Clase: Mago
# Raza: Istar

# Nombre: Legolas
# Clase: Arquero
# Raza: Elfo Sindar


# RESOLUCION DEL PROFE
personajes = [] #Creamos una lista vacia
# creamos diccionarios
P = {'Nombre': 'Aragon','Clase':'Guerrero','Raza':'Dunadan del norte'}
personajes.append(P) # agregamos a la lista un personaje
P = {'Nombre': 'Gandalf','Clase':'Mago','Raza':'Istar'}
personajes.append(P)
P = {'Nombre': 'Legolas','Clase':'Arquero','Raza':'Elfo Sindar'}
personajes.append(P)
print(personajes)