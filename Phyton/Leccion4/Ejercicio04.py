# Ejercicio 4: Sumar números pares dentro de un rango
# Hacer un programa para sumar números pares dentro
# de un rango, por ejemplo:
# suma de números pares del 2 al 30
# suma = $240

a = int(input("Digite desde que número va a comenzar la suma: "))
b = int(input("¿Hasta que número quiere que llegue la suma?: "))
suma = 0
for i in range(a, b+1): # el +1 es para que llegue al 30, sino llegaría hasta el 29
    if i%2==0: # estos es si el número es par
        suma +=i
print(f"La suma de núeros pares dentro del rang es: {suma}")


