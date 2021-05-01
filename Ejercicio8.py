# Ejercicio 8
print("El programa está orientado a calcular el área y perímetro de un círculo (en cm).")
pi = 3.1416
radio = float(input("Digite el valor del radio de su círculo (en cm): "))
area = pi * radio ** 2
perimetro = 2 * pi * radio
area = round(area, 2)
perimetro = round(perimetro, 2)

print(f"El área del círculo es de: {area} cm^2")
print(f"El perímetro del círculo es de: {perimetro} cm")
