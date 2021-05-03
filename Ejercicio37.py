# Ejercicio 37
def contar_digitos_letras(cadena):
    digitos = 0
    letras = 0

    for c in cadena:
        if c.isdigit():
            digitos += 1
        elif c.isalpha():
            letras += 1
        else:
            pass

    return digitos, letras


texto = input("Digite un texto: ")
resultado = contar_digitos_letras(texto)

print("Cantidad de dígitos: %i" % resultado[0])
print("Cantidad de letras: %i" % resultado[1])
