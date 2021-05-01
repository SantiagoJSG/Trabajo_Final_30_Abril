# Ejercicio 26
print("El programa está orientado a leer un número, si este es mayor o igual a 10, devolvera el triple de este, de lo contrario la cuarta parte de este.")
numero = float(input("Digite un número: "))
if numero >= 10:
    operacion1 = numero ** 3
    print(operacion1)
else:
    operacion2 = numero / 4
    print(operacion2)
