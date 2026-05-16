from base_datos.conexion import conectar
from modelos.persona import Persona


class RepositorioPersona:

    def obtener_todas_las_personas(self):
        """
        Obtiene todas las personas de la base de datos.
        """

        conexion = conectar()

        cursor = conexion.cursor()

        cursor.execute("""
            SELECT
                id_persona,
                nombre,
                edad,
                puntaje_evaluacion
            FROM personas
        """)

        registros = cursor.fetchall()

        conexion.close()

        lista_personas = []

        for registro in registros:

            persona = Persona(
                registro[0],
                registro[1],
                registro[2],
                registro[3]
            )

            lista_personas.append(persona)

        return lista_personas