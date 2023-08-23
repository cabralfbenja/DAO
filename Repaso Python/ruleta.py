import random



def es_par(n):
    return ((n % 2) == 0) and (n != 0)

def definir_docena(n):
    return (n-1)//12

def es_cero(n):
    return n == 0

def es_rojo(n):
    rojos = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
    return n in rojos

def pct(a, b):
    return round((a/b)*100, 2)

def main():
    total = 1000
    count_par = 0
    docena = [0, 0, 0]
    count_cero = 0
    count_rojos = 0
    for i in range(total):
        n = random.randint(0, 36)
        if es_cero(n):
            count_cero += 1
            continue
        if es_par(n):
            count_par += 1
        
        if es_rojo(n):
            count_rojos += 1
        docena[definir_docena(n)] += 1
        
    
    print("Cantidad de pares: ", count_par)
    print("Cantidad de impares: ", total - count_par)

    print("Cantidad de tiradas docena 1 (1-12): ", docena[0])
    print("Cantidad de tiradas docena 1 (13-24): ", docena[1])
    print("Cantidad de tiradas docena 1 (25-36): ", docena[2])

    print("Porcentaje de ceros sobre el total de jugadas: ", pct(count_cero, total), "%")
    print("Cantidad de rojos: ", count_rojos)
    print("Cantidad de negros: ", total - count_rojos)

main()