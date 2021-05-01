# Ejercicio 49
print("El programa está orientado a leer 10 números, para calcular su suma y promedio.")
count = 0
suma = 0
numero = 1

while count != 10:
    numero = float(input("Digite un número: "))
    suma += numero
    count += 1

else:
    promedio = suma / count
    print(f"El promedio de los {count} números es igual a {promedio}")
    print(f"La suma de los {count} números es igual a {suma}")
