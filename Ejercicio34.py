# Ejercicio 34
print("El programa está orientado a calcular una ecuación cuadrática de tipo ax2 + bx + c.")
a = float(input("A: "))
b = float(input("B: "))
c = float(input("C: "))

discriminante = (b ** 2) - 4 * a * c
if discriminante < 0:
    print("La ecuación no tiene soluciones reales")
elif discriminante == 0:
    x = -b / (2 * a)
    print(f"La solución es = {x}")
else:
    x1 = (-b - (discriminante ** 0.5)) / (2 * a)
    x2 = (-b + (discriminante ** 0.5)) / (2 * a)
    x1 = round(x1, 2)
    x2 = round(x2, 2)
    print(f"Las dos soluciones reales son = {str(x1)} y {str(x2)}")
