"""
Programar una clase Persona con atributos suficientes para almacenar documento, nombre,
apellido y edad de una persona.
Crear un programa que lea el archivo personas.csv, cree una instancia de Persona
por cada línea del archivo y guarde todas las instancias en un diccionario indexado por documento.
A continuación, desde el diccionario informe:

Cantidad de personas cargadas
Cantidad de personas mayores de edad
Listado de nombres y apellidos de aquellas personas cuyo apellido empiece en vocal
Cantidad de personas por cada apellido
"""
from Persona import Persona
def leer_archivo(f):
    archivo = open(f)
    diccionario = dict()
    for linea in archivo.readlines():
        items = linea.strip().split(",")
        persona = Persona(items[0], items[1], items[2], items[3])
        diccionario[persona.documento] = persona
    archivo.close()
    return diccionario

def main():
    personas = leer_archivo("personas.csv")
    personas_mayores_edad = len(list(filter(lambda persona: persona.esMayor(), personas.values())))
    personas_con_vocal = list(filter(lambda p: p.nombreConVocal(), personas.values()))
    personas_con_vocal = list(filter(lambda p: p.apellidoConVocal(), personas.values()))
    print(f"Cantidad de personas: {len(personas)}")
    print(f"Cantidad de personas: {personas_mayores_edad}")
    print("Listado de nombres con vocal:")
    print(nombres_con_vocal)
    print("Listado de apellidos con vocal:")
    print(apellidos_con_vocal)
    


if __name__ == "__main__":
    main()