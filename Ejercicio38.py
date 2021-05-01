# Ejercicio 38
print("El programa está orientado a identificar si al ingresar 3 números, estos en su sencuencia estan aumentando, decreciendo o estan al azar.")
print("Digite 3 numeros :")
a = float(input("Número 1: "))
b = float(input("Número 2: "))
c = float(input("Número 3: "))
if a < b < c:
    print("Los numeros estan aumentando")
elif a > b > c:
    print("Los numeros estan disminuyendo")
else:
    print("No se incrementa, ni se disminuye")
