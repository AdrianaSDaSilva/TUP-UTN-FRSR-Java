# class Persona: # Creamos una clase
  #  pass #pass no se procesa nada más(no tiene contenido)
# print(type(Persona)) # para ver de que se trata Persona
# solo muestra que es una clase

# para agregar atributos o caracteristicas necesitamos un método
# el método es similar a un constructor
# en phyton el constructor esta oculto, se llama por el lenguaje
# para inicializar los objetos va a depender del método init

class Persona:
    def __init__(self, nombre, apellido, edad): # Definimos un método, el self es el parámetro por default
     # self significa uno mismo
     # Atributos dentro de un método
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    # Respetamos la tabulación de Persona si queremos seguir en esa clase
    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}')

# creamos un objeto de la clase
Persona1 = Persona('Ariel', 'Betancud', 40) # este construcotr apunta al init
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
Persona2 = Persona('Osvaldo', 'Giordanini', 45)
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
Persona1.mostrar_detalle()
Persona2.mostrar_detalle()


