def ingresarApellido():
    apellido = input("Ingrese el apellido a buscar: ")
    return apellido

def main():
    apellido = input("Ingrese el apellido a buscar: ")
    archivo = open("personas.txt", "r")
    nombre, edad = [], []
    for linea in archivo.readlines():
        datos = linea.strip().split(",")
        if datos[2] == apellido.upper():
            nombre.append(datos[1])
            edad.append(datos[3])
    
    if len(nombre)>0:
        for i in range(len(nombre)):
            print("Nombre:", nombre[i])
            print("Edad:", edad[i])
    else:
        print("No se encontro...")
main()