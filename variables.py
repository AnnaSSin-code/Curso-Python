#Asignacion de valores
#Declaracion de valores
#int / numero entero
numero = 10

#float / Decimal
float = 13.14

#character / caracter
character = "$"

#string / cadena de caracteres
cadena = "hola como estas, yo muy bien. ¿Y tu?"

numeros = "numeros jaja" 

#mal uso de identificadores
#Contraintuitivo
palabra = 123
#x no nos dice nada sobre que representa la variable
x = "hola mundo"

#no se recomienda abreviar, cero motivos para abreviar

#mostrar los resultados
print(x)
print (f"Esto es un entero: {numero}")
print(f"Esto es un decimal: {float}")
print(f"Esto es un caracter: {character}")
print(f"Esto es una cadena de caracteres (string): {cadena}")

#Reasignacion de valor
numero = 13345
print (f"Nuevo valor de la variable numero: {numero}")

#Nacio aquí?
cuenta_bancaria = 20000.99
retiro = 100
saldo_despues_retiro = cuenta_bancaria - retiro

print(f"saldo en la cuenta: {cuenta_bancaria}")
print(f"Saldo despues del retiro: {saldo_despues_retiro}")

#cambiando el valor de la variable
cuenta_bancaria = saldo_despues_retiro
print(f"saldo actual: {cuenta_bancaria}")