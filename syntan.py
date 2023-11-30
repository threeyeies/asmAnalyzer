# syntax analysis: Establecer Palabras Relativas y la comparacion del archivo con ellas

import re

# importando los diccionarios (analisis lexico)
from lexan import MNEMONICS, DIRECTIVES, REGISTERS, MACROS_AND_FUNTIONS, INT_CONSTANTS, LABELS

# Definir una expresión regular de difernetes palabras reservadas utilizando el diccionario
mnemonic_pattern = '|'.join(MNEMONICS.values())
directives_pattern = '|'.join(DIRECTIVES.values())
registers_pattern = '|'.join(REGISTERS.values())
macros_and_funtions_pattern = '|'.join(MACROS_AND_FUNTIONS.values())
int_constants_pattern = '|'.join(INT_CONSTANTS.values())
labels_pattern = '|'.join(LABELS.values())


# Definir una expresión regular para las instrucciones del dataSegment
instruccion_patternDataSegment = re.compile(
    r'^\s*([a-zA-Z][a-zA-Z0-9]{1,247})\s+(DWORD|WORD|BYTE|DB|QWORD|16 bits|24 bits|64 bits|{directives_pattern})\s+(\?|\d+|\w+)', re.IGNORECASE)

# Definir una expresión regular para las instrucciones del codeSegment
instruccion_patternCodeSegment = re.compile(
    rf'^\s*({mnemonic_pattern})\s+({registers_pattern}),\s*(\w+[rtqxyRTQXY]?)\s*$', re.IGNORECASE)

# Definir una expresión regular para las instrucciones de procesos
instruccion_patternProc = re.compile(
    rf'^\s*([a-zA-Z][a-zA-Z0-9]{{1,247}})\s+({directives_pattern})', re.IGNORECASE)

# Definir una expresion regular para las instrucciones de metodos
instruccion_patternMetodos = re.compile(
    rf'^\s*({directives_pattern})\s+([a-zA-Z][a-zA-Z0-9]{{1,247}})', re.IGNORECASE)

# Definir una expresion regular para instrucciones de macros y funciones de Windows
instruccion_patternMacrosAndFuntions = re.compile(
    rf'^\s*({macros_and_funtions_pattern})\s+({macros_and_funtions_pattern}),\s+([0-9])', re.IGNORECASE)

instruccion_patternMainProc = re.compile(
    rf'^\s*({macros_and_funtions_pattern})\s+({macros_and_funtions_pattern})', re.IGNORECASE)


# Definiendo una expresión regular para ins reg/mem/etiqueta
instruccion_patternAsignedProject = re.compile(
    rf'^\s*(LOOP|JMP|INC|NEG)\s+({registers_pattern}|([a-zA-Z][a-zA-Z0-9]{{1,247}}))\s*$', re.IGNORECASE)

# Definiendo una expresión regular para etiqueta:

instruccion_patternLabel = re.compile(
    rf'^\s*(([a-zA-Z][a-zA-Z0-9]{{0,246}}))\s*(:)?\s*$', re.IGNORECASE)


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
    matchMacrosAndFuntions = instruccion_patternMacrosAndFuntions.match(linea)
    matchAsignedProject = instruccion_patternAsignedProject.match(linea)
    matchMainProc = instruccion_patternMainProc.match(linea)
    matchLabel = instruccion_patternLabel.match(linea)

    if match:
        # haciendo una desempaquetacion de la linea, sirve para mandar las parte de la instruccion
        instruccion = match.group(1).upper()
        operando1 = match.group(2)
        operando2 = match.group(3)
        return instruccion, operando1, operando2

    elif matchProc:

        instruccionProc = matchProc.group(1)
        operando1Proc = matchProc.group(2)
        operando2Proc = ""
        return instruccionProc, operando1Proc, operando2Proc

    elif matchMetodos:
        instruccionMetodos = matchMetodos.group(1)
        operando1Metodos = matchMetodos.group(2)
        operando2Metodos = ""
        return instruccionMetodos, operando1Metodos, operando2Metodos

    elif matchMacrosAndFuntions:
        instruccionMacrosAndFuntions = matchMacrosAndFuntions.group(1)
        operando1MacrosAndFuntions = matchMacrosAndFuntions.group(2)
        operando2MacrosAndFuntions = matchMacrosAndFuntions.group(3)
        return instruccionMacrosAndFuntions, operando1MacrosAndFuntions, operando2MacrosAndFuntions

    elif matchAsignedProject:
        instruccionAP = matchAsignedProject.group(1)
        destinoAP = matchAsignedProject.group(2)
        vacioAP = ""
        return instruccionAP, destinoAP, vacioAP

    elif matchMainProc:
        instruccionMP = matchMainProc.group(1)
        otherMP = matchMainProc.group(2)
        vacio = ""
        return instruccionMP, otherMP, vacio

    elif matchLabel:
        instruccionLabel = matchLabel.group(1)
        indicator = matchLabel.group(2)
        vacio = ""
        return instruccionLabel, indicator, vacio
