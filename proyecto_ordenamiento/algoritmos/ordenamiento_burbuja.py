def ordenamiento_burbuja(lista_personas, criterio):
    """
    Ordena una lista de personas usando Bubble Sort.
    """

    total_elementos = len(lista_personas)

    # Recorre toda la lista
    for i in range(total_elementos):

        hubo_intercambio = False

        # Comparar elementos consecutivos
        for j in range(0, total_elementos - i - 1):

            valor_actual = getattr(lista_personas[j], criterio)

            valor_siguiente = getattr(lista_personas[j + 1],criterio)

            # Si el actual es mayor
            if valor_actual > valor_siguiente:

                temporal = lista_personas[j]

                lista_personas[j] = (lista_personas[j + 1])

                lista_personas[j + 1] = temporal

                hubo_intercambio = True

        # Optimización
        if not hubo_intercambio:
            break

    return lista_personas