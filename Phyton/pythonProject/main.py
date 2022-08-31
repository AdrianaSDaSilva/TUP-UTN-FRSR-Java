#print("Hola Mundo")
miVariable = 3
print(miVariable)
miVariable = "Hola a todos los estudiantes de la Tecnicatura"
print(miVariable)
miVariable = 3.5
print(miVariable)
x = 10
y = 2
z = x + y
print(id(x))
#Las literales se escriben +528, la variable y = x272, la variable z = x592
print(id(y))
print(id(z))

#Manejo de cadenas
miGrupoFavorito = "Luciano Pereyra"
print(miGrupoFavorito)

#Unimos cadenas. Concatenacion
print("Mi grupo favorito es:" + " " + miGrupoFavorito)

numero1 = "7"
numero2 = "8"
print(int(numero1) + int(numero2))

#Tipos Booleanos (bool)
miBooleano = True
print(miBooleano)
miBooleano2 = False
print(miBooleano2)

miBooleano3 = 3 > 2
print(miBooleano3)

if miBooleano3:
    print("El resultado es verdadero")
else:
    print("El resultado es falso")

# Procesar la entrada del ususario
# funcion input
resultado = input("Digite un número: ")
print(resultado)



