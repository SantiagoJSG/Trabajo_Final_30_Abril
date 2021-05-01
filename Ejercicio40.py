# Ejercicio 40
print("El programa está orientado a brindar el nombre del número ingresado en días (solo se aceptan desde el 1 - 7).")
lista = ["Invalido", "Lunes", "Martes", "Miercoles", "Júeves", "Viernes", "Sabado", "Domingo"]
numero = int(input("Digita un número entre 1 y 7 para saber el nombre del día : "))
if 1 <= numero <= 7:
    print(f"El nombre del día {numero} es: {lista[numero]}")
else:
    print("Error, Digitó un número fuera de rango.")
