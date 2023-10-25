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

def cantidad_por_apellido(personas):
    diccionario_apellidos = dict()
    for p in personas.values():
        if p.apellido in diccionario_apellidos:
            diccionario_apellidos[p.apellido] += 1
            continue
        diccionario_apellidos[p.apellido] = 1
    return diccionario_apellidos

def main():
    personas = leer_archivo("personas.csv")
    personas_mayores_edad = len(list(filter(lambda persona: persona.esMayor(), personas.values())))
    apellidos_con_vocal= list(filter(lambda p: p.apellidoConVocal(), personas.values()))
    personas_vocal = list(map(lambda p: f"{p.nombre} {p.apellido}", apellidos_con_vocal))
    print(f"Cantidad de personas: {len(personas)}")
    print(f"Cantidad de personas: {personas_mayores_edad}")
    print("Listado de nombres y apellidos de aquellas personas cuyo apellido empiece con vocal:")
    for nombre_completo in personas_vocal:
        print(nombre_completo)
    diccionario_apellidos = cantidad_por_apellido(personas)
    for persona, cantidad in diccionario_apellidos.items():
        print(f"{persona}: {cantidad}")


if __name__ == "__main__":
    main()