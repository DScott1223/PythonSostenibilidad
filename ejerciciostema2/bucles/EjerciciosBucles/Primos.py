'''Solicita al usuario un número entero positivo y comprueba si es primo. Usa un bucle while
para verificar si tiene divisores y muestra el resultado. Valida la entrada con try-except.'''

# try:
#     a= (int(input("introduce un numero: ")))
#
#     dividores = 0
#     for numero in range(1,a+1):
#         if a % numero == 0:
#             dividores = dividores + 1
#     if dividores == 2:
#         print("el numero es primo")
#     else:
#         print("el numero no es primo")
# except ValueError:
#     print("Argumentos invalidos")


'''Ejercicio 5: Números primos hasta N
Solicita al usuario un número entero positivo N y muestra todos los números primos desde 2
hasta N. Usa un bucle for para recorrer los números y otro bucle while para verificar si son
primos. Maneja errores si el usuario introduce un valor no válido.'''

try:
    N = int(input("Introduce un número entero positivo: "))

    if N < 2:
        print("No hay números primos en ese rango.")
    else:
        for numero in range(2, N + 1):
            divisor = 2
            es_primo = True

            while divisor < numero:
                if numero % divisor == 0:
                    es_primo = False
                    break
                divisor += 1

            if es_primo:
                print(numero)

except ValueError:
    print("Argumentos inválidos")
