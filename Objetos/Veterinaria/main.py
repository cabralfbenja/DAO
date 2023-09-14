"""
Una Veterinaria encargada del cuidado de mascotas ha solicitado la
realización de un software para obtener resultados sobre sus clientes y sus
respectivas mascotas. (Suponer que cada cliente posee una sola mascota)
Se sabe que cada Cliente de esta veterinaria tiene: un numero de cliente, un
nombre, una antigüedad (hace cuántos años que son clientes de la veterinaria) y una
Mascota.
De la Mascota se dispone los siguientes datos: el nombre y la edad.
El software requiere cargar por teclado los datos de varios clientes y almacenarlos en alguna colección adecuada.
Se pide:

Mostrar la cantidad de clientes.
Mostrar el promedio de edad de las mascotas.
Informar cuántos clientes tienen una antigüedad mayor igual a 5 años.
Listado de los datos de todos los clientes cuya mascota tiene más de 5 años de edad.
"""
from Mascota import Mascota
from Cliente import Cliente


def ingresoENTRE(a, b, msj):
    variable = int(input(msj))
    while variable > a or variable < b:
        print("Intente nuevamente...")
        variable = int(input(msj))
    return variable

def ingresar_datos():
    id = ingresoENTRE(99999999, 0, "Ingrese ID: ")
    nombre = input("Ingrese un nombre: ")
    ant = ingresoENTRE(100, 0, "Ingrese antiguedad: ")
    nombre_mascota = input("Ingrese nombre de la mascota: ")
    edad_mascota = int(input("Ingrese edad de la mascota: "))
    mascota = Mascota(nombre_mascota, edad_mascota)
    return Cliente(id, nombre, ant, mascota)
# TODO: corregir para que no puedan ingresarse 2 clientes con mismo id

def leer_archivo(f):
    archivo = open(f)
    diccionario = dict()
    for linea in archivo.readlines():
        items = linea.strip().split(",")
        mascota = Mascota(items[3], int(items[4]))
        cliente = Cliente(items[0], items[1], int(items[2]), mascota)
        diccionario[cliente.id] = cliente
    archivo.close()
    return diccionario

def ingresoManual():
    flag = 1
    lista_clientes = {}
    print("Bienvenido... ingrese los clientes...")
    cliente = ingresar_datos()
    lista_clientes[cliente.id] = cliente
    while flag:
        flag = int(input("¿Desea agregar una nueva persona? (0:NO, 1:SI): "))
        if flag:
            cliente = ingresar_datos()
            lista_clientes[cliente.id] = cliente
    return lista_clientes

def main():
    opc = int(input("INGRESE OPCION (0:LECTURA, 1:MANUAL): "))
    if opc:
        lista_clientes = ingresoManual()
    else:
        lista_clientes = leer_archivo("clientes.txt")
    print("Carga completa")
    suma_edad_mascotas = 0
    for cliente in lista_clientes.values():
        suma_edad_mascotas += cliente.getEdadMascota()

    lista_clientes_antiguos = list(filter(lambda c: c.antiguedad >= 5, lista_clientes.values()))
    lista_mascotas_mayores = list(filter(lambda c: c.getEdadMascota()>5, lista_clientes.values()))
    cant_clientes = len(lista_clientes)
    print("La cantidad de clientes es: ", cant_clientes)
    print("El promedio de edad de las mascotas: ", suma_edad_mascotas/ cant_clientes)
    print("Cantidad de clientes que tienen una antigüedad mayor igual a 5 años: ", len(lista_clientes_antiguos))
    print("Estos son los clientes que tienen mascotas con màs de 5 años: ")
    for cliente in lista_mascotas_mayores:
        print(f'\n{cliente}')
    

    
if __name__ == "__main__":
    main()