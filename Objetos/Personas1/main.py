from Persona import Persona

def ingresoENTRE(a, b, msj):
    dni = int(input(msj))
    while dni > a or dni < b:
        print("Intente nuevamente...")
        dni = int(input(msj))
    return dni

def ingresar_datos():
    dni = ingresoENTRE(99999999, 0, "Ingrese DNI: ")
    nombre = input("Ingrese un nombre:")
    apellido = input("Ingrese un apellido:")
    edad = ingresoENTRE(100, 0, "Ingrese edad:")
    return Persona(dni, nombre, apellido, edad)

def menor_que(a, b):
    if a<b: return a
    return b


def main():
    flag = 1
    miPersona = ingresar_datos()
    menorEdad = miPersona.edad
    while flag:
        if menor_que(menorEdad, miPersona.edad):
            persona_menor = Persona(miPersona.documento, miPersona.nombre, miPersona.apellido, miPersona.edad)
            menorEdad = persona_menor.edad
        flag = int(input("¿Desea agregar una nueva persona? (0:NO, 1:SI): "))
        if flag:
            miPersona = ingresar_datos()
    print("La persona con menor edad registrada fue: ")
    print(persona_menor)

if __name__ == "__main__":
    main()



