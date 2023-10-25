def generar_lista(csv):
    lista = []
    for item in csv.readlines():
        data = item.strip().split(";")
        data[1] = int(data[1])
        lista.append(data)
    return lista

def buscar_codigo(cod, lista):
    for i, item in enumerate(lista):
        if item[1] == cod:
            return i
    return -1

def ingreso_codigos():
    codigos = []
    codigo = 1
    while codigo != 0:
        codigo = int(input("Ingrese codigo postal (0 para terminar): "))
        if codigo != 0:
            codigos.append(codigo)
    return codigos

def imprimir_datos(codigos, datos):
    codigos_no_encontrados = []
    print("\nCodigos encontrados:")
    print("NUMERO|PROVINCIA|NOMBRE")
    for codigo in codigos:
        indice = buscar_codigo(codigo, datos)
        if indice != -1:
            print(f"{codigo:^6}|{datos[indice][0]:^9}|{datos[indice][2]:^5}")
        else:
            codigos_no_encontrados.append(codigo)
    
    if len(codigos_no_encontrados) > 0:
        print("Los codigos no encontrados fueron:", codigos_no_encontrados)



def main():
    archivo = open("cp.csv", "r")
    datos = generar_lista(archivo)
    codigos = ingreso_codigos()
    imprimir_datos(codigos, datos)
    archivo.close()

if __name__ == "__main__":
    main()
