# Ejercicio 6: Tabla de multiplicar
# Hacer un programa que pida un número por teclado y guarde
# en una lista su tabla de multiplicar hasta el 10. Por ejemplo:
# si digita el 5 la lista tendrá:5,10,15,20,25,30,35,40,45,50

numero = int(input("Digite un número: "))

lista = [] # es una lista vacía

for i in range(1,11):
    lista.append(i*numero)
# print(f'\nTabla de multiplicar del {numero}: \n{lista}')
#f es interpolacion

#for indice,i in enumerate(lista):
 #   print(f'{numero} x {i} = {lista[indice]}')

for j in range(1, 11):
    print(f' {numero} x {j} = {numero * j}')