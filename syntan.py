# syntax analysis: Establecer Palabras Relativas y la comparacion del archivo con ellas

import re

# importando los diccionarios (analisis lexico)
from lexan import MNEMONICS, DIRECTIVES, REGISTERS, INT_CONSTANTS, LABELS

# Definir una expresión regular de difernetes palabras reservadas utilizando el diccionario
mnemonic_pattern = '|'.join(MNEMONICS.values())
directives_pattern = '|'.join(DIRECTIVES.values())
registers_pattern = '|'.join(REGISTERS.values())
int_constants_pattern = '|'.join(INT_CONSTANTS.values())
labels_pattern = '|'.join(LABELS.values())


# Definir una expresión regular para las instrucciones del dataSegment
instruccion_patternDataSegment = re.compile(
    r'^\s*([a-zA-Z][a-zA-Z0-9]{1,123})\s+(DWORD|WORD|BYTE|QWORD|16 bits|24 bits|64 bits)\s+(\?|\d+)', re.IGNORECASE)

# Definir una expresión regular para las instrucciones de procesos
instruccion_patternProc = re.compile(
    rf'^\s*([a-zA-Z][a-zA-Z0-9]{1,123})\s+({directives_pattern})', re.IGNORECASE)

instruccion_patternMetodos = re.compile(
    rf'^\s*({directives_pattern}\s+([a-zA-Z][a-zA-Z0-9]{1,123}))', re.IGNORECASE)

instruccion_patternOthers = re.compile(
    r'^\s*(.*invoke.*ExitProcess,.*0|end.*main)', re.IGNORECASE)

# Definir una expresión regular para las instrucciones del codeSegment
instruccion_patternCodeSegment = re.compile(
    rf'^\s*({mnemonic_pattern})\s+(\w+),\s*(\w+)\s*$', re.IGNORECASE)


def analizar_lineaDataSegment(linea):
    # Buscar coincidencias con la expresión regular
    match = instruccion_patternDataSegment.match(linea)

    if match:
        # Obtener la instrucción
        instruccion = match.group(1)
        operando1 = match.group(2)
        operando2 = match.group(3)
        return instruccion, operando1, operando2


def analizar_lineaCodeSegment(linea):
    # Buscar coincidencias con la expresión regular
    match = instruccion_patternCodeSegment.match(linea)
    matchProc = instruccion_patternProc.match(linea)
    matchMetodos = instruccion_patternMetodos.match(linea)

    if match:
        # haciendo una desempaquetacion de la linea, sirve para mandar las parte de la instruccion
        instruccion = match.group(1).upper()
        operando1 = match.group(2)
        operando2 = match.group(3)
        return instruccion, operando1, operando2

    elif matchProc:

        instruccionProc = matchProc.group(1)
        operando1Proc = matchProc.group(2)
        operando2Proc = None
        return instruccionProc, operando1Proc, operando2Proc

    elif matchMetodos:
        instruccionMetodos = matchMetodos.group(1)
        operando1Metodos = matchMetodos.group(2)
        operando2Metodos = None
        return instruccionMetodos, operando1Metodos, operando2Metodos
