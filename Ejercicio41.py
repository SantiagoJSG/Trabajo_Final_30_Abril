# Ejercicio 41
print("El programa está orientado a identificar si al ingresar 3 números al menos 2 de ellos se repiten.")
print("Digite 3 numeros: ")
a = float(input("Digite un número: "))
b = float(input("Digite otro número: "))
c = float(input("Digite otro número: "))
if a == b or a == c or b == c:
    print("Al menos dos o más de los numeros ingresados son iguales")
else:
    print("Ninguno de los numeros ingresados son iguales")
