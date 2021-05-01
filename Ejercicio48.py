# Ejercicio 48
print("El programa está orientado a determinar la suma de los números naturales contenidos entre dos números ingresados.")
print("Digite dos numeros, pero el primero debe ser menor que el segundo: ")
num1 = int(input("Número 1: "))
num2 = int(input("Número 2: "))
num2 += 1
y = 0
contador = num2 - num1
if num2 > num1:
    for x in range(num1, num2 + 1):
        y = y + x
        contador = contador - 1
        if contador == 0:
            print(y)
            break
else:
    print("El primer numero que digitó no es menor que el segundo")
