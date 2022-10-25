class Persona2:
    def __init__(self, nombre, apellido, edad):  # estan encapsulados
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalle(self):
        print(f'Los datos a mostrar son los siguientes: {self._nombre} {self._apellido} {self._edad}')

    # AGREGAMOS UN DECORADOR
    @property
    # CREAMOS EL METODO GETTER
    def nombre(self):
        print('Estamos usando el metodo get')
        return self._nombre

    # CREAMOS EL METODO SETTER
    @nombre.setter
    def nombre(self, nombre):  # pasamos el parámetro
        print('Estamos usando el metodo set')
        self._nombre = nombre

    @property
    def apellido(self):
        print('Estamos usando el método get')
        return self._apellido
    @apellido.setter
    def apellido(self, apellido):
        print('Estamos usando el método set')
        self._apellido = apellido

    @property
    def edad(self):
        print('Estamos usando el método get')
        return self._edad
    @edad.setter
    def edad(self, edad):
        print('Estamos usando el método set')
        self._edad = edad

    # creamos una funcion para borrar
    def __del__(self):
        print(f'Persona2: {self._nombre} { self._apellido} {self._edad}')

if __name__ == 'main':


    # COMO MOSTRAMOS ESTO ( el metodo get)
    persona1 = Persona2('Ariel', 'Betancud', 41)
    print(persona1.nombre) # Aqui llamamos al metodo que no necesita parametros, al metodo getter

    # COMO LLAMAMOS AL METODO SET
    persona1.nombre = 'Juan Pedro'
    print(persona1.nombre)
    print(persona1.mostrar_detalle())

    # persona1._edad = 40
    # print(persona1.edad) # en este caso se transforma en un read only
    # esto sucede cuando no se hizo el set y esta encapsulado
    # NO SE DEBE HACER PORQUE ESTA ENCAPSULADO
    # PODRIAMOS MOSTRARLO PERO NO MODIFICARLO
    # READ ONLY = SOLO LECTURA

    # EJERCICIO
    # CREAR TRES OBJETOS MAS UTILIZANDO LOS MÉTODOS GETTER Y SETTER
    # PARA MODIFICAR, Y MOSTRAR LOS CAMBIOS.

    persona_A = Persona2('Ivana', 'Germir', 33)
    print(persona_A.nombre)
    print(persona_A.apellido)
    print(persona_A.edad)
    persona_A.nombre = 'Ivi'
    persona_A.apellido = 'Gonzalez'
    persona_A.edad = 32
    print(persona_A.mostrar_detalle())

    persona_B = Persona2('Lucas', 'Diaz', 25)
    print(persona_B.nombre)
    print(persona_B.apellido)
    print(persona_B.edad)
    persona_B.nombre = 'Lukas'
    persona_B.apellido = 'Dominguez'
    persona_B.edad = 35
    print(persona_B.mostrar_detalle())

    persona_C = Persona2('Ema', 'Clabero', 31)
    print(persona_C.nombre)
    print(persona_C.apellido)
    print(persona_C.edad)
    persona_C.nombre = 'Emanuel'
    persona_C.apellido = 'Clavero'
    persona_C.edad = 32
    print(persona_C.mostrar_detalle())

    # COMPROBACION DE DONDE SE ESTA EJECUTANDO EL CODIGO
    print(__name__)