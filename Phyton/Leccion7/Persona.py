class Persona:  # Está heredando la clase persona de la clase objet
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    @property
    def edad(self):
        return self._edad
    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def __str__(self): # lo que hace este metodo es sobreescribir
        return f'Persona: {self._nombre} {self._edad}'
        # no los muestra con el valor real
        # muestra los datos en tipo string



class Empleado(Persona):  # hereda de la clase persona
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad) # usamos las caracteristicas de clase padre
        self._sueldo = sueldo
    @property
    def sueldo(self):
        return self._sueldo
    @sueldo.setter
    def sueldo(self, sueldo):
        self._sueldo = sueldo

    def __str__(self):
        return f'Empleado:  Sueldo: {self._sueldo} {super().__str__()}'


empleado1 = Empleado('Ariel', 45, 75000)
print(empleado1.nombre)
print(empleado1.edad)
print(empleado1.sueldo)
# Tarea: encapsular los atributois y agregar los métodos getters and setters
# Crear otro objeto, pasar los datos para nombre, edad y sueldo
# Mostrar estos datos, luego modificar y mostrar nuevamente

empleado2 = Empleado('Liliana', 36, 500000)
print(empleado2.nombre)
print(empleado2.edad)
print(empleado2.sueldo)
empleado2.nombre = 'Natalia'
empleado2.edad = 35
empleado2.sueldo = 80000
print(empleado2.nombre)
print(empleado2.edad)
print(empleado2.sueldo)