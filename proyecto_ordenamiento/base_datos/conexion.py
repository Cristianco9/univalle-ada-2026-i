import sqlite3


def conectar():
    """
    Crea una conexion con la base de datos SQLite
    """

    conexion = sqlite3.connect("data/personas.db")

    return conexion