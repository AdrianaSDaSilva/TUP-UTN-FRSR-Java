#Ejercicio Etapas de vida según la edad
edad = int(input('Digite su edad: '))
mensaje = None
if 0 <= edad < 10: #Sintaxis simplificada
    mensaje = 'La infancia es increible y bella'
elif 10 <= edad < 20:
    mensaje = 'Tienes muchos cambios y afortunadas aventuras por vivir'
elif 20 <= edad < 30:
    mensaje = 'El amor y el trabajo empiezan a dar forma'
else:
    mensaje = 'Digitá un edad menor por que ya estarias viejo... =)'
print(f'Tu edad es: {edad}, {mensaje}')

