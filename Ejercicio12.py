# Ejercicio 12
from math import sqrt
print("El programa está orientado a calcular el tiempo de caída de un objeto que se suelta desde una altura h.")

fuerza_de_gravedad = 10
altura = float(input("Digite la altura de lanzamiento en metros: "))
tiempo = sqrt(2 * altura / fuerza_de_gravedad)
tiempo = round(tiempo, 2)

print(f"El tiempo de caída a dicha altura es de: {tiempo} segundos")
