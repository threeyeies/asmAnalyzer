# lexeme analysis: Analizar las lineas e identificar los lexemas

import re
from lexan import MNEMONICS, DIRECTIVES, REGISTERS, MACROS_AND_FUNTIONS, INT_CONSTANTS, LABELS


# Define una lista de directorios junto con sus nombres
directories = [(MNEMONICS, 'MNEMONICS'), (DIRECTIVES, 'DIRECTIVES'), (REGISTERS, 'REGISTERS'),
               (MACROS_AND_FUNTIONS, 'MACROS_AND_FUNCTIONS'), (INT_CONSTANTS, 'INT_CONSTANTS'), (LABELS, 'LABELS'),]

# Patron para alphanumericos
alphaNumericPattern = re.compile(r'^\s*([a-zA-Z][a-zA-Z0-9]{1,247})\s*')


def lexemaAnalysis(palabra, isString):

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
            
            
            
            if palabra.casefold() == ';':  # Si se encuentra un comentario
                return (palabra, isString, 'COMMENT')
            
            if '.' in palabra and palabra[0].isdigit(): #Si el numero es un real
                return (palabra, isString, 'REAL_INT_CONSTANTS')
            
            if '.' in palabra and palabra[0].casefold() == '-' and palabra[1].isdigit(): #Si el numero es un real negativo
                return (palabra, isString, 'NEGATIVE_REAL_INT_CONSTANTS')
            
            if '.' in palabra and palabra[0].casefold() == '+' and palabra[1].isdigit(): #Si el numero es un real marcado con +
                return (palabra, isString, 'REAL_INT_CONSTANTS')
            
            if palabra.isdigit(): #Si es un numero sin sufijo 
                return (palabra, isString,  'INT_CONSTANTS')
            
            if palabra.casefold() == '?': #Si es una varialbe sin inicializar
                return (palabra, isString,  'UNINITIALIZED VARIABLE')
            
            if palabra[0].casefold() == '-' and palabra[1].isdigit(): #Si el número es negativo
                return (palabra, isString, 'NEGATIVE_INT_CONSTANTS')
            
           
            
            if (palabra[0].isdigit() and palabra[-1].casefold() == valor.casefold()) or (palabra[0] == '+' and palabra[1].isdigit() and palabra[-1].casefold() == valor.casefold()): # Comprobar si la palabra comienza con un número y termina con el sufijo de una base
                #Este codigo es para obtener el nombre de la clave que contiene el valor; NOTA: Estoy seguro que no esta optimizado y se puede hacer de manera mas simple pero solo se me ocurrio esta forma jaja
                claves = list(directory.keys())
                i=0
                for clave, valor2 in directory.items():
                    if valor2 == valor.casefold():
                        break  # Detén la búsqueda cuando encuentres el valor
                    i += 1
                num_type = claves[i]
                return (palabra, isString,directory_name + ' TYPE ' + num_type)
            
            
            
            if (palabra[0].casefold() == "'"  and palabra[-1].casefold() == "'" ) or ( palabra[0].casefold() == '"' and palabra[-1].casefold() == '"'): #Comprueba si es constante de tipo cadena de una sola palabra
                return (palabra, isString, 'STRING_OR_CHARACTER_CONSTANT')
            
            
            if palabra[0].casefold() == "'"  or palabra[0].casefold() == '"' or palabra[-1].casefold() == "'"  or palabra[-1].casefold() == '"': #Comprueba si es constante de tipo cadena
                isString = not isString #isString nos ayuda a saber cuando empieza y cuando termina la cadena
                return (palabra, isString, 'STRING_CONSTANT')
            
            if palabra[-1].casefold() == ':': #Comprueba si es una etiqueta
                return (palabra, isString, 'LABEL')
            
            if palabra.casefold() == valor.casefold(): #Encontrar a que caso pertenece la palabra
                if palabra[0].casefold() == '.': #Si es una directiva comprueba si empieza con ','
                    return (palabra,  isString, '.DIRECTIVES')
                return (palabra,  isString, directory_name)
            

    # ESTE IF FALTA IMPLEMENTARLO BIEN
    # se supone que encontraría un alphanumerico y diria, ah, pues esa palabra es un alphanumerico
    if alphaNumericPattern.match(palabra.casefold()):
        return (palabra, isString, "VARIABLE_PATTERN")

    # Si no se encuentra en ninguno de los directorios, devolver "No reconocido"
    return (palabra, isString, 'No reconocido' )
