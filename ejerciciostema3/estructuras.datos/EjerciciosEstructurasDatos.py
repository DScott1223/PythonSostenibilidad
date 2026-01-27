'''Realiza un programa que siga las siguientes instrucciones:

Crea un conjunto llamado usuarios con los usuarios Marta, David, Elvira, Juan y Marcos
Crea un conjunto llamado administradores con los administradores Juan y Marta.
Borra al administrador Juan del conjunto de administradores.
Añade a Marcos como un nuevo administrador, pero no lo borres del conjunto de usuarios.
Muestra todos los usuarios por pantalla de forma dinámica, además debes indicar cada usuario es administrador o no.'''

# usuarios= ("Marta", "David", "Elvira", "Juan", "Marcos")
# administradores = ["Juan", "Marta"]
# print(usuarios, administradores)
# administradores.remove("Juan")
# administradores.append(usuarios.__getitem__(1))
# # print(administradores)
# for nombre in usuarios:
#     if nombre in administradores:
#         print("Admin ",nombre)
#     else:
#         print(nombre)

'''Aprende con Alf. Ejercicio 2 
Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. 
Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.'''
def ejer2(nombre, edad, telfono, direccion):
    diccionario = {"nombre" : nombre, "edad" : edad, "telfono" : telfono, "direccion":direccion}
    return print(diccionario["nombre"]+" tiene " +diccionario["edad"] + " años y vive en "+diccionario["direccion"]
                 + " y su número de telefno es "+diccionario["telfono"])

# print(ejer2("Carlos","12", "147719256", "Calle Mayor"))

'''Aprende con Alf:Ejercicio 3
Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al 
usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. 
Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.'''

def ejer3(fruta, kilos):
    diccionario = {"Platano" : 1.35, "Manzana" : 0.80, "Pera" : 0.85, "Naranja": 0.70}
    fruta = fruta.capitalize()
    kilos = float(kilos)
    if fruta not in diccionario:
        salida = "La fruta no esta en el diccionario"
    else:
        salida = diccionario[fruta] * kilos
    return salida

# print(ejer3("Platano", 2))
# print(ejer3("manzana", 4))
# print(ejer3("pera", 4))
# print(ejer3("Naranja", 3.5))

'''Aprende con alf: Ejercicio 5
Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso
 {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura en el 
 formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos. 
Al final debe mostrar también el número total de créditos del curso.'''

def ejer5():
    asignaturas = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
    creditosTot = 0
    for asignatura in asignaturas:
        creditosTot += asignaturas[asignatura]
        print(asignatura +" tiene: "+str(asignaturas[asignatura]) +" créditos")
    return ("Creditos totales: "+ str(creditosTot))

print(ejer5())

''' '''