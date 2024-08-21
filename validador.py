def validate(opciones, eleccion):
    # Definir validación de eleccion
    """
    Valida si una opción se encuentra dentro de un conjunto de opciones.

    Args:
        opciones: Lista de opciones válidas.
        eleccion: Opción elegida por el usuario.

    Return:
        Se regresa la opción elegida si esta es válida, de lo contrario solicita una opción válida.
    """
    while eleccion not in opciones:
        print(f'Opción no válida, ingrese una de las opciones válidas:{opciones}')
        eleccion = input('Ingresa una Opción: ').lower()
    return eleccion


if __name__ == '__main__':
    eleccion = str(input('Ingresa una Opción: ')).lower()
    numeros = ['0','1', '2', '3']
    # Si se ingresan valores no validos a eleccion debe seguir preguntando
    validate(numeros, eleccion)



