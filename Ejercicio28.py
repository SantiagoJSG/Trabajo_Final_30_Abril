# Ejercicio 28
print("El programa está orientado a determinar el número mayor de los valores ingresados.")
numero1 = float(input("Número 1: "))
numero2 = float(input("Número 2: "))

if numero1 > numero2:
    print(f"El número mayor es: {numero1}")
elif numero1 < numero2:
    print(f"El número mayor es: {numero2}")
else:
    print("Son iguales")
