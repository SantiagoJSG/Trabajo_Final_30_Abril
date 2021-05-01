# Ejercicio 30
print("El programa está orientado a determinar el número mayor y menor de los valores ingresados.")

lista = []
numero1 = float(input("Digite un número: "))
numero2 = float(input("Digite un número: "))
numero3 = float(input("Digite un número: "))

lista.append(numero1)
lista.append(numero2)
lista.append(numero3)

print(f"El valor máximo es: {max(lista)}")
print(f"El valor minimo es: {min(lista)}")
