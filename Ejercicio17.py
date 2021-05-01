# Ejercicio 17
print("El programa está orientado a convertir segundos en horas.")
segundos = float(input("Digite los segundos a convertir: "))
minutos = segundos * 1 / 60
horas = minutos * 1 / 60
horas = round(horas, 4)

print(f"Representa {horas} hora(s)")
