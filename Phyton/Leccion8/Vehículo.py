class Vehiculo:
    '''
    Definir una clase padre llamada vehiculo y dos clases hijas llamadas
    Auto y Bicicleta, las cuales heredan de la clase padre Vehiculo. La lclase
    padre debe tener los siguientes atributos y métodos:
    Vehiculo (clase padre)
    -Atributos(color, ruedas)
    -Metodos(__init__(color, ruedas) y __str__() )

    Auto(clase hija de Vehiculo)
    - Atributos(velocidad (km/hs))
    - Métodos(__init__(color, ruedas, velocidad) y __str__() )

    Bicicleta(clase hija de vehiculo)
    - Atributos(tipo(urbana/montaña/etc)
    - Métodos(__init__(color, ruedas, tipo) y __str__() )

    Crear un objeto de cada clase
    '''

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return 'Color: ' + self.color + ', Ruedas: ' + str(self.ruedas)

#Creamos la clase hija auto
class Auto(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
    def __str__(self):
        return super().__str__()+ ' , Velocidad(Km/hr): '+str(self.velocidad)

#Creamos la clase bicicleta
class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
    def __str__(self):
        return super().__str__()+ ' , Tipo: '+self.tipo





# Creamos un objeto clase vehiculo
vehiculo = Vehiculo('Blanco', 4)
print(vehiculo)

#Creamos el segundo objeto de la clase auto
auto = Auto('Amarillo', 4, 120)
print(auto)

#Creamos el tercer objeto bicicleta
bicicleta = Bicicleta('Rojo', 2, 'Ruta')
print(bicicleta)