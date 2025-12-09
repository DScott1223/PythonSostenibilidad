'''Ordenar 5 números ordenados con un bucle for'''
# try:
#     print("Introduce 5 números")
#     lista = []
#     for n in range( 5):
#         x = int(input())
#         lista.append(x)
#     lista.sort()
#     print(lista)
# except ValueError:
#     print("ingresa numeros validos para el programa")


    # Realizar un programa que te pida una numero de filas e imprimir una piramide de asteriscos
try:
    filas = int(input("Introduce un número de filas: "))

    for i in range(1, filas + 1):
        espacios = " " * (filas - i)
        asteriscos = "*" * (2 * i - 1)
        print(espacios + asteriscos)

except ValueError:
    print("Ingresa un número válido para el programa")
