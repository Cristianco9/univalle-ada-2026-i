from openpyxl import Workbook


class ServicioExportarExcel:

    def exportar(self, lista_personas):
        """
        Exporta personas a Excel.
        """

        workbook = Workbook()

        hoja = workbook.active

        hoja.title = ("Personas Ordenadas")

        # Encabezados
        hoja.append(["ID Persona", "Nombre", "Edad", "Puntaje Evaluacion"])

        # Datos
        for persona in lista_personas:

            hoja.append([
                persona.id_persona,
                persona.nombre,
                persona.edad,
                persona.puntaje_evaluacion
            ])

        ruta_archivo = (
            "output/"
            "personas_ordenadas.xlsx"
        )

        workbook.save(ruta_archivo)

        return ruta_archivo