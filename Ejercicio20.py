import os

cantidad_de_euros = int(input('Ingresa el valor de cantidad de euros: '))
monedas_de_1 = cantidad_de_euros
billetes_de_500 = (monedas_de_1-monedas_de_1 % 500)//500
monedas_de_1 = monedas_de_1 % 500
billetes_de_200 = (monedas_de_1-monedas_de_1 % 200)//200
monedas_de_1 = monedas_de_1 % 200
billetes_de_100 = (monedas_de_1-monedas_de_1 % 100)//100
monedas_de_1 = monedas_de_1 % 100
billetes_de_50 = (monedas_de_1-monedas_de_1 % 50)//50
monedas_de_1 = monedas_de_1 % 50
billetes_de_20 = (monedas_de_1-monedas_de_1 % 20)//20
monedas_de_1 = monedas_de_1 % 20
billetes_de_10 = (monedas_de_1-monedas_de_1 % 10)//10
monedas_de_1 = monedas_de_1 % 10
billetes_de_5 = (monedas_de_1-monedas_de_1 % 5)//5
monedas_de_1 = monedas_de_1 % 5
monedas_de_2 = (monedas_de_1-monedas_de_1 % 2)//2
monedas_de_1 = monedas_de_1 % 2

print('Valor de billetes de 10: ' + repr(billetes_de_10))
print('Valor de billetes de 100: ' + repr(billetes_de_100))
print('Valor de billetes de 20: ' + repr(billetes_de_20))
print('Valor de billetes de 200: ' + repr(billetes_de_200))
print('Valor de billetes de 5: ' + repr(billetes_de_5))
print('Valor de billetes de 50: ' + repr(billetes_de_50))
print('Valor de billetes de 500: ' + repr(billetes_de_500))
print('Valor de monedas de 1: ' + repr(monedas_de_1))
print('Valor de monedas de 2: ' + repr(monedas_de_2))
print()
os.system('pause')
