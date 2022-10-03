# Ejercicio 5: Convertidor de temperaturas
# Realizar dos funciones para convertir de grados  celsius
# a fahrenheit y viseversa
# Investigar las formulas

# funcion que convierte de cesius a fahrenheit
def celsius_fahrenheit(celsius):
    return celsius * 9 / 5 + 32 # la presedencia de operacion:primero multiplica, luego divide y por ultimo suma

 # funcion de fahrenheit a celsius
def fahrenheit_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9 # parentesis para que primero reste



celsius = float(input('Digite el valor de celsius que desea convertir: '))
resultado = celsius_fahrenheit(celsius)
print(f'{celsius} C a F -> {resultado:.2f}')

fahrenheit = float(input('Digite el valor farhenheit que desea convertir a celsius: '))
resultado = fahrenheit_celsius(fahrenheit)
print(f'{fahrenheit} F a C -> {resultado:.2f}')

