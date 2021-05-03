# Ejercicio 20

valor = 0
cien = 0
cincuenta = 0
veinte = 0
diez = 0
cinco = 0
mil = 0

valor = int(input("Ingresa la cantidad de dínero (Mínimo 1.000): "))
if valor >= 1000:
    cien = int(valor / 100000)
    reserva = valor % 100000

    cincuenta = int(reserva / 50000)
    reserva = reserva % 50000

    veinte = int(reserva / 20000)
    reserva = reserva % 20000

    diez = int(reserva / 10000)
    reserva = reserva % 10000

    cinco = int(reserva / 5000)
    reserva = reserva % 5000

    dosmil = int(reserva / 2000)
    reserva = reserva % 2000

    mil = int(reserva / 1000)
    reserva = reserva % 1000

    print("La cantidad mínima de cada billete son: ")
    print(str(cien) + " de 100.000" + "\n" + str(cincuenta) + " de 50.000" + "\n" + str(veinte) + " de 20.000" + "\n" + str(diez) + " de 10.000" + "\n" + str(cinco) + " de 5.000" + "\n" + str(dosmil) + " de 2.000" + "\n" + str(mil) + " de 1.000")
else:
    print("Digitó un número fuera del rango")
