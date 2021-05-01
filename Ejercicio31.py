# Ejercicio 31
print("El programa está orientado a determinar si la suma del primer y segundo valor ingresado sea mayor o menor que el tercero.")
numero1 = float(input("Digite un número: "))
numero2 = float(input("Digite un número: "))
numero3 = float(input("Digite un número: "))

suma = numero1 + numero2

if suma > numero3:
    print(f"La suma del primero y el segundo número: {suma}, es mayor que el tercer número ingresado {numero3}")
elif suma == numero3:
    print(f"La suma del primero y el segundo número: {suma}, es igual que el tercer número ingresado {numero3}")
else:
    print(f"La suma del primero y el segundo número: {suma}, es menor que el tercer número ingresado {numero3}")
