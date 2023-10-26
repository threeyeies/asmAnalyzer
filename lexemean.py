# lexeme analysis: Analizar las lineas e identificar los lexemas

import re
from lexan import MNEMONICS, DIRECTIVES, REGISTERS, MACROS_AND_FUNTIONS, INT_CONSTANTS, LABELS


# Define una lista de directorios junto con sus nombres
directories = [(MNEMONICS, 'MNEMONICS'), (DIRECTIVES, 'DIRECTIVES'), (REGISTERS, 'REGISTERS'),
               (MACROS_AND_FUNTIONS, 'MACROS_AND_FUNCTIONS'), (INT_CONSTANTS, 'INT_CONSTANTS'), (LABELS, 'LABELS')]

# Patron para alphanumericos
alphaNumericPattern = re.compile(r'^\s*([a-zA-Z][a-zA-Z0-9]{1,247})\s*')


def lexemaAnalysis(palabra):

    # es otro tratamiento alternativo a la utilizacion de expresiones regulares linea 85 en editorTxt.py
    '''def run():
        # Separar la palabra en dos utilizando la coma como delimitador
        partes = palabra.split(',')
        for directory, directory_name in directories:
            for valor in directory.values():
                if partes[0].casefold() == valor.casefold():
                    return (partes[0], directory_name)
                if partes[1].casefold() == valor.casefold():
                    return (partes[1], directory_name)

    if ',' in palabra:
        run(palabra)

    if ' ' in palabra:
        # Separar la palabra en dos utilizando espacio como delimitador
        partes = palabra.split(' ')
        if ',' in palabra:
            for parte in partes:
                run(parte)

        for directory, directory_name in directories:
            for valor in directory.values():
                if partes[0].casefold() == valor.casefold():
                    return (partes[0], directory_name)
                if partes[1].casefold() == valor.casefold():
                    return (partes[1], directory_name)'''

    for directory, directory_name in directories:
        for valor in directory.values():
            if palabra.casefold() == valor.casefold():
                return (palabra, directory_name)

    # ESTE IF FALTA IMPLEMENTARLO BIEN
    # se supone que encontraría un alphanumerico y diria, ah, pues esa palabra es un alphanumerico
    if alphaNumericPattern.match(palabra.casefold()):
        return (palabra, "variable_pattern")

    # Si no se encuentra en ninguno de los directorios, devolver "No reconocido"
    return (palabra, 'No reconocido')
