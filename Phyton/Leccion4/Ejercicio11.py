# Ejercicio 11: Agenda telefónica
# Hacer un programa que simule una agenda de contactos. Crear un
# diccionario donde la clave sea el nombre del usuario y el valor
# sea el teléfono, el programa tendrá el siguiente menú de opciones:
#    1. Nuevo contacto
#    2. Borrar contacto
#    3. Ver contactos existentes
#    4. Salir

agenda = {}
while True:
    print('\t.:MENÚ: ')
    print('1. Nuevo Contacto')
    print('2. Borrar Contacto')
    print('3. Ver Contactos Existentes')
    print('4. Salir')
    opcion = int(input('Digite una opción de menú: '))
    if opcion == 1:
        nombre = input('Digite el nombre del contacto: ')
        telefono = input('Digite el número de teléfono: ')
        if nombre not in agenda:
            agenda[nombre] = telefono
            print('¡Contacto agregado exitosamente!')
        else:
            print('Este contacto ya existe')
    elif opcion == 2:
        nombre = input('Nombre de contacto: ')
        if nombre in agenda:
            del(agenda[nombre])
            print('Su contacto ha sido eliminado')
        else:
            print('El contacto no existe en tu agenda')
    elif opcion == 3:
        print('AGENDA DE CONTACTOS')
        for clave, valor in agenda.items(): # con la funcion items mostramos clave y valor
            print(f'Nombre: {clave}, Teléfono: {valor}')
    elif opcion == 4:
        print('Gracias por utilizar su agenda de contactos')
        break
    else:
        print('La opción elegida es inválida, ingrese opción válida')
        print(' ')
