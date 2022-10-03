# una funcion necesita ser llamada para que se ejecute el codigo que esta dentro de ese bloque
# definimos una función con una palabra reservada (def)
def mi_funcion():
    print("Saludos a todos")
    print()
    print()
    # respetando la identacion estamos dentro del bloque funcion, si nos salimos de la tabulacion sale del bloque

mi_funcion() # llamando la función
mi_funcion()
mi_funcion()
# podemos llamar a la funcion las veces que sean necesarias
# no se puede llamar antes de definirla

# Desempaquetado de listas o list Unpacking
def show(name, lastName): # parametros
    print(name+' '+lastName)
person = ['Ariel', 'Betancud']
show(person[0],person[1]) # pasamos uno por uno los datos de la lista
# para que muestre todos los datos
show(*person) # aqui muestra todo
# tambien lo usamos con tuplas
person2 = ('Osvaldo', 'Giordanini')
show(*person2)
# con diccionarios
person3 = {'lastName': 'Lucero', 'name': 'Natalia'}
show(**person3) # dos asteriscos porque tenemos clave y valor

#REPASO DE FOR ELSE
numbers = [1, 2, 3, 4, 5]
for n in numbers:
    print(n)
    if n == 3:
        break # esta es la unica manera para que no se ejecute el else
else:
    print('Esto se terminó')

# LIST COMPRHENSION, LISTA DE COMPRENSION
names = ['Paola', 'Rodrigo', 'Lupe', 'Pepe']
alongP = [p for p in names if p[0] == 'P'] # esto regresa una nueva lista
print(alongP) # imprime nombres con letra P

# con un diccionario
bottleC = [{'name': 'Quilmes', 'country': 'Arg'},
           {'name': 'Corona', 'country': 'Mx'},
           {'name': 'Stella Artois', 'country': 'Belgium'},
           ]
Arg = [b for b in bottleC if b['country'] == "Arg"]
print(Arg)
print(bottleC)

# FUNCIONES: PASO DE ARGUMENTOS
def mi_funcion2(name, lastName):
    print('saludos a todos')
    print(f'Nombre: {name}, Apellido: {lastName} ')
    print(f'Nombre: {name}, Apellido: {lastName}')
    mi_funcion2('Jorge', 'Lucero')
    mi_funcion2('Ariel', 'Betancud')
    mi_funcion2('Analia', 'Pedrosa')

# FUNCIONES: PALABRA RETURN
# Creamos una funcion para sumar
def sumar(a,b):
    return a + b
resultado = sumar(78, 22)
#print(f'el resultado de la suma es: {resultado}')
print(f'El resultado de la suma es: {sumar(55, 45)}')

# FUNCIONES: VALORES POR DEFAULT EN ARGUMENTOS
def sumar2(a = 0, b = 0): # le damos un valor por default
    return a + b
resultado = sumar2()
print(f'Resultado e la suma: {resultado}')
print(f'Resultado de la suma: {sumar2(22, 66)}')

# FUNCIONES: ARGUMENTOS, VARIABLES EN FUNCIONES
def listarNombres(*nombres): # desconocemos la cantidad de argumentos
    for nombre in nombres:
        print(nombre)
listarNombres('Lucas', 'Jose', 'Claudia', 'Rosa', 'María')
listarNombres('Marcos', 'Daniel', 'Romina','Pepe','Marcela')

