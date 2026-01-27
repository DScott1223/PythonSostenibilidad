import math


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

# print(calcular_estadisticas(numeros))

'''Ejercicio 2: Crea una función distancia(p1, p2) que reciba dos tuplas representando
puntos en el plano (x, y) y devuelva la distancia entre ellos usando la fórmula:'''

def distancia(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


punto1 = (4, 7)
punto2 = (9, -11)

# print(distancia(punto1, punto2))


'''Ejercicio 3: Crea una función analizar_texto(texto) que devuelva una tupla con:
● Número total de caracteres.
● Número de palabras.
● Primera palabra del texto.
'''
def analizar_texto(texto):
    texto = texto.lower()
    totalCaracteres = len(texto)
    totalPalabras = 0
    primeraPalabra = ""
    cadenaSplit = texto.split()
    for palabra in cadenaSplit:
        totalPalabras += 1
        primeraPalabra += palabra
        break
    return (totalCaracteres,totalPalabras,primeraPalabra)

resultado = analizar_texto("Lorem ipsum dolor sit amet consectetur adipiscing elit arcu at")
# print(resultado)


'''Ejercicio 5: Crea una función analizar_numeros(numeros) que reciba una lista de
enteros y devuelva una tupla con:
● El número de elementos pares.
● El número de elementos impares.
● La suma total.'''
def analizar_numeros(numeros):
    sumaTotal = 0
    pares = 0
    inpares = 0
    for numero in numeros:
        sumaTotal += numero
        if numero % 2 == 0:
            pares += 1
        else:
            inpares += 1
    return (pares, inpares, inpares)
res = analizar_numeros(numeros)
print("Cantidad pares "+str(res[0]))
print("Cantidad inpares "+str(res[1]))
print("Suma total "+ str(res[2]))