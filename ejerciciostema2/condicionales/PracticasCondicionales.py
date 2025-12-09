# Ejercicio de calcular la paga de un empleado segun el rate y las horas trabajadas
try:
    inp = input("Ingresa un numero de horas: ")
    a = int(inp)
    inp = input("Ingresa la paga por hora: ")
    rate = float(inp)
    horasExtras = 0
    if a > 40:
        horasExtras = a - 40
        a = 40
        paga = float(rate * a)
        pagaExtras = horasExtras * (rate * 1.5)
        pagaTotal = pagaExtras + paga
        print("La paga por hora es de: ", pagaTotal)
    else:
        print("La paga por hora es de: ", rate * a)

except ValueError:
    print("ingresa numeros validos para el programa")
except Exception as e:
    print(e)