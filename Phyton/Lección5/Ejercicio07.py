# Ejercicio 7: Juego adivina el número
# Reailzar un juego para adivinar un númer. Para ello se debe
# generar un número aleatorio entre 1 -100, y luego ir pidiendo
# números indicando "es mayor" o "es menor segun corresponda
# El proceso termina cuando el usuario acierta
# y alli se debe mostrar el número de intentos

import random # esto es para el número aleatorio
print('\tJUEGO: ADIVINA EL NÚMERO....')
aleatorio = random.randint(0, 100) # toma de 0 a 100 literal, genera un número aleatorio
contador = 0
while True:
    numero = int(input('Digite un número: '))
    contador += 1 # operador simplificado para que vaya de 1 en 1
    if numero > aleatorio:
        print('\tNo es el número, digite un número menor')
    elif numero < aleatorio:
        print('\tNo es el número, digite un número mayor')
    else:
        print(f'FELICIDADES,acabas de adivinar el número{aleatorio}')
        break # Rompe el ciclo y el bucle al ser encontrado el número
print(f'\nNúmero de intentos: {contador}')
