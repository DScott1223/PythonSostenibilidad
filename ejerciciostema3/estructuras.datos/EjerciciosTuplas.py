'''Ejercicio 1: Crea una función calcular_estadisticas(numeros) que reciba una lista de
números y devuelva una tupla con:
● El valor mínimo.
● El valor máximo.
● La media aritmética.
'''

def calcular_estadisticas(lista):
    mayor = lista[0]
    menor = lista[0]
    media = 0
    for numero in lista:
        media += numero
        if numero > mayor:
            mayor = numero
        if numero < menor:
            menor = numero
    media = media / len(lista)
    return (mayor, menor, media)


numeros = [1, 0, -4, 6, 21]

print(calcular_estadisticas(numeros))