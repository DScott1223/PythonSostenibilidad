opcion = int(input("Selecciona el ejercicio (1 o 2): "))

match opcion:
    case 1:
        # Ejercicio 1
        '''Escribe un programa que abra un fichero de texto llamado datos.txt, 
        lea todo su contenido y lo muestre por pantalla.'''
        with open("datos.txt", "r") as f:
            print(f.read())

    case 2:
        # Ejercicio 2
        '''Escribe un programa que abra un fichero datos.txt y cuente cuántas líneas tiene el archivo.'''
        with open("datos.txt", "r") as fichero:
            numLineas = fichero.readlines()
            print("Contenido por líneas:")
            print(numLineas)
            print("Número de líneas:", len(numLineas))


    case 3:
        '''Ejercicio 3: Crea un programa que lea el fichero datos.txt y cuente cuántas veces aparece una 
        palabra específica que el usuario introduce.'''

    case _:
        print("Opción no válida")

