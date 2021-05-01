# Ejercicio 16
from math import sqrt
print("El programa está orientado a calcular la distancia entre 2 coordenadas (x1, y1) (x2, y2).")

x1 = float(input("Valor de x1: "))
x2 = float(input("Valor de x2: "))
y1 = float(input("Valor de y1: "))
y2 = float(input("Valor de y2: "))

distancia = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
distancia = round(distancia, 2)

print(f"La distancia entre dichos puntos es de: {distancia} unidades")
