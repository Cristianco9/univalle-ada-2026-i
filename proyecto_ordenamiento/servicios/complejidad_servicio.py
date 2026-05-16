class ServicioComplejidad:

    def obtener_complejidad(self, algoritmo):
        """
        Retorna complejidad teórica del algoritmo.
        """

        complejidades = {

            "burbuja": {
                "big_o": "O(n²)",
                "big_theta": "Θ(n²)",
                "big_omega": "Ω(n)"
            },

            "insercion": {
                "big_o": "O(n²)",
                "big_theta": "Θ(n²)",
                "big_omega": "Ω(n)"
            },

            "seleccion": {
                "big_o": "O(n²)",
                "big_theta": "Θ(n²)",
                "big_omega": "Ω(n²)"
            }
        }

        return complejidades.get(algoritmo)