"""
Del archivo numeros.txt que contiene un número entero por cada línea, generar un conjunto 
que contenga todos los números del archivo y desde el conjunto calcular e informar:

Cantidad de números no repetidos
Suma de todos los números
Cantidad de impares
Promedio de pares
"""

def leer_numeros():
    archivo = open("numeros.txt")
    numeros = set()
    for numero in archivo.readlines():
        numeros.add(int(numero))

    archivo.close()
    return numeros

def promedio(numeros):
    return round(sum(numeros) / len(numeros), 2)

def main():
    numeros = leer_numeros()
    impares = {x for x in numeros if x%2==1}
    pares = {x for x in numeros if x%2==0}
    promedio_pares = promedio(pares)
    
    
    
    print("Cantidad de números no repetidos:", len(numeros))
    print("Suma de todos los números:", sum(numeros))
    print("Cantidad de impares:", len(impares))
    print("Promedio de pares:", promedio_pares)

if __name__ == "__main__":
    main()