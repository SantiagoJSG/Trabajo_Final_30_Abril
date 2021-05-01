# Ejercicio 10
print("El programa está orientado a calcular el promedio de 3 números ingresados (escala del 0 - 5).")
num1 = float(input("Digite su primer valor: "))
num2 = float(input("Digite su segundo valor: "))
num3 = float(input("Digite su tercer valor: "))
promedio = (num1 + num2 + num3) / 3

if 0 <= num1 <= 5 and 0 <= num2 <= 5 and 0 <= num3 <= 5:
    print(f"El promedio de los valores ingresados es de: {promedio}")
else:
    print("Error, digitó números fuera del rango permitido.")
