# Ejercicio 33
print("El programa está orientado a determinar si el año ingresado es bisiesto o no.")
x = int(input("Digite un año para determinar si es o no bisiesto: "))

if x % 4 == 0 and (x % 100 != 0 or x % 400 == 0):
    print("Es bisiesto")
else:
    print("No es bisiesto")
