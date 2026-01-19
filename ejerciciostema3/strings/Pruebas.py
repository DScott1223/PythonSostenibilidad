import itertools
import string
import time
from tokenize import String


def fuerza_bruta(password):
    caracteres = string.ascii_lowercase + string.digits  # letras minúsculas + números
    inicio = time.time()

    # Generar combinaciones de longitud 1 hasta la longitud de la contraseña
    for longitud in range(1, len(password) + 1):
        for intento in itertools.product(caracteres, repeat=longitud):
            intento = ''.join(intento)
            if intento == password:
                fin = time.time()
                print(f"Contraseña encontrada: {intento}")
                print(f"Tiempo: {fin - inicio:.4f} segundos")
                return


# Ejemplo de uso
# fuerza_bruta("abc")

'''Ejercicio(Oscar Pérez): Crea una función que al pasar le una frase cuente el numero de vocales que tiene 
en total y  que pregunte por que otra vocal quiere cambiar todas las vocales de la frase, que retorne
 la frase cambiada y el numero de vocales de la frase antes de cambiarlas.'''


def funcionOscar(frase):
    cantidadVocales = 0
    vocales = ["a", "e", "i", "o", "u"]
    frase = frase.lower()
    for x in frase:
        if x in vocales:
            cantidadVocales += 1

    salida = (f"Cantidad de vocales: {cantidadVocales}")

    vocal = input(("Por qué vocal quieres cambiar todas las vocales:  "))
    for x in frase:
        if x in vocal:
            frase.replace("a", vocal)
            frase.replace("e", vocal)
            frase.replace("i", vocal)
            frase.replace("o", vocal)
            frase.replace("u", vocal)

    salida = (f"Cantidad de vocales: {cantidadVocales}\nFrase cambiada: {frase}")
    return salida


# print(funcionOscar("Va a tener que ser esta tarde"))

def ejercicioIvanPenia(cadena):
    cadena = cadena.lower()
    cadenaSplit = cadena.split()
    maximaLongitud = 0
    cadenaNueva = ""
    contadorLetraFinal = 0
    for x in cadenaSplit:
        if len(x) > maximaLongitud:
            maximaLongitud = len(x)
            palabraLongitud = x
        if(len(x) % 2 == 0):
            cadenaNueva += " "+x
        else:
            cadenaNueva += " "+x[::-1]
    for x in cadena:
        if cadena[-1:] == x:
            contadorLetraFinal += 1
    return ("Frase original: " + cadena + "\nLa palabra más larga encontrada: " + palabraLongitud +
            "\nFrase transformada: " + cadenaNueva + "\nApariciones última letra: " + str(contadorLetraFinal))


print(ejercicioIvanPenia("palabra tener cierra palabraGrande"))