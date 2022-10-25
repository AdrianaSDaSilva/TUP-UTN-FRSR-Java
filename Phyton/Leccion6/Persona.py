# class Persona: # Creamos una clase
#  pass #pass no se procesa nada más(no tiene contenido)
# print(type(Persona)) # para ver de que se trata Persona
# solo muestra que es una clase

# para agregar atributos o caracteristicas necesitamos un método
# el método es similar a un constructor
# en phyton el constructor esta oculto, se llama por el lenguaje
# para inicializar los objetos va a depender del método init

class Persona:
    def __init__(self, nombre, apellido, dni, edad, *args,
                 **kwargs):  # Definimos un método, el self es el parámetro por default
        # self significa uno mismo
        # Atributos dentro de un método
        self.nombre = nombre
        self.apellido = apellido
        self._dni = dni
        self.edad = edad
        self.args = args
        self.kwargs = kwargs


    # Respetamos la tabulación de Persona si queremos seguir en esa clase
    def mostrar_detalle(self):  # self es idéntica a this usado en otros lenguajes
        print(
            f'La clase tiene los siguientes datos: {self.nombre} {self.apellido} {self._dni}  {self.edad}. el teléfono y la dirección es: {self.args}, los datos importantes son: {self.kwargs}')


# creamos un objeto de la clase
Persona1 = Persona('Ariel', 'Betancud', 34354521, 40)  # este construcotr apunta al init
print(Persona)
print(Persona1.nombre)
print(Persona1.apellido)
print(Persona1.edad)

# CREACION DE OBJETOS CON ARGUMENTO
## class Persona2:
##   def __init__(self, nombre, apellido, edad): # se definen las variables
##       self.nombre = nombre
##     self.apellido = apellido
##   self.edad = edad

# agregamos un segundo objeto
Persona2 = Persona('Osvaldo', 'Giordanini', 35966988, 45)
print(f'El objeto 2 de la clase persona: {Persona2.nombre} {Persona2.apellido} , su edad es: {Persona2.edad}')

# MODIFICAMOS LOS DATOS
Persona1.nombre = 'Liliana'
Persona1.apellido = 'Buccella'
Persona1.edad = 40
print(f'El objeto1  de la clase persona: {Persona1.nombre} {Persona1.apellido} , su edad es: {Persona1.edad}')

# los atributos son características RECORDAR
# los métodos son el comportamiento qe van a tener los objetos (acciones)
# un método es igual que una función
# al método se lo llama porque se asocia a una clase
# la funcion es propia de si misma

# LA VARIABLE SELF SOLO SE ENCUENTRA DENTRO DE LOS METODOS
# utilizamos un método que es mostrar_detalle
Persona1.mostrar_detalle()  # La referencia se pasa de manera automática
Persona2.mostrar_detalle()

# otra forma de llamar al metodo
Persona.mostrar_detalle(Persona1)  # debemos darle una referencia
# PErsona1 y Persona2 son objetos

# agregar atributos al objeto sin que esten cargados en el metodo init
Persona1.telefono = '1234567890'
print(Persona1.telefono)

persona3 = Persona('Rogelio', 'Romero', 35255699, 22, 'Teléfono', '1234567890', 'Calle Lopez', 852, 'Manzana', 77, 'Casa', 5,
                   Altura=1.93, Peso=89, CFavorito='Azul', Auto='Citroen', Modelo=2021)
# Desde 22 hasta 18 es una tupla; desde altura hasta Modelo es un diccionario
persona3.mostrar_detalle()

# ENCAPSULAMIENTO EN PHYTON
# EN PHYTON NO FUNCIONA CON MODIFICADORES DE ACCESO PUBLIC O PRIVATE
# EN PHYTON LOS ATRIBUTOS SON PUBLICOS, NO HAY ENCAPSULAMIENTO
# AGREGAMOS _ A APELLIDO PARA ENCAPSULAR
persona3.mostrar_detalle()
print(persona3._dni) # NO DEBERIA UTILIZARSE DE ESTA MANERA
# SI AGREGAMOS DOS __ NO SE PUEDEN MODIFICAR LOS DATOS

# CLASE 10
# ENCAPSULAMIENTO OBJETIVO ES QUE NO SE PUEDAN ACCEDER A LOS ATRIBUTOS DE LAS CLASES
# PARA ACCEDER A ELLOS UTILIZAMOS LOS METODOS SET Y GET
# GET NOS PERMITE OBTERNER LOS ATRIBUTOS DE UNA CLASE
# SET NOS PERMITE MODIFICAR LOS ATRIBUTOS DE UNA CLASE
# HAY QUE CREAR UN METODO GET Y SET
