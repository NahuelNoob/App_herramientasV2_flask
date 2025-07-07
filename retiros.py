
from db import conectar

def registrar_retiro(herramienta_id, responsable_id, cantidad, observaciones=None):
    conn = conectar()
    cursor = conn.cursor()

    # Registrar retiro
    sql = """
    INSERT INTO retiros (herramienta_id, retirado_por, cantidad_retirada, observaciones)
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(sql, (herramienta_id, responsable_id, cantidad, observaciones))
    
    # Actualizar cantidad disponible (opcional: control de stock)
    cursor.execute("SELECT cantidad_total FROM herramientas WHERE id = %s", (herramienta_id,))
    cantidad_actual = cursor.fetchone()[0]
    nueva_cantidad = cantidad_actual - cantidad
    cursor.execute("UPDATE herramientas SET cantidad_total = %s WHERE id = %s", (nueva_cantidad, herramienta_id))
    
    conn.commit()
    conn.close()
    print("✅ Retiro registrado.")

def herramienta_existe(herramienta_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM herramientas WHERE id = %s", (herramienta_id,))
    existe = cursor.fetchone() is not None
    conn.close()
    return existe

def responsable_existe(responsable_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM responsables WHERE id = %s", (responsable_id,))
    existe = cursor.fetchone() is not None
    conn.close()
    return existe

def obtener_stock(herramienta_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT cantidad_total FROM herramientas WHERE id = %s", (herramienta_id,))
    resultado = cursor.fetchone()
    conn.close()
    return resultado[0] if resultado else None

def registrar_retiro(herramienta_id, responsable_id, cantidad, observaciones):
    conn = conectar()
    cursor = conn.cursor()

    # Verificar stock
    cursor.execute("SELECT cantidad_total FROM herramientas WHERE id = %s", (herramienta_id,))
    stock_actual = cursor.fetchone()[0]
    if cantidad > stock_actual:
        print("❌ No hay suficiente stock.")
        conn.close()
        return

    # Registrar retiro
    cursor.execute("""
        INSERT INTO retiros (herramienta_id, retirado_por, cantidad_retirada, observaciones)
        VALUES (%s, %s, %s, %s)
    """, (herramienta_id, responsable_id, cantidad, observaciones))

    # Descontar stock
    nuevo_stock = stock_actual - cantidad
    cursor.execute("UPDATE herramientas SET cantidad_total = %s WHERE id = %s", (nuevo_stock, herramienta_id))

    conn.commit()
    conn.close()
    print("✅ Retiro registrado correctamente.")
