##CLASE 5##
#OPERADORES DE PYTHON PARTE 2#

 #OPERADORES LÓGICOS#
#Operador and
a = True
b = True
resultado = a and b
print(resultado)

#Operador or
resultado = a or b
print(resultado)

#Operador not
resultado = not a
print(resultado) ## operador unario'''

#Ejercicio: Valor dentro de un rango
valor = int(input("Digite un número: "))
ValorMinimo = 0
ValorMaximo = 5
dentroRoango = (valor >= ValorMinimo and valor <= ValorMaximo)
if dentroRoango:
    print(f'El valor {valor} está dentro del rango')
else:
    print(f'El valor {valor} no está dentro del rango')

#################################################
#Ejercicio con operador or
vacaciones = False
diaDescanso = False
if vacaciones or diaDescanso:
    print ('Puede asistir al juego')
else:
    print('tiene trabajo que hacer')
##################################################
#Ejercicio: Rango entre 20 y 30 años.

edad = int(input("Digite su edad:"))
#veinte = edad >= 20 and edad < 30
#print(veinte)
#treinta = edad >= 30 and edad < 40
#print(treinta)

# SINTAXI SIMPLIFICADA DEL OPERADOR AND
#if veinte or treinta
if (20 <= edad < 30) or (30 <= edad < 40 ):
    print('Estas dentro del rango de los (20\'0) a (30\' 0) años ')
#    if veinte:
#        print('Estas dentro del rango de los rangos (20\'0) años')
#    elif treinta:
#        print('Estas dentro del rango de los rangos (30\'0) años')
#    else:
#        print('No estas dentro del rango')
else:
    print('No estas dentro del rango de los (20\'0) a (30\' 0) años ')

##########################################################################

#Ejercicio: el mayor de dos números

numero1 = int(input('Digite el valor para el numero1: '))
numero2 = int(input('Digite el valor para el numero2: '))

if numero1 > numero2:
    print(('El número 1 es mayor'))
else:
    print(('El número 2 es mayor'))
###########################################################################
#Ejercicio => Tienda de libros
print('Digite los siguientes datos del libro: ')
nombre = input('Digite el nombre del libro: ')
id = int(input('Digite el ID del libro: '))
precio = float(input('Digite el precio del libro: '))
envioGratuito = input('Indicar si el libro es gratuito (True/Flase): ')

if envioGratuito == 'True':
   envioGratuito = True
elif envioGratuito =='False':
     envioGratuito = False
else:
    emvioGratuito = 'El valor es incorrecto, debe escribir True o False'
print(f'''
        Nombre: {nombre}
        Id: {id}
        Precio: {precio}
        Envio Gratuito?: {envioGratuito}
''')
