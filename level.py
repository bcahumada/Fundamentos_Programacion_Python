def choose_level(n_pregunta, p_level):
    """
    Determina el nivel de dificultad de una pregunta.

    Args:
        n_pregunta: Número de la pregunta actual.
        p_level: Cantidad de preguntas por nivel.

    Return:
        Nivel de dificultad de la pregunta.
    """

    # Define la variable level con un valor por defecto
    level = None

    # Lógica para escoger el nivel
    if p_level == 2:
        if n_pregunta <= 2:
            level = 'basicas'
        elif n_pregunta <= 4:
            level = 'intermedias'
        else:
            level = 'avanzadas'
    elif p_level == 3:
        if n_pregunta <= 3:
            level = 'basicas'
        elif n_pregunta <= 6:
            level = 'intermedias'
        else:
            level = 'avanzadas'
    elif p_level == 1:  # Agrega esta condición para p_level == 1
        level = 'basicas'  # Asigna un valor válido para level

    return level


if __name__ == '__main__':
    # Test entregado en cada requerimiento 
    eleccion = str(input('Ingresa una Opción: ')).lower()
    # verificar resultados
    print(choose_level(2, 2)) # básicas
    print(choose_level(3, 2)) # intermedias
    print(choose_level(7, 2)) # avanzadas
    print(choose_level(4, 3)) # intermedias
    print(choose_level(1, 1))  # Test para p_level == 1



