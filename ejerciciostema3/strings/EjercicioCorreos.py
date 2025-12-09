''' Ejercicio 1 (Diego Scott): Crea un método:  correos_nombres(lista_correos)
que con los correos de la lista de correos genere dos listas, una con los nombres y
otras con los dominios de todos los correos e imprimirlos'''

correos = ["diego@gmail.com", "maria@yahoo.es", "juan@outlook.com", "infanta@elena.es", "galapagar@alcaldia.org"]
nombres = []
dominios = []

def correos_nombres(lista_correos=correos):
    salida = ""
    for correo in correos:
        pos = correo.find("@")
        if pos != -1:
            nombres.append(correo[:pos])
            dominios.append(correo[pos + 1:])
        else:
            salida = "No existen correos validos"
            return salida
    salida = nombres + dominios;
    return salida

print(correos_nombres(correos))
