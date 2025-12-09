'''Ejercicio 1: Verificación de número primo con control
de errores'''

# try:
#     entrada = (input("Ingrese un numero entero y positivo: "))
#     entrada = float(entrada)
#     if entrada <= 0 or not entrada.is_integer():
#         raise ValueError("El numero ingresado no es un entero")
#
#     numero = int(entrada)
#     i = 2
#
#     while i < entrada:
#         if entrada % i == 0:
#             print("El número no es primo")
#             break
#         i = i + 1
#     else:
#         print("El numero es primo, porque es divisible entre 1 y ", i)
# except ValueError:
#     print("Argumento invalido")


'''Ejercicio 2: Conversor de divisas con control de errores
Crea un programa que convierta una cantidad en euros a otra divisa (USD, GBP o JPY). El
usuario debe introducir:
- La cantidad en euros.
- La divisa destino.
El programa debe:
- Validar que la cantidad sea un número positivo.
- Validar que la divisa esté entre las permitidas.
- Manejar excepciones si el usuario introduce datos incorrectos.
'''
# try:
#     euros = float(input("Ingrese la cantidad en euros a cambiar: "))
#     if euros <= 0 or not euros.is_integer():
#         raise ValueError("El usuario introduce datos incorrectos")
#     euros = int(euros)
#     destino = str(input("Ingrese la divisa destino a cambiar: \nUSD, GBP o JPY: "))
#     destino = destino.upper()
#     if destino.upper() == "USD":
#         total = float(euros*1.17)
#         print(total)
#     elif destino.upper() == "GBP":
#         total = float(euros)*0.87
#         print(total)
#     elif destino.upper() == "JPY":
#         total = float(euros*176.06)
#         print(total)
#     else:
#         raise ValueError("El usuario introdujo moneda incorrecta")
# except ValueError:
#     print("El usuario introdujo argumentos incorrectos")


