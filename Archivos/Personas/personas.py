def ingresarApellido():
    apellido = input("Ingrese el apellido a buscar: ")
    return apellido

def main():
    apellido = input("Ingrese el apellido a buscar: ")
    archivo = open("personas.txt", "r")
    nombre, edad = "", 0
    for linea in archivo.readlines():
        datos = linea.strip().split(",")
        if datos[2] == apellido.upper():
            nombre = datos[1]
            edad = datos[3]
    
    if len(nombre)>0:
        print("Nombre:", nombre)
        print("Edad:", edad)
    else:
        print("No se encontro...")
main()