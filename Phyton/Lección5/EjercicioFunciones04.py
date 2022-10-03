# Eejrcicio 4: Calculadora de Impuestos
# Crear una funcion para calcular el total de un pago incluyendo
# un impuesto aplicado (IVA)
# Formula: pago toal = pago sin impuesto  + pago sin impuesto * (impuesto/100)
# proporcione el pago sin impuesto: 1000
# proporciones el monto del impuesto: 21%
# pago con impuesto: xxxxx

# creamos la funcion que calcula el total del pago incluyendo el impuesto
def calcular_total_pago(pago_sin_impuesto, impuesto):
    pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
    return pago_total

# ejecutamos la funcion, pedimos los datos al usuario
pago_sin_impuesto = float(input('Digite el pago sin impuestos: '))
impuesto = float(input('Digite el valor del impuesto a aplicar: '))
pago_con_impuesto = calcular_total_pago(pago_sin_impuesto, impuesto)
print(f'El pago con impuesto es: {pago_con_impuesto}')
