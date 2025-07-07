from db import conectar

def agregar_herramienta(nombre, cantidad, ubicacion, descripcion):
    conn = conectar()
    cursor = conn.cursor()
    sql = "INSERT INTO herramienta (nombre, cantidad_total,ubicacion, descripcion) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (nombre, cantidad, ubicacion, descripcion))
    conn.commit()
    conn.close()
    print("✅ Herramienta agregada.")

def listar_herramientas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, cantidad_total, ubicacion FROM herramientas")
    herramientas = cursor.fetchall()
    conn.close()
    return herramientas


def editar_herramienta(id_herramienta, nombre=None, cantidad=None, ubicacion=None, descripcion=None):
    conn = conectar()
    cursor = conn.cursor()
    campos = []
    valores = []

    if nombre:
        campos.append("nombre = %s")
        valores.append(nombre)
    if cantidad is not None:
        campos.append("cantidad_total = %s")
        valores.append(cantidad)
    if ubicacion:
        campos.append("ubicacion = %s")
        valores.append(ubicacion)
    if descripcion:
        campos.append("descripcion = %s")
        valores.append(descripcion)

    if campos:
        sql = f"UPDATE herramientas SET {', '.join(campos)} WHERE id = %s"
        valores.append(id_herramienta)
        cursor.execute(sql, valores)
        conn.commit()
        print("✅ Herramienta actualizada.")
    conn.close()

def eliminar_herramienta(id_herramienta):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM herramientas WHERE id = %s", (id_herramienta,))
    conn.commit()
    conn.close()
    print("🗑️ Herramienta eliminada.")

def obtener_herramientas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre FROM herramientas")
    resultado = cursor.fetchall()
    conn.close()
    return resultado
