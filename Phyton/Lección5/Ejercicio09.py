# Ejercicio 9: Mostrar una frase sin espacios y contar su longitus
# Hacer un programa donde el usuario ingrese una frase, se le
# devolverá la misma frae pero sin espacios en blanco, y
# además un contador de cuantos caracteres tiene la frase
# sin contar los espacion en blanco
# Ejemplo:    frase = vivi por siempre en paz
# frase final = vivirporsiempreenpaz
# n° de caracteres = 21

frase1 = input('Digite una frase: ')
frase2 = ' '
for i in frase1:
    if i != " ":
        frase2 += i
frase1 = frase2
print(f'\nFrase Final: {frase1}')
print(f'N° de caracteres: {len(frase1)}')

