# Ejercicio 32
print("El programa está orientado a calcular el precio de un pasaje en avión.")
k = float(input("¿Cuanta distancia en kilometros va a recorrer en su vuelo?: "))
d = float(input("¿Cuantos dias ocupara su estancia? :"))
precio = 5000 * k
if precio < 100000:
    precio = 100000
if k > 1000 and d > 7:
    preciopago = precio - (precio * 0.15)
    print(f"El valor total de el vuelo aplicando un descuento del 15% es de : {preciopago}")
else:
    print(f"El valor total de su vuelo es de : {precio}")
