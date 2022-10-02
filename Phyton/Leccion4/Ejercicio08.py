# Ejercicio 8: Menú interactivo - Cajero automático
# Hacer un programa que simule un cajero automático con un saldo
# inicial de $1000 y tendrá el siguiente menú de opciones:
# 1. Ingresar dinero en la cuenta
# 2. Retirar dinero de la cuenta
# 3. Mostrar dinero disponible
# 4. Salir

saldo = 1000
while True:
    print('\t.:MENU:.')
    print('1. Ingresar dinero en la cuenta')
    print('2. Retirar dinero de la cuenta')
    print('3. Mostrar dinero disponible')
    print('4. Salir')
    opcion = int(input('Digite una opción de menú: '))
    print()
    if opcion == 1:
        extra = float(input('¿Cuánto dinero desea ingresar? -> '))
        saldo += extra
        print(f'Dinero total en la cuenta: ${saldo}')
    elif opcion == 2:
        retirar = float(input('¿Cuánto dinero desea retirar? -> '))
        if retirar > saldo:
            print(f'Saldo insuficiente, ingrese un monto menor')
        else:
            saldo -= retirar
    elif opcion == 3:
        print(f'Saldo disponible: ${saldo}')
    elif opcion == 4:
        print('GRACIAS POR UTILIZAR EL SERVICIO, HASTA PRONTO')
        break
    else:
        print('Error, elija una opción válida')


