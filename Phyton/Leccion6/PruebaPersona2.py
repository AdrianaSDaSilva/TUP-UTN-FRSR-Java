# IMPORTAMOS LA CLASE
from Persona2 import Persona2
# si queremos importar todas las clases seria * luego de import
print('Creación de Objetos'.center(50, '-'))
if __name__ == '__main__':
    persona5 = Persona2('Lionel', 'Messi', 35)
    persona5.mostrar_detalle()
    print(__name__)

print('Eliminación de Objetos'.center(50, '-'))
# center es para centrar el numero es la cantidad de carcteres y luego el caracter
del persona5
