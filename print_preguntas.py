import preguntas as p

def print_pregunta(enunciado, alternativas):
    """
    Imprime el enunciado y las alternativas de una pregunta con formato.

    Args:
        enunciado: Lista con el enunciado de la pregunta.
        alternativas: Lista de alternativas con sus textos y indicadores de correcto.

    Formato: Enunciado básico 1

    # A. alt_1
    # B. alt_2
    # C. alt_3
    # D. alt_4
    """
    print(enunciado[0])
    letras = ['A', 'B', 'C', 'D']
    for i, alt in enumerate(alternativas):
        print(f"{letras[i]}. {alt[0]}")

if __name__ == '__main__':
    # Muestra preguntas y alternativas siguiendo el formato
    pregunta = p.pool_preguntas['basicas']['pregunta_1']
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])



    
