from base_datos.conexion import conectar


def crear_tabla():
    """
    Crea la tabla persona si esta no existe en la base de datos
    """

    conexion = conectar()

    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS personas (
            id_persona INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            edad INTEGER NOT NULL,
            puntaje_evaluacion INTEGER NOT NULL
        )
    """)

    conexion.commit()
    conexion.close()

    print("Tabla creada exitosamente.")


if __name__ == "__main__":
    crear_tabla()