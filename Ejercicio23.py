# Ejercicio 23
print("El programa está orientado a determinar si el número ingresado es positivo o negativo (solo se aceptan números enteros).")
numero = float(input("Digite un número: "))

if numero < 0:
    print("Ingreso un número negativo")
elif numero == 0:
    print("Ingreso 0")
else:
    print("Ingreso un número positivo")
