# Ejercicio 39
print("El programa está orientado a identificar si al ingresar 2 números, estos esten entre 0 y 5 retornando True, de lo contrario retornara False.")
print("Digite 2 numeros :")
a = float(input("Número 1: "))
b = float(input("Número 2: "))
if 0 <= a <= 5 and 0 <= b <= 5:
    print("True")
else:
    print("False")
