from db import conectar

def mostrar_herramientas():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM herramientas")
    herramientas = cursor.fetchall()
    for h in herramientas:
        print(h)
    conexion.close()

if __name__ == "__main__":
    mostrar_herramientas()
