"""
Tomando el texto del libro "El Quijote de La Mancha" y el diccionario 
del idioma inglés calcular e informar

Cantidad de palabras únicas (sin repetición) del libro.
Cantidad de palabras del diccionario.
Cantidad de palabras del libro que no existen en el diccionario.
Listado ordenados de todas las palabras que no existen.
"""
import re


def leer_archivo(f):
    archivo = open(f)
    palabras = set()
    for linea in archivo.readlines():
        limpia = re.sub("[^a-zA-Z]", " ", linea)
        palabras.update(limpia.lower().split())
    
    return palabras

def main():
    diccionario = leer_archivo("words_alpha.txt")
    quijote = leer_archivo("Quijote.txt")
    
    palabras_unicas = sorted(quijote.difference(diccionario))
    
    print("Cantidad de palabras únicas (sin repetición) del libro:", len(quijote))
    print("Cantidad de palabras del diccionario:", len(diccionario))
    print("Cantidad de palabras del libro que no existen en el diccionario:", len(palabras_unicas))
    print("Listado ordenado de palabras ùnicas...")
    for i, item in enumerate(palabras_unicas):
        if i == 5:
            break
        print(item)

if __name__ == "__main__":
    main()