# Ejercicio 50
print("El programa está orientado a leer números infinitamente, para luego calcular su suma y promedio.")
count = 0
suma = 0
numero = 1

while numero != 0:
    numero = int(input("Digite un número entero (Digite 0 para terminar el proceso): "))

    if numero != 0:
        suma += numero
        count += 1

if count == 0:
    print("No digitó ningún número.")
else:
    promedio = suma / count
    print(f"El promedio de los {count} números es igual a {promedio}")
    print(f"La suma de los {count} números es igual a {suma}")
