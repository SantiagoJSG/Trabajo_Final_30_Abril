# Ejercicio 24
print("El programa está orientado a determinar si el número ingresado es par-positivo, par-negativo, impar-positivo o impar-negativo (solo se aceptan números enteros).")
numero = int(input("Digite un número entero: "))

if numero < 0 and numero % 2 == 0:
    print("Ingreso un número par-negativo")
elif numero < 0 and numero % 2 != 0:
    print("Ingreso un número impar-negativo")
elif numero > 0 and numero % 2 == 0:
    print("Ingreso un número par-positivo")
elif numero > 0 and numero % 2 != 0:
    print("Ingreso un número impar-positivo")
else:
    print("Digitó 0")
