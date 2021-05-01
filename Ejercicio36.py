# Ejercicio 36
print("El programa está orientado a brindar el nombre del número ingresado (solo se aceptan desde el 0 - 10).")
lista = ["Cero", "Uno", "Dos", "Tres", "Cuatro", "Cinco", "Seis", "Siete", "Ocho", "Nueve", "Diez"]
numero = int(input("Digita un número entre 0 y 10 para saber su nombre: "))
if 0 <= numero <= 10:
    print(f"El nombre de {numero} es: {lista[numero]}")
else:
    print("Digitó un número fuera de rango.")
