try:
    inversion = int(input("Ingresa cantidad a invertir: "))
    interesAnual = int(input("Ingresa cantidad a interes en decimal: "))
    numeroAnios = int(input("Ingresa cantidad a número de años:  "))

    for n in range(numeroAnios):
        capital = float(inversion * (interesAnual / 100 + 1))
        print(capital)
        inversion = capital
        print(f"El interes que generas el año {n + 1} es de : ", inversion)

except ValueError:
    print("Argumento invalido")
