# Ejercicio 45
rango = int(input("Digita un número natural del que se hara un conteo hasta llegar a este: "))
rango += 1

if 0 <= rango:
    for i in range(rango):
        print(i)
else:
    print("Digitó un número negativo")
