import math
import random


def calcular_precio(precio_base, iva=0.21):
    try:
        return precio_base * iva
    except ValueError:
        print("ingresa argumentos valida")


def saludar(nombre, saludo="Hola"):
    try:
        return saludo + " " + nombre
    except ValueError:
        print("ingresa argumentos valida")


'''Función llamada make_pizza(tamanio,*ingredientes) 
donde elegimos cantidad de porciones y los ingredientes'''


def make_pizza(tamanio, *ingredientes):
    res = ""
    try:
        if len(ingredientes) == 0:
            res = "No hay ingredientes, no hay pizza, espabilla xicx"
        elif len(ingredientes) >= 1:
            res = "Pizza de ", tamanio, " porciones y de ingredientes", ingredientes
        return res
    except ValueError:
        print("ingresa argumentos validos")


'''Función ganador con lista de participantes y aleatoriamente se elige el ganador'''


def ganador(*participantes):
    try:
        if len(participantes) == 0:
            raise TypeError("No hay participantes")
        elif len(participantes) >= 1:
            return random.choice(participantes)
    except Exception as e:
        print(e)


'''Función factorial'''


def factorialClase(n):
    try:
        n = int(n)
        if n == 0:
            return 1
        else:
            return n * factorialClase(n - 1)
    except Exception as e:
        print(e)


'''Fibonacci con recursividad'''
def fibonacci(n):
    try:
        if n < 0:
            raise ValueError("El número debe ser positivo")
        elif n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)
    except Exception as e:
        print("Error:", e)


# Ejemplo de uso
num = int(input("Ingrese la posición de la serie Fibonacci: "))
print(f"El número Fibonacci en la posición {num} es: {fibonacci(num)}")



'''Modulos de funciones'''
def modulosGeometricos(opcion):
    try:
        match opcion:
            case 1:
                r = int(input(("Ingresa el radio ")))
                return (areaCirculo(r))
            case 2:
                l = input(int("Ingresa el lado "))
                return (areaCuadrado(l))
            case 3:
                b = input(int("Ingresa la base "))
                h = input(int("Ingresa la altura "))
                return (areaTriangulo(b, h))
    except Exception as e:
        print(e)


def areaCirculo(radius=8):
    try:
        if radius <= 0:
            raise TypeError("Radio no valida")
        else:
            return math.pi * (radius ** 2)
    except Exception as e:
        print(e)


def areaCuadrado(l=8):
    try:
        if l <= 0:
            raise TypeError("Lado no valida")
        else:
            return (l ** 2)
    except Exception as e:
        print(e)


def areaTriangulo(base=8, high=8):
    try:
        if base <= 0:
            raise TypeError("Base no valida")
        elif high <= 0:
            raise TypeError("altura no valida")
        else:
            return (base * high) / 2
    except Exception as e:
        print(e)
