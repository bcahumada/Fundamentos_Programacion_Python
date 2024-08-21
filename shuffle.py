import preguntas as p
import random

def shuffle_alt(pregunta):
    """
    Mezcla las alternativas de una pregunta cada vez que comienza la trivia.

    Args:
        pregunta: Diccionario que representa una pregunta con alternativas.

    Return:
        Lista de alternativas mezcladas o en diferente orden.
    """
    alternativas = pregunta['alternativas']
    random.shuffle(pregunta['alternativas'])
    return pregunta['alternativas']

if __name__ == '__main__':
  print(shuffle_alt(p.pool_preguntas['basicas']['pregunta_1'])) 
