class Persona:

    def __init__(self, id_persona, nombre, edad, puntaje_evaluacion):
        self.id_persona = id_persona
        self.nombre = nombre
        self.edad = edad
        self.puntaje_evaluacion = puntaje_evaluacion

    def convertir_a_diccionario(self):
        """
        Convierte el objeto en diccionario.
        """

        return {
            "id_persona": self.id_persona,
            "nombre": self.nombre,
            "edad": self.edad,
            "puntaje_evaluacion": self.puntaje_evaluacion
        }