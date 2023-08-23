def validar_carga(min, max, msj):
    n = min - 1
    while n < min or n > max:
        n = int(input(msj))

        if n < min or n > max:
            print("Intente nuevamente...\n")
    return n


def cargar_surtidores():
    surtidores = []
    for i in range(10):
        n_surtidor = validar_carga(1, 30, "Cargue número de surtidor: ")
        cantidad_l = validar_carga(0, 9000, "Cargue número de litros: ")
        tipo = validar_carga(1, 3, "Cargue tipo de combustible: ")
        print("\n")
        surtidores.append([n_surtidor, cantidad_l, tipo])
    return surtidores

def menor_entre(min,num):
    if num < min:
        return True
    return False

def imprimeCantVendida(total_l):
    print("Total de litros vendidos Nafta Super: ", total_l[0])
    print("Total de litros vendidos Nafta Especial: ", total_l[1])
    print("Total de litros vendidos Gas Oil: ", total_l[2], "\n")

def imprimeMin(surtidor, cant):
    print("La venta minima la realizo el surtidor", surtidor, "con", cant,"litros")

def imprimePromedio(total):
    print("El promedio por surtidor fue: ", suma(total)/10)

def suma(lista):
    sum = 0
    for i in lista:
        sum += i
    return sum

def main():
    surtidores = cargar_surtidores()

    total_l = [0, 0, 0]
    min = 10000
    i_min = None

    for surtidor in surtidores:
        total_l[surtidor[2]-1] += surtidor[1]
        if menor_entre(min, surtidor[1]):
            min = surtidor[1]
            i_min = surtidor[0]
        
    imprimeCantVendida(total_l)
    imprimeMin(i_min, min)
    imprimePromedio(total_l)
    

main()