import preguntas as p
import random
from shuffle import shuffle_alt

# Opciones dadas para escoger.

opciones = {'basicas': [1,2,3],
            'intermedias': [1,2,3],
            'avanzadas': [1,2,3]}

# Función 
def choose_q(dificultad):
    """
    Escoge una pregunta aleatoria de un nivel dado y la elimina de la lista.

    Args:
        dificultad: Nivel de dificultad de la pregunta ('basicas', 'intermedias', 'avanzadas').

    Return:
        Tupla con el enunciado y las alternativas mezcladas de la pregunta.
    """
    preguntas = p.pool_preguntas[dificultad]
    
    # usar opciones desde ambiente global
    global opciones
    # escoger una pregunta
    n_elegido = random.choice(opciones[dificultad])
    # eliminarla del ambiente global para no escogerla de nuevo
    opciones[dificultad].remove(n_elegido)
    
    # escoger enunciado y alternativas mezcladas
    pregunta = preguntas[f'pregunta_{n_elegido}']
    alternativas = shuffle_alt(pregunta)
    
    return pregunta['enunciado'], alternativas


if __name__ == '__main__':
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')






    # Escoger preguntas por dificultad
    #preguntas = list(p.pool_preguntas[dificultad].keys())
    
    