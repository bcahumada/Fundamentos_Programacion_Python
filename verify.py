import preguntas as p
from print_preguntas import print_pregunta

def verificar(alternativas, eleccion):
    """
    Verifica si la respuesta del usuario es correcta.

    Args:
        alternativas: Lista de alternativas posibles e indicadores
        eleccion: Respuesta del usuario (letra de la alternativa).

    Return:
        Informa si la respuesta es correcta o es incorrecta.
    """
    eleccion = ['a', 'b', 'c','d'].index(eleccion)

    # Lógica para determinar respuestas correctas
 
    correcto = alternativas[eleccion][1] == 1
    if correcto:
        print('Respuesta Correcta')
    else:
        print('Respuesta Incorrecta')

    return correcto

if __name__ == '__main__':
    
    
    # definir la respuesta correcta ? = alt_2
    pregunta = p.pool_preguntas['basicas']['pregunta_2']
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
    respuesta = input('Escoja la alternativa correcta:\n> ').lower()
    verificar(pregunta['alternativas'], respuesta)