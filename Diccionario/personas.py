"""
El archivo personas.csv contiene un padrón de personas a razón de una persona 
por línea y en cada una separadas con comas el documento, nombre, apellido y edad.

Desarrollar un programa en python que lea el archivo y guarde todo su contenido 
en un diccionario indexado por documento. Luego el programa debe ofrecer un menú 
con las siguientes opciones:

Búsqueda por documento: que solicite un documento y si lo encuentra muestre todos 
los datos de la persona encontrada y un mensaje adecuado si no la encuentra.

Búsqueda por apellido: que solicite un apellido y muestre por pantalla todos 
los datos de todas las personas cuyo apellido sea igual al ingresado.

Mostrar el promedio de edades de todos.
"""
def menu():
    print("Bienvenido... Elija la opcion que desee:")
    print("1) Busqueda por documento")
    print("2) Busqueda por apellido")
    print("3) MOstrar promedios")
    print("4) Salir")
    opcion = int(input("Opcion:"))
    return opcion

def leer_archivo(f):
    archivo = open(f)
    diccionario = dict()
    for linea in archivo.readlines():
        items = linea.strip().split(",")
        diccionario[items[0]] = items[1:5]
    return diccionario


def busqueda_por_dni(personas):
    dni = input("Ingrese un dni:")
    print(personas[dni]) 

def main():
    opcion = 0
    personas = leer_archivo("personas.csv")
    
    while opcion != 4:
        opcion = menu()
        
        if opcion == 1:
            busqueda_por_dni(personas)
        elif opcion == 2:
            busqueda_por_apellido(personas)
        elif opcion == 3:
            mostrar_promedio(personas)
        elif opcion == 4:
            print("BYE BYE...")
        else:
            print("Opcion no valida...")
        print()

if __name__ == "__main__":
    main()