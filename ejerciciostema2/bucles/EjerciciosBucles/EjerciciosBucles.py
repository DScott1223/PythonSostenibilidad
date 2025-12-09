'''Ejercicio 1: Calculadora de operaciones básicas
Crea un programa que simule una calculadora. El usuario debe introducir dos números y
seleccionar una operación: suma, resta, multiplicación o división. El programa debe
repetirse hasta que el usuario decida salir. Debe manejar errores como división por cero y
entrada de datos no numéricos.'''
try:
    print("*** CALCULADOR DE OPERACIONES ***")
    while True:
        a = (input("Introduce el primer valor o 'salir' para terminar  ")).lower()
        b = (input("Introduce el segundo valor o 'salir' para terminar  ")).lower()
        if a == "salir" or b == "salir":
            print("Saliendo...")
            break
        else:
            a = int(a)
            b = int(b)
            suma = a + b
            resta = a - b
            multiplicacion = a * b

            operacion = input("Introduce la operacion a realizar:\n1: Suma\n2: Restar\n3: Multiplicacion\n4: Dividir\n").lower()
            if operacion == "1" or operacion == "suma":
                print("La suma es: ",suma)
            elif operacion == "2" or operacion == "resta":
                print("La resta es: ",resta)
            elif operacion == "3" or operacion == "multiplicacion":
                print("La multiplicacion es: ",multiplicacion)
            elif operacion == "4" or operacion == "dividir":
                try:
                    print("La dividir es: ",a/b)
                except ZeroDivisionError:
                    print("Error: No se puede dividir entre 0")
            else:
                print("Error: Operacion no valida")
except ValueError:
    print("Invalid arguments")
