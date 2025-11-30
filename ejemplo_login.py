#Credenciales
usuario = "David"
contrasena = "admin123"
intentos = 3


usuario_input = None
contrasena_input = None

while usuario_input != usuario:
    usuario_input = input("Ingrese usuario: ")
    if usuario_input.isdigit():
        print("Nombre de usuario no valido")

    elif usuario_input != usuario:
        print("Incorrecto. Intentelo de nuevo")

print(f"Bienvenido {usuario}!")

while contrasena_input != contrasena and intentos != 0:
    print(f"Tienes {intentos} intentos")
    contrasena_input = input("Ingrese su contrasena: ")
    if contrasena_input == None:
        print("Debes ingresar al menos un caracter")

    elif contrasena_input != contrasena:
        intentos = intentos - 1
        print("Contrasena incorrecta. Te quedan {intentos} intentos")
if intentos == 0:
    print("Has alcanzado el limite de intentos, intentelo de nuevo mas tarde.")
else:
    print(f"Bienvenido {usuario}!") 