# Ejercicio 9
print("El programa está orientado a calcular el área de un hexágono (en cm).")
perimetro = float(input("Digite el valor del perímetro del hexágono: "))
apotema = float(input("Digite el valor del apotema del hexágono: "))
area = perimetro * apotema / 2
area = round(area, 2)

print(f"El área del círculo es de: {area} cm^2")
