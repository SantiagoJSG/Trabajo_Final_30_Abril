# Ejercicio 7
print("El programa está orientado a calcular el valor de una venta con IVA del 19%.")

iva = 0.19
venta = float(input("Digite el valor de su compra: "))
iva_singular = venta * iva
iva_incluido = venta + iva_singular

print(f"El valor de la venta original es de: {venta}")
print(f"El valor del iva es de: {iva_singular}")
print(f"El valor de la venta con iva incluido es de: {iva_incluido}")
