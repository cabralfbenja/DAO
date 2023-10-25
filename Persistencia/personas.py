import sqlite3
conn = sqlite3.connect("personas.sqlite")
cursor = conn.cursor()

cursor.execute("select * from Personas p where p.edad>40")

for fila in cursor.fetchall():
    print(fila)

cursor.close()
conn.close()