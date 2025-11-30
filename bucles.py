#Estructuras de repeticion en Python
#for -definido (;imite), tu le pones un limite ejemplo: 1 a 100

for i in range(1, 21):
    print("Interacion: ", i)


tabla = int(input("Ingrese el numero para generar tabla: "))
print(f"Tabla del {tabla}")
for i in range(1, 11):
   print(f"{i} x {tabla} = {tabla * i}")
   
#while - indefinidoc (condicional). se usa en menus o casa de usuario
respuesta = None 

capcha = "8U&r"

print(f"capcha: {capcha}")
while respuesta != capcha:
    print("Ingresa tu respuesta para continuar: ")
    respuesta = input()
    if respuesta != capcha:
        print("Error. Intentalo de nuevo")
    else:
        print("Correcto")