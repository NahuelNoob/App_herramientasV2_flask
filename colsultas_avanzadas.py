from db import conectar

def historial_retiros():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT r.id, h.nombre, res.nombre, r.cantidad_retirada, r.fecha_retiro, r.observaciones
        FROM retiros r
        JOIN herramientas h ON r.herramienta_id = h.id
        JOIN responsables res ON r.retirado_por = res.id
        ORDER BY r.fecha_retiro DESC
    """)
    for fila in cursor.fetchall():
        print(fila)
    conn.close()

def retiros_por_responsable(responsable_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT h.nombre, r.cantidad_retirada, r.fecha_retiro, r.observaciones
        FROM retiros r
        JOIN herramientas h ON r.herramienta_id = h.id
        WHERE r.retirado_por = %s
        ORDER BY r.fecha_retiro DESC
    """, (responsable_id,))
    for fila in cursor.fetchall():
        print(fila)
    conn.close()

def herramientas_por_ubicacion(ubicacion):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM herramientas WHERE ubicacion = %s", (ubicacion,))
    for fila in cursor.fetchall():
        print(fila)
    conn.close()

def herramientas_con_stock_bajo(limite=2):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM herramientas WHERE cantidad_total <= %s", (limite,))
    for fila in cursor.fetchall():
        print(fila)
    conn.close()
