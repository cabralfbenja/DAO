"""
Tito el robot
Desarrollar un programa controlado por menú de opciones que permita simular el desplazamiento
de un robot sobre un plano cuyo tamaño es de 400 x 400, y las posiciones válidas se identifican
desde 0 como en un sistema de coordenadas cartesianas.
Inicialmente se genera la posición aleatoria del robot en forma de punto (x,y). Luego se presenta
un menú de opciones que permita los siguientes movimientos:

Opción N: Girar al norte y avanzar 10 pasos
Opción S: Girar al sur y avanzar 20 pasos
Opción E: Girar al este y avanzar 10 pasos
Opción O: Girar al oeste y avanzar 20 pasos
Opcion F: Finalizar

Luego de cada movimiento el programa debe informar la posición del robot.
"""
import random
def menu():
    opc = input("Escoja la opcion deseada(F para terminar): ")
    return opc.lower()

def validar400(n):
    return 400 if n > 400 else n

def validarCero(n):
    return 0 if n < 0 else n

def validarPunto(punto):
    punto[0] = validar400(punto[0])
    punto[0] = validarCero(punto[0])
    punto[1] = validar400(punto[1])
    punto[1] = validarCero(punto[1])
    return punto


def main():
    
    opcion = {
        "n": lambda x,y: [x, y+10],
        "s": lambda x,y: [x, y-20],
        "e": lambda x,y: [x+10, y],
        "o": lambda x,y: [x-20, y]
    }

    punto = [random.randint(0, 400), 
             random.randint(0, 400)]

    opc = " "
    print("Sus coordenadas iniciales son: ", punto)
    while opc != "f":
        opc = menu()

        if(opc in ["n", "s", "e", "o"]):
            punto = validarPunto(opcion[opc](punto[0], punto[1]))
            print("Sus coordenadas son: ", punto)
    print("Sus coordenadas finales fueron: ", punto)

if __name__ == "__main__":
    main()