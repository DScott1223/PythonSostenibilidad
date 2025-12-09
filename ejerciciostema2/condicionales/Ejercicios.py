'''Pide al usuario que introduzca su edad. Valida que sea un número entero positivo. Si la edad
es mayor o igual a 18, muestra un mensaje indicando que es mayor de edad. Si no, indica que
es menor de edad. '''

# try:
#     edad = int(input("ingrese su edad: "))
#     if edad >= 18:
#         print("Eres mayor de edad")
#     else:
#         print("Eres menor de edad")
# except ValueError:
#     print("ingresa argumentos validos para el programa")
# except Exception as e:
#     print(e)

'''Solicita al usuario dos números enteros. Muestra cuál es mayor, cuál es menor o si son
iguales.'''

# try:
#     numeroA = int(input("ingrese su numero: "))
#     numeroB = int(input("ingrese su numero: "))
#     if numeroA == numeroB:
#         print(str(numeroA) + " es igual a " + str(numeroB))
#     elif numeroA < numeroB:
#         print(str(numeroA) + " es el número menor y " + str(numeroB)+ " el número mayor")
#     else:
#         print((str(numeroB) + " es el número menor y " + str(numeroA)+ " el número mayor"))
# except ValueError:
#     print("ingresa argumentos validos para el programa")


'''Pide al usuario una nota numérica entre 0 y 10. Valida que sea un número decimal dentro
del rango. Clasifica la nota como:Suspenso (0-4.9) Aprobado(5-6.9)
Notable (7-8.9)
Sobresaliente (9-10)
'''
'''
try:
    nota = float(input("Ingrese la nota: "))
    if 0 <= nota <= 10:
        if 0 <= nota <= 4.9:
            print("Suspenso")
        elif 5 <= nota <= 6.9:
            print("Aprobado")
        elif 7 <= nota <= 8.9:
            print("Notable")
        elif 9 <= nota <= 10:
            print("Sobresaliente")
    else:
        print("Nota inválida")
except ValueError:
    print("Error: Debes ingresar un número válido")'''

'''Pide al usuario que introduzca una clave. Si la clave coincide con "python123", muestra un
mensaje de acceso concedido. Si no, muestra acceso denegado.'''

# try:
#     cadena = str(input("Ingrese la clave: "))
#     if cadena.lower() ==  "python123":
#         print("Acceso concedido")
#     else:
#         print("Acceso denegado")
# except ValueError:
#     print("solo se permite cadenas en este programa")
# except Exception as e:
#     print(e.message)

'''Ejer5: Muestra un menú con tres opciones:
1. Ver perfil
2. Editar perfil
3. Salir
Pide al usuario que introduzca el número de la opción. Muestra un mensaje según la opción
elegida. Si introduce un valor no válido, muestra un mensaje de error.
'''
# try:
#     print("\t1. Ver perfil \n\t2. Editar perfil \n\t3. Salir")
#     opcionUser = float(input());
#     if opcionUser == 1:
#         print("Ver perfil")
#     elif opcionUser == 2:
#         print("Editar perfil")
#     elif opcionUser == 3:
#         print("Salir")
#     else:
#         print("Número invalido")
# except ValueError:
#     print("Error: ", "Valor invalido")
# except Exception as e:
#     print("Error: ", e)

'''Ejercicio 6: Validación de número par o impar
Solicita al usuario un número entero. Valida que sea correcto. Muestra si el número es par o
impar.'''

# try:
#     valorUser = float(input("Ingrese un número: "));
#     if valorUser % 2 == 0:
#         print("Número par");
#     else:
#         print("Número impar");
# except ValueError:
#     print("Error de argumento");


'''Ejercicio 7: Verificación de permisos para conducir según edad
Solicita al usuario su edad. Según la edad, muestra qué tipo de vehículo puede conducir:
- Menor de 14: no puede conducir
- 14 o más: moto de poca cilindrada
- 16 o más: moto de gran cilindrada
- 18 o más: coche'''

try:
    edad = int(input("Ingrese la edad: "))
    if edad >= 14 and edad < 16:
        print("Moto de poca cilindrada")
    elif edad >= 16 and edad < 18:
        print("Moto de gran cilindrada")
    elif edad >= 18:
        print("Coche")
    else:
        print("No puede conducir")
except ValueError:
    print("Argumento invalido")
