def ordenamiento_insercion(lista_personas, criterio):
    """
    Ordena una lista de personas usando Insertion Sort.
    """

    total_elementos = len(lista_personas)

    for i in range(1, total_elementos):

        elemento_actual = (lista_personas[i])

        valor_actual = getattr(elemento_actual, criterio)

        posicion = i - 1

        while posicion >= 0:

            valor_posicion = getattr(lista_personas[posicion], criterio)

            if (valor_posicion > valor_actual):

                lista_personas[posicion + 1] = lista_personas[posicion]

                posicion -= 1

            else:
                break

        lista_personas[posicion + 1] = elemento_actual

    return lista_personas