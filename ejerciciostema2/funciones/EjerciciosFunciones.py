'''Vuelva a escribir su cálculo de pago con tiempo y medio para las horas extra y cree
una función llamada Computepay que toma dos parámetros (horas y tarifa).'''
try:
    def computepay(horas, tarifa):
        if horas > 40:
            horasExtras = horas - 40
            horas = horas - horasExtras
            pagaNormal = horas * tarifa
            pagaExtra = float(horasExtras * (tarifa * 1.5))
            return pagaNormal + pagaExtra
        else:
            return horas * tarifa
except ValueError:
    print("ingresa números validos para el programa")

'''Pide al usuario una nota numérica entre 0 y 10. Valida que sea un número decimal dentro
del rango. Clasifica la nota como:Suspenso (0-4.9) Aprobado(5-6.9) Notable (7-8.9) Sobresaliente (9-10)'''


def notasExamen(nota):
    try:
        if nota >= 0 and nota <= 10:
            if 0 <= nota <= 4.9:
                return "Suspenso"
            elif 5 <= nota <= 6.9:
                return "Aprobado"
            elif 7 <= nota <= 8.9:
                return "Notable"
            elif 9 <= nota <= 10:
                return "Sobresaliente"
            else:
                return "Nota inválida"
        else:
            return ("Error")
    except ValueError:
        print("ingresa una nota valida")


# print(computepay(45, 10))
# print(notasExamen(9))



#EJERCICIOS HOJA DE EJERCICIOS DE CLASE



'''Ejercicio 1: Saludo personalizado
Crea una función llamada saludar que reciba dos argumentos por palabra clave:
- nombre (str)
- saludo (str), con valor por defecto "Hola"
La función debe devolver una cadena con el saludo seguido del nombre.'''
def saludar(nombre, saludo = "Hola"):
    try:
        return saludo + " " + nombre
    except ValueError:
        print("ingresa argumentos valida")

# print(saludar("Giancarlo", "Buenos dias"))

'''Ejercicio 2: Cálculo de precio con IVA
Crea una función llamada `calcular_precio` que reciba:
- precio_base (float)
- iva (float), como argumento por palabra clave, con valor por defecto 21
La función debe devolver el precio final con el IVA aplicado.
'''

def calcular_precio(precio_base, iva = 0.21):
    try:
        return precio_base * iva
    except ValueError:
        print("ingresa argumentos valida")

# print(calcular_precio(100, iva=1.3))


'''Ejercicio 3: Crear usuario con lista
Crea una función llamada `crear_usuario` que reciba los siguientes argumentos por palabra
clave:
- nombre (str)
- email (str)
- activo (bool), con valor por defecto True
La función debe devolver una lista sólo de los usuarios activos con los datos del usuario en
el orden: [nombre, email, activo].'''
def crear_usuario(*, nombre: str, email: str, activo: bool = True):
    try:
        if not isinstance(nombre, str):
            raise TypeError(nombre, " debe ser una cadena")

        if not isinstance(email, str):
            raise TypeError(email, " debe ser una cadena")

        if not isinstance(activo, bool):
            raise TypeError(activo, " debe ser booleano")

        if "@" not in email:
            raise ValueError("El email debe contener '@'.")

        if activo:
            return [nombre, email, activo]
        else:
            return []
    except Exception as e:
        print(e)

# print(crear_usuario(nombre="", email="", activo=True))

#Ejercicio personal propuesto para clase

'''Crea una función llamada competiciones_nombre que debe recibrir por parametro palabra 
clave el nombre del atleta y listar las competiciones donde este ha estado. Ten en cuenta que un atleta puede no haber competido nunca'''
def competiciones_nombre(nombre, *competiciones):
    try:
        if not isinstance(nombre, str):
            raise TypeError(nombre, " debe ser una cadena")
        if not competiciones:
            competiciones = ("Sin competiciones registradas",)

        return [nombre , "ha competido en: ", *competiciones]
    except Exception as e :
        print("Error: ", e)

print(competiciones_nombre("Darlo", "Nacionales", "Autonómica", "Olimpiadas"))
print(competiciones_nombre("Marco"))

