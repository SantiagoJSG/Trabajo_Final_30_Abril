# Ejercicio 46
print("El programa está orientado a imprimir los números contenidos entre 1 y el ingresado, con un curioso patrón.")
conta1 = 1
conta2 = -2
x = True
num = int(input("Digite el limite para la sucesión de numeros :"))
num = num + 1
print(conta1)
print(conta2)
while x:
    conta1 = conta1 + 2
    conta2 = conta2 - 2
    if conta1 == num:
        break
    else:
        print(conta1)
    if conta2 * -1 == num:
        break
    else:
        print(conta2)
