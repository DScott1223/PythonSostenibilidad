'''Realizar un ejercicio que conste de ordenar una lista en función de una clave'''
cars = ['Ford', 'BMW', 'Volvo']
# cars.sort(reverse=True) # False ['Volvo', 'Ford', 'BMW'] True ['Volvo', 'Ford', 'BMW']




''' --------------- Ordenar por promedios--------------'''
#Dada una lista de números ordénalos por el número más cercano el promedio de la lista
numeros = [10, 20, 30, 40]

def premedio(n):
    return sum(n) / len(n)

promedio = sum(numeros) / len(numeros)

def diferencia_promedios(n):
    return abs(n - promedio)


print("la lista de los números ", numeros)
print("El promedio es: ", premedio(numeros))


numeros.sort(key=diferencia_promedios)
print(numeros)

'''EjERCICIO Jaime: Ordenar la lista de estudiantes por la nota'''
print("\nEjercicio Jaime")
estudiantes = [
    ["Ana", 22, 8.5],
    ["Luis", 20, 7.0],
    ["Marta", 21, 9.2],
    ["Carlos", 23, 6.8]
]

def clave_nota(estudiante):
    return estudiante[2]

estudiantes.sort(key=clave_nota)

print(estudiantes)
