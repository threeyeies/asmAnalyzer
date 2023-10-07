import re  # biblioteca regular expression
import syntan

lineStates = []
state = False


def show():
    # abrir archivo a analizar
    with open("practica.asm") as archivo:
        # Variable de estado para controlar si estamos dentro del segmento .data
        type_segment = 0  # Variable para detectar el tipo de segmento
        lineNumber = 0  # Contador de linea

        for linea in archivo:
            linea = linea.strip()  # Eliminar los saltos de linea
            lineNumber += 1  # Incrementando linea

            if re.findall(r'\.data', linea):  # busca si en la linea esta la etiqueta .data
                type_segment = 1

            if re.findall(r'\.code', linea):  # busca si en la linea esta la etiqueta .code
                type_segment = 2

            if type_segment == 1 and ".data" not in linea:
                getDataSegment(linea)  # Funcion para mostrar en ventana
                syntaxAnalysis(linea, type_segment, lineNumber)

            if type_segment == 2 and ".code" not in linea:
                getCodeSegment(linea)  # Funcion para mostrar en ventana
                syntaxAnalysis(linea, type_segment, lineNumber)


def getDataSegment(linea):
    print(linea, end="")  # sustuir para que se muestre en ventana


def getCodeSegment(linea):
    print(linea, end="")  # sustituir para que se muestre en ventana


# funcion donde se hará el analisis parse
def syntaxAnalysis(linea, type_segment, lineNumber):
    global lineStates
    global state

    if not linea:  # Si la línea está en blanco, ignora el análisis
        return

    if type_segment == 1:
        resultado = syntan.analizar_lineaDataSegment(linea)
        if resultado:
            instruccion, operando1, operando2 = resultado  # Desmpaquetado en variables
            lineStates.append((lineNumber, True))
            state = True
            print(
                f'instruccion: {instruccion}, operando1: {operando1}, operando2: {operando2}')
            print(state)

        else:
            lineStates.append((lineNumber, False))
            state = False
            print(state)

    if type_segment == 2:
        resultado = syntan.analizar_lineaCodeSegment(linea)
        if resultado:
            instruccion, operando1, operando2 = resultado  # Desepaquetado en variables
            lineStates.append((lineNumber, True))
            state = True
            print(
                f'instruccion: {instruccion}, operando1: {operando1}, operando2: {operando2}')
            print(state)

        else:
            lineStates.append((lineNumber, False))
            state = False
            print(state)


def main():
    global lineStates
    show()

    incorrectLines = [line for line, state in lineStates if not state]
    if not incorrectLines:
        print("El código es correcto.")
    else:
        print("El código es incorrecto en las líneas:", incorrectLines)


if __name__ == "__main__":
    main()
