class Aritmetica:  # clase Aritmetica creada
    """
    # Las triples comillas sirve para documentar las clases
    Este tipo de comentario es: DocTring
    Esto es documentacion de la clase en Phyton
    Vamos a hacer algunas operaciones de : suma, resta, multiplicación y más
    """

    # METODO INICIALIZADOR
    def __init__(self, operandoA, operandoB):
        # creamos los atributos
        self.operandoA = operandoA
        self.operandoB = operandoB

    # METODO PARA SUMAR
    def sumar(self):
        return self.operandoA + self.operandoB

    # METODO PARA RESTAR
    def resta(self):
        return self.operandoA - self.operandoB

    # METODO DE MULTIPLICAR
    def multiplica(self):
        return self.operandoA * self.operandoB

    # PARA DIVIDIR
    def dividir(self):
        return self.operandoA / self.operandoB


# CREAMOS UN OBJETO, UNA INSTANCIA DE LA CLASE ARITMETICA
aritmetica1 = Aritmetica(7, 9)  # le pasamos los argumentos para los operandos
print(aritmetica1.sumar())
print(f'la resta de los números es: {aritmetica1.resta()}')
print(f'la multiplicación de los números es: {aritmetica1.multiplica()}')
print(f'la división de los números es: {aritmetica1.dividir():.2f}')
