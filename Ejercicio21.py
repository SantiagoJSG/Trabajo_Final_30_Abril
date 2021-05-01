# Ejercicio 21
print("El programa está orientado a invertir el número ingresado.")
numero_ingresado = (input("Ingrese un número: "))
revertir = 0
try:
    valor = int(numero_ingresado)
    while valor > 0:
        residuo = valor % 10
        revertir = (revertir * 10) + residuo
        valor //= 10
    print(f"El inverso del número ingresado es: {revertir}")
except ValueError:
    print("Ese número no es valido. Inténtalo de nuevo")
