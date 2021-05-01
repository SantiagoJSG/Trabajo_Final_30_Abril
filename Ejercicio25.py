# Ejercicio 25
print("El programa está orientado a calcular el resultado de una venta con IVA (19%), que al ser mayor de 150.000, se le aplicara un descuento del 5%.")
iva = 0.19
venta = float(input("Digite el valor de su compra: "))
descuento = venta * 0.05

if venta > 150000:
    valor = venta - descuento
    total = (valor * iva) + valor
    print("Tiene descuento")
    print(f"El valor de la venta original es de: {venta}")
    print(f"El valor de la venta con descuento es de: {valor}")
    print(f"El valor de la venta con descuento e iva incluido es de: {total}")
elif venta <= 150000:
    total = (venta * iva) + venta
    print("No tiene descuento")
    print(f"El valor de la venta original es de: {venta}")
    print(f"El valor de la venta con iva incluido es de: {total}")
