class Rectangulo:
    """
    Crear una clase llamada REctangulo, debe tener 2 atributos: altura y base
    el nombre del método será calcular_area utilizando la formula:
    area = base * altura. Pero la base y la altura deben ser ingresadas por el
    usuario y los objetos deben ser tres.
    """

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

base = int(input('Digite la medida de la base del rectángulo: '))
altura = int(input('Digite la medida de la altura del rectángulo: '))

rectangulo1 = Rectangulo(base, altura)
print(f'El área del rectángulo es: {rectangulo1.calcular_area()}')
