import re  # biblioteca regular expression


def show():
    # abrir archivo a analizar
    with open("practica.asm") as archivo:
        # Variable de estado para controlar si estamos dentro del segmento .data
        type_segment = 0

        for linea in archivo:

            if re.findall(r'\.data', linea):  # busca si en la linea esta la etiqueta .data
                type_segment = 1

            if re.findall(r'\.code', linea):  # busca si en la linea esta la etiqueta .code
                type_segment = 2

            if type_segment == 1 and ".data" not in linea:
                getDataSegment(linea)
                # parseAnalitic(linea)

            if type_segment == 2 and ".code" not in linea:
                getCodeSegment(linea)
                # parseAnalitic(linea)


def getDataSegment(linea):
    print(linea, end="")  # sustuir para que se muestre en ventana


def getCodeSegment(linea):
    print(linea, end="")  # sustituir para que se muestre en ventana

# funcion donde se hará el analisis parse
# def parseAnalitic(lista):


def main():
    show()


if __name__ == "__main__":
    main()
