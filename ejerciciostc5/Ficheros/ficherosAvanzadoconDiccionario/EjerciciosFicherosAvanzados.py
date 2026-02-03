import csv
from unittest import case
seleccion = 0
while seleccion >= 0:
    seleccion = int(input("ejercicio: "))
    match seleccion:
        case 2:
            try:
                with open("datos.csv") as f:
                    lector = csv.reader(f);
                    numFilas = 0
                    for row in lector:
                        numFilas += 1
                        print(row)
                    print("numero de filas: " + str(numFilas))
            except FileNotFoundError:
                print("El fichero 'datos.txt' no existe")
        case 3:
            try:
                with open("datos.csv") as f:
                    lector = csv.DictReader(f)
                    datos = list(lector)
                    for person in datos:
                        print(f"Nombre: {person['nombre']}, Edad: {person['edad']}")
            except FileNotFoundError:
                print("El fichero 'datos.csv' no existe")

        case 4:
            try:
                with open("datos.csv", 'a') as f:
                    escritor = csv.writer(f)
                    escritor.writerow(['Marta', 'Malone Richards', '46803579O','644678901,36'])
            except FileNotFoundError:
                print("El fichero 'datos.csv' no existe")
        case 4.5:
            nueva_persona = {
                'nombre': 'Juan',
                'apellidos': 'Pérez González',
                'dni': '99887766Z',
                'telefono': '611223344',
                'edad': '41'  # Nota: DictWriter espera strings, no integers
            }
            try:
                with open("datos.csv", 'a') as f:
                    escritor = csv.DictWriter(f, fieldnames=['nombre', 'edad'])
                    escritor.writeheader()
                    escritor.writerows(nueva_persona)
            except FileNotFoundError:
                print("El fichero 'datos.csv' no existe")
        case _:
            print("Opción no válida")
print("Programa terminado")