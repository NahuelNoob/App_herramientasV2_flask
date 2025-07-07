from db import conectar

def agregar_responsable(nombre):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO responsables (nombre) VALUES (%s)", (nombre,))
    conn.commit()
    conn.close()
    print("✅ Responsable agregado.")

def listar_responsables():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM responsables")
    for fila in cursor.fetchall():
        print(fila)
    conn.close()

def obtener_responsables():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre FROM responsables")
    resultado = cursor.fetchall()
    conn.close()
    return resultado
