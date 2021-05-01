# Ejercicio 19
print("El programa está orientado a convertir segundos en horas, minutos y segundos.")
segundos = int(input("Digite los segundos a convertir: "))
horas = int(segundos / 3600)
minutos = int((segundos - (horas * 3600)) / 60)
segundos = segundos - ((horas * 3600) + (minutos * 60))

print(f"{horas} h {minutos} m {segundos} s")
