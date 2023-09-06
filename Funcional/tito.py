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



def main():
    x = random.randint(0, 400)
    y = random.randint(0, 400)
    mayor400 = lambda x: x>400
    menorA_cero = lambda x: x<0
    punto = [x, y]
    opc = " "
    print("Sus coordenadas iniciales son: ", punto)
    while opc != "f":
        opc = menu()
        if(opc == "n"):
            punto[1] += 10
            if(mayor400(punto[1])):
                punto[1] = 400
        elif(opc == "s"):
            punto[1] -= 20
            if(menorA_cero(punto[1])):
                punto[1] = 0
        elif(opc == "e"):
            punto[0] += 10
            if(mayor400(punto[0])):
                punto[0] = 400
        elif(opc == "o"):
            punto[0] -= 20
            if(menorA_cero(punto[0])):
                punto[0] = 0
        elif(opc == "f"):
            print("Bye Bye")
        else:
            print("Opcion no válida...")
        if(opc != "f"):
            print("Sus coordenadas son: ", punto)
    print("Sus coordenadas finales fueron: ", punto)

if __name__ == "__main__":
    main()