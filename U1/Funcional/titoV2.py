"""
Alternativas:

En lugar de ingresar cada movimiento individualmente, se puede recibir una cadena 
que contenga más de un movimiento, por ejemplo "NNEENSSNO".
En el caso de que una orden de movimiento lleve al robot fuera de los márgenes del plano, 
el movimiento debería finalizar en el borde.
"""
import random
def menu():
    opc = input("Escriba la secuencia que desee ejecutar(F para terminar): ")
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

    flag = True
    print("Sus coordenadas iniciales son: ", punto)
    while flag:
        instrucciones = menu()
        for instruccion in instrucciones:
            if(instruccion in ["n", "s", "e", "o"]):
                punto = validarPunto(opcion[instruccion](punto[0], punto[1]))
            elif(instruccion == "f"):
                flag = False
        print("Sus coordenadas son: ", punto)
        
    print("Sus coordenadas finales fueron: ", punto)

if __name__ == "__main__":
    main()