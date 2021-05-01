# Ejercicio 27
print("El programa está orientado a calcular la definitiva de un alumno y brindara mensajes personalizados dependiendo su rendimiento.")
n1 = float(input("Digite la nota 1: "))
n2 = float(input("Digite la nota 2: "))
n3 = float(input("Digite la nota 3: "))
n4 = float(input("Digite la nota 4: "))
n5 = float(input("Digite la nota 5: "))
definitiva = (n1 * 0.15) + (n2 * 0.20) + (n3 * 0.15) + (n4 * 0.30) + (n5 * 0.20)
if definitiva > 4.5:
    print("Felicitaciones")
elif definitiva >= 3:
    print("Aprobó")
elif 3 > definitiva > 2:
    print("Reprobó")
elif definitiva < 2:
    print("No puede habilitar")
print(f"La nota final del estudiante, es de: {definitiva}")
