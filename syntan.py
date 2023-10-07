import re

# Definir una expresión regular para las isntrucciones del dataSegment
instruccion_patternDataSegment = re.compile(
    r'^\s*([a-zA-Z][a-zA-Z0-9]{1,123})\s+(DWORD|WORD|BYTE|QWORD|16 bits|24 bits|64 bits)\s+(\?|\d+)', re.IGNORECASE)

instruccion_patternProc = re.compile(
    r'^\s*([a-zA-Z][a-zA-Z0-9]{1,123})\s+(proc|endp)', re.IGNORECASE)

instruccion_patternOthers = re.compile(
    r'^\s*(invoke ExitProcess,|end)\s+([0-9]|main)', re.IGNORECASE)

# Definir una expresión regular para las instrucciones del codeSegment
instruccion_patternCodeSegment = re.compile(
    r'^\s*(MOV|LEA|ADD|SUB|INC|DEC|AND|OR|XOR|NOT|CMP|JMP|MUL|IMUL|DIV|IDIV|CALL|RET|PUSH|POP)\s+(\w+),\s*(\w+)\s*$', re.IGNORECASE)


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
    matchex = instruccion_patternProc.match(linea)
    matchoth = instruccion_patternProc.match(linea)

    if match:
        # Obtener la instrucción en mayúsculas
        instruccion = match.group(1).upper()
        operando1 = match.group(2)
        operando2 = match.group(3)
        return instruccion, operando1, operando2

    elif matchex:
        # Obtener la instrucción en mayúsculas
        instruccionex = matchex.group(1)
        operando1ex = matchex.group(2)
        operando2ex = None
        return instruccionex, operando1ex, operando2ex

    elif matchoth:
        # Obtener la instrucción en mayúsculas
        instruccionex = matchoth.group(1)
        operando1ex = matchoth.group(2)
        operando2ex = None
        return instruccionex, operando1ex, operando2ex
