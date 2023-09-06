"""
Generar 1000 números enteros al azar entre -1000000 y 1000000. 
Investigar cómo generar los números con un flujo en lugar de un ciclo for
Informar:

El menor de todos.
La cantidad de pares.
El promedio de los impares.
El cuadrado de todos los que se encuentren entre 10 y 100 sin incluirlos
Los múltiplos de 3 del punto anterior (los multiplos de 3 de los cuadrados calculados)
Todos los múltiplos de 7 ordenados en forma descendente.
El promedio de los impares negativos.
La desviación estandar de todos.
Si existe o no algún múltiplo de 127.
Generar una lista que contenga únicamente los que terminan en 2 o 3.
"""
import random
import math
from functools import reduce

def generar_numeros_aleatorios(cantidad):
    contador = 0
    lista = []
    while contador < cantidad:
        numero = random.randint(-100000, 100000)
        lista.append(numero)
        contador += 1
    return lista

def multiploDe(n):
    return lambda x: x%n == 0

def calcular_desvEst(numeros):
    media = sum(numeros) / len(numeros)

    # Calcular la varianza utilizando una función lambda y map
    varianza = sum(map(lambda x: (x - media) ** 2, numeros)) / len(numeros)

    # Calcular la desviación estándar como la raíz cuadrada de la varianza
    desviacion_estandar = math.sqrt(varianza)
    return desviacion_estandar

def main():
    numeros = generar_numeros_aleatorios(1000)
    imprimir = lambda x: print(x, end=" | ")
    esMinimo = lambda x, y: x if x < y else y
    esPar = lambda x: x%2 == 0
    cuadrado = lambda x: x*x
    entre10y100 = lambda x: x>10 and x<100
    esNegativo = lambda x: x < 0
    
    
    minimo = reduce(esMinimo, numeros)
    pares = list(filter(esPar, numeros))
    numerosEntre10y100 = list(filter(entre10y100, numeros))
    cuadrados = list(map(cuadrado, numerosEntre10y100))
    multiplosDe3 = list(filter(multiploDe(3), cuadrados))
    multiplosDe7 = list(filter(multiploDe(7), numeros))
    m7_ordenados = sorted(multiplosDe7, reverse=True)
    negativos = list(filter(esNegativo, numeros))
    imparesNegativos = list(filter(lambda x: esNegativo(x) and not esPar(x), numeros))
    suma_impares_negativos = reduce(lambda x, y: x + y, imparesNegativos)
    promedio_impares_negativos = suma_impares_negativos / len(imparesNegativos)
    desviacion_estandar = calcular_desvEst(numeros)
    multiplosDe127 = list(filter(multiploDe(127), numeros))
    listaEspecifica = list(filter(lambda x: (x%10 == 2) or (x%10 == 3), numeros))

    print("Generador de números random, operando de manera funcional")
    print("El minimo es: ", minimo)
    print("\nLa cantidad de pares es: ", len(pares))
    
    print("\nEl cuadrado de todos los que se encuentren entre 10 y 100:")
    imprimeCuadrados = list(map(imprimir, cuadrados))
    
    print("\n\nLos múltiplos de 3 del punto anterior:")
    imprimeMultiplosDe3 = list(map(imprimir, multiplosDe3))
    
    print("\n\nTodos los múltiplos de 7 ordenados en forma descendente:")
    imprimirMultiplosDe7 = list(map(imprimir, m7_ordenados))

    print("\n\nEl promedio de los impares negativos:", promedio_impares_negativos)
    print("\n\nLa desviación estandar de todos:", desviacion_estandar)
    if(len(multiplosDe127)):
        print("\nExisten múltiplos de 127")
    else:
        print("\nNo existen múltiplos de 127")
    print("\n\nLista de los que terminan en 2 o 3:")
    imprimirLista = list(map(imprimir, listaEspecifica))
if __name__ == "__main__":
    main()
