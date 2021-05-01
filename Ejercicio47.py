# Ejercicio 47
print("El programa está orientado a imprimir los números naturales contenidos entre dos números ingresados.")
n = int(input("Digite un número entero: "))
m = int(input("Digite un número entero mayor al anterior: "))
m += 1

if m > n:
    for i in range(n, m):
        print(i)
elif m == n:
    print(m)
else:
    print("Error, el valor del segundo número debe ser mayor al primero")
