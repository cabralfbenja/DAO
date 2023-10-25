def leer_numeros():
    archivo = open("numeros.txt", "r")
    numeros = []
    for numero in archivo.readlines():
        numeros.append(int(numero))

    archivo.close()
    return numeros

def promedio(lista):
    suma = 0
    for num in lista:
        suma += num
    return suma / len(lista)

def es_mayor(a, b):
    return a > b

def cant_num_mayor_avg(lista, avg):
    count = 0
    for num in lista:
        if es_mayor(num, avg):
            count +=1
    return count

def es_par(num):
    return (num%2) == 0

def generar_lista_pares(lista):
    pares = []
    for num in lista:
        if es_par(num):
            pares.append(num)
    return pares




def main():
    numeros = leer_numeros()
    avg = promedio(numeros)
    cant_num_mayor= cant_num_mayor_avg(numeros, avg)
    lista_pares = generar_lista_pares(numeros)

    print("El promedio de los numeros es:", round(avg,2))
    print("La cantidad de números mayores al promedio es:", cant_num_mayor)
    print("El listado de pares es el siguiente:", lista_pares)

if __name__=="__main__":
    main()