"""
Alternativas:

En lugar de ingresar cada movimiento individualmente, se puede recibir una cadena 
que contenga más de un movimiento, por ejemplo "NNEENSSNO".
En el caso de que una orden de movimiento lleve al robot fuera de los márgenes del plano, 
el movimiento debería finalizar en el borde.
"""

import random
def menu():
    instrucciones = input("Ingrese la cadena de instrucciones (F para terminar): ")
    return instrucciones.lower()



def main():
    x = random.randint(0, 400)
    y = random.randint(0, 400)
    mayor400 = lambda x: x>400
    menorA_cero = lambda x: x<0
    punto = [x, y]
    flag = True
    print("Sus coordenadas iniciales son: ", punto)
    while flag:
        instrucciones = menu()
        for instruccion in instrucciones: 
            if(instruccion == "n"):
                punto[1] += 10
                if(mayor400(punto[1])):
                    punto[1] = 400
            elif(instruccion == "s"):
                punto[1] -= 20
                if(menorA_cero(punto[1])):
                    punto[1] = 0
            elif(instruccion == "e"):
                punto[0] += 10
                if(mayor400(punto[0])):
                    punto[0] = 400
            elif(instruccion == "o"):
                punto[0] -= 20
                if(menorA_cero(punto[0])):
                    punto[0] = 0
            elif(instruccion == "f"):
                print("Bye Bye")
                flag = False
                break
            else:
                print("Opcion no válida...")
            if(instruccion != "f"):
                print("Sus coordenadas son: ", punto)
    print("Sus coordenadas finales fueron: ", punto)

if __name__ == "__main__":
    main()