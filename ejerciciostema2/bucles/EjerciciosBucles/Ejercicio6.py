try:
    n = int(input("ingrese cantidad de alumnos en el grupo: "))
    notas = []

    for i in range(n):
        nota = float(input(f"Ingrese la nota del alumno {i + 1}: "))
        if nota < 0 or nota > 10:
            raise ValueError("Las notas deben estar entre 0 y 10.")
        notas.append(nota)

    aprobados = 0
    for nota in notas:
        if nota >= 5:
            aprobados += 1

    media = sum(notas) / len(notas)

    nota_max = max(notas)
    nota_min = min(notas)

    print("Notas ingresadas: ", notas)
    print("Alumnos aprobados : ", aprobados)
    print("Nota media del grupo: ", round(media, 3)) #2 por la cantidad de decimales
    print("Nota más alta: ", nota_max)
    print("Nota más baja: ", nota_min)

except ValueError:
    print("Error: Argumentos invalidos.")
except Exception as e:
    print("Ha ocurrido un error inesperado:", e)
