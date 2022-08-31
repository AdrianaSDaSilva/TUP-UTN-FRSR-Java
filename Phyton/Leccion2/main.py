#SENTENCIA DE CLASE if/eslse

'''condicion = 10
if condicion == True:
    print('Condicion verdadera')
elif condicion == False:
    print('Condición Falsa')
else:
    print('Condicion Falsa')
'''
################################
# CONVERSIÓN DE NÚMERO A TEXTO
num = int(input('Digite un número en el rango del 1 al 3: '))
numTexto = ''
if num == 1:
    numTexto = 'Número uno'
elif num == 2:
    numTexto = 'Número dos'
elif num == 3:
    numTexto = 'Número tres'
else:
    numTexto = 'Has ingresado un número fuera de rango'
print(f'El número ingresadoi es: {num} - {numTexto}')



