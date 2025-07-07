from retiros import obtener_stock
from retiros import herramienta_existe
from db import conectar

def devolver_herramienta(herramienta_id, cantidad):
    if cantidad <= 0:
        print("❌ La cantidad debe ser mayor que cero.")
        return

    if not herramienta_existe(herramienta_id):
        print("❌ La herramienta no existe.")
        return

    stock = obtener_stock(herramienta_id)
    nuevo_stock = stock + cantidad

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE herramientas SET cantidad_total = %s WHERE id = %s", (nuevo_stock, herramienta_id))
    conn.commit()
    conn.close()
    print(f"🔁 Devolución realizada. Stock actualizado a {nuevo_stock}")

