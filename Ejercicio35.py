# Ejercicio 35
print("El programa está orientado a identificar el ingreso correcto de un usuario.")
usuario = "santijsg"
contra = "cuppycake"
u = str(input("¿Cual es el usario? "))
c = str(input("¿Cual es la contraseña? "))
if u == usuario and c == contra:
    print("Ha ingresado a la cuenta correctamente")
else:
    print("El usuario o contraseña esta incorrecto, vuelva a intentar")
