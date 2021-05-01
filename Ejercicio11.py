# Ejercicio 11
print("El programa está orientado a intercambiar el valor de las variables ingresadas (solo se permiten números).")
a = float(input("Digite el valor de a: "))
b = float(input("Digite el valor de b: "))

print(f"El valor de a es: {a}")
print(f"El valor de b es: {b}")

a, b = b, a

print(f"Despues del intercambio, el valor de a es: {a}")
print(f"Despues del intercambio, el valor de b es: {b}")
