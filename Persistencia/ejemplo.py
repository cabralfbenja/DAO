import sqlite3

conn = sqlite3.connect("personas.db")
cursor = conn.cursor()
#cursor.execute("CREATE TABLE articulos(id integer primary key autoincrement, nombre text, precio numeric)")

# Insert Hardcodeado
#cursor.execute("insert into articulos(nombre, precio) values (?,?)", ("Martillo", 500))

# Insert Hardcodeado con parámetros
#nombre = input("Ingres el nombre del articulo: ")
#precio = int(input("Ingres el precio del articulo: "))
#cursor.execute("insert into articulos(nombre, precio) values (?,?)", (nombre, precio))
#conn.commit()  # para modificaciones

cursor.execute("SELECT * FROM articulos")


#cursor.fetchone()  lista con las columnas, fila por fila
#cursor.fetchall()  una lista de listas

#for fila in cursor.fetchall(): # ojo, a veces las tablas son muy grandes
    #id, nombre, precio = fila
    # nuevo = Articulo(*fila)
    
while fila := cursor.fetchone():
    print(fila)


    