# Ejercicio 5
import math
print("El programa está orientado a leer un número decimal e imprimir su parte entera y decimal por aparte.")

numero = float(input("Digite un número decimal: "))
parte_decimal, parte_entera = math.modf(numero)

print(f"La parte entera del número digitado es: {parte_entera} y su parte decímal es: {parte_decimal}")
