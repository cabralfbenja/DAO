def ingresarApellido():
    apellido = input("Ingrese el apellido a buscar: ")
    return apellido

def main():
    apellido = input("Ingrese el apellido a buscar: ")
    archivo = open("personas.txt", "r")
    count = 0
    for linea in archivo.readlines():
        datos = linea.strip().split(",")
        if datos[2] == apellido.upper():
            count += 1
            print(count, "| Nombre:", datos[1], "| Edad:", datos[3])
    
main()