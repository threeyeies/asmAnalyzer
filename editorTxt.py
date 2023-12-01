from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from screeninfo import get_monitors
from tkinter import font
from ttkthemes import ThemedTk
from analysisForLine import show, lexemeAnalysis, lineStates
import re

# Cambiar el directorio de acceso para uno de Windows
# Cambiar el tipo de archivos de abre de txt a asm}
# Agregar regleta y que se sombre la linea que se esta editando*
# Quitar codigo ineccesario para poder implementar en el proyecto final

# Configuración de la ventana

root = ThemedTk()
root.set_theme('equilux')
root.title("ASM Analysis")  # Título de la ventana
monitor = get_monitors()[0]
ancho_ventana = monitor.width // 2
alto_ventana = monitor.height // 2
root.geometry(f"{ancho_ventana}x{alto_ventana}")  # Dimensiones ventana
#root.iconbitmap("Akane.ico")  # Icono
root.configure(bg="#202020")  # Fondo de estilo "cyberpunk"

# Crear un estilo personalizado para los widgets
style = ttk.Style()
style.configure("TButton", padding=10, relief="flat")
style.configure("TLabel", background="#f2f2f2", font=("Helvetica", 14))
style.configure("TFrame", background="#f2f2f2")
style.configure("TText", background="white", font=("Courier", 14))

global statusName

global lineaAnalizada


type_segment = 0
statusName = False

global selected
selected = False

# Funciones


def newFile():
    textBox.configure(state='normal')
    textBox.delete("1.0", END)
    statusBar.config(text="Nuevo archivo...")


def openFile():
    textBox.configure(state='normal')
    textBox.delete("1.0", END)

    textFile = filedialog.askopenfilename(
        initialdir="/home/danielperez/Documents/Python Projects/ASM Analysis",
        title="Abrir archivo",
        filetypes=(("Archivos de ensamblador", "*.asm"),
                   ("Archivos de texto", "*.txt"))
    )

    if textFile:
        global statusName
        global lineaAnalizada
        statusName = textFile

        with open(textFile, 'r') as file:
            global contenido 
            contenido = file.read()
            textBox.insert(END, contenido)
            statusBar.config(text="Archivo abierto...")

            # habilando contenedores
            text_dataSegment.configure(state='normal')
            text_codeSegment.configure(state='normal')
            text_sentencias.configure(state='normal')
            text_bien.configure(state='normal')

            text_dataSegment.delete("1.0", END)
            text_codeSegment.delete("1.0", END)
            text_sentencias.delete("1.0", END)
            text_bien.delete("1.0", END)

            for linea in contenido.split('\n'):
                # pasando cada linea al metodo show de analysisForLine.py y guardando los returns en estas cuatro variables
                lineaAnalizada, type_segment, lineNumber = show(linea)

                incorrectLines = [line for line,
                                  state in lineStates if not state]
                if not incorrectLines:
                    print("El código es correcto.")
                else:
                    print("El código es incorrecto en las líneas:", incorrectLines)

                if type_segment == 1:
                    text_dataSegment.insert(END, lineaAnalizada + '\n')
                elif type_segment == 2:
                    text_codeSegment.insert(END, lineaAnalizada + '\n')

                isString = False
                stringConstant = ''

                # Para cada linea separar en palabras cuando encuentre espacios, comas, dos puntos y punto
                for palabra in re.split(r'[ ,]', linea):

                    # Comprobando si la línea está en blanco (sin caracteres visibles)
                    if not palabra.strip():
                        continue

                    # pasando cada palabra al metodo lexemeAnalysis en analisysForLine.py
                    lexema, isString, comprobable = lexemeAnalysis(
                        palabra, isString)
                    # Comprobando si es un comentario
                    if comprobable == 'COMMENT':
                        text_sentencias.insert(
                            END, linea + '\t' + comprobable + '\n')
                        break
                    # Comprueba si una directiva empieza con '.', si es asi todo lo de adelante sera contado como directiva
                    if comprobable == '.DIRECTIVES':
                        text_sentencias.insert(
                            END, linea + '\t' + 'DIRECTIVES' + '\n')
                        break

                    # Comprueba si una macro o una función, si es asi todo lo de adelante es una macro o función
                    if comprobable == 'MACROS_AND_FUNCTIONS':
                        text_sentencias.insert(
                            END, linea + '\t' + comprobable + '\n')
                        break

                    # Comprobando si es una cadena, la primera vez que reciba STRING_CONSTANT, volvera isString = True, por lo que cada palabra siguiente la agregara
                    # a una lista para cuando vuelva a recibir STRING_CONSTANT cierre la cadena (isString = False) e imprima la lista con la cadena completa
                    if comprobable == "STRING_CONSTANT":
                        if isString == True:
                            stringConstant = stringConstant + lexema + '\t'
                            continue
                        if isString == False:
                            stringConstant = stringConstant + lexema + '\t'
                            text_sentencias.insert(
                                END, stringConstant + comprobable + '\n')
                            stringConstant = ''
                            continue
                    if isString == True:
                        stringConstant = stringConstant + lexema + '\t'
                        continue

                    # Insertando palabra
                    text_sentencias.insert(
                        END, lexema + '\t' + comprobable + '\n')

            text_dataSegment.configure(state='disable')
            text_codeSegment.configure(state='disable')
            text_sentencias.configure(state='disable')
            text_bien.configure(state='disable')

def saveFile():

    global statusName

    if statusName:

        textFile = open(statusName, 'w')
        textFile.write(textBox.get(1.0, END))
        textFile.close()
        print("Archivo guardado...")
        #Abrir de nuevo el archivo de la ruta statusName
        with open(statusName, 'r') as archivo:
        # Realiza operaciones en el archivo
            contenido = archivo.read()
            #print(contenido)
        text_dataSegment.configure(state='normal')
        text_codeSegment.configure(state='normal')
        text_sentencias.configure(state='normal')
        text_bien.configure(state='normal')

        text_dataSegment.delete("1.0", END)
        text_codeSegment.delete("1.0", END)
        text_sentencias.delete("1.0", END)
        text_bien.delete("1.0", END)

        for linea in contenido.split('\n'):
                # pasando cada linea al metodo show de analysisForLine.py y guardando los returns en estas cuatro variables
                lineaAnalizada, type_segment, lineNumber = show(linea)

                incorrectLines = [line for line,
                                  state in lineStates if not state]
                if not incorrectLines:
                    print("El código es correcto.")
                else:
                    print("El código es incorrecto en las líneas:", incorrectLines)

                if type_segment == 1:
                    text_dataSegment.insert(END, lineaAnalizada + '\n')
                elif type_segment == 2:
                    text_codeSegment.insert(END, lineaAnalizada + '\n')

                isString = False
                stringConstant = ''

                # Para cada linea separar en palabras cuando encuentre espacios, comas, dos puntos y punto
                for palabra in re.split(r'[ ,]', linea):

                    # Comprobando si la línea está en blanco (sin caracteres visibles)
                    if not palabra.strip():
                        continue

                    # pasando cada palabra al metodo lexemeAnalysis en analisysForLine.py
                    lexema, isString, comprobable = lexemeAnalysis(
                        palabra, isString)
                    # Comprobando si es un comentario
                    if comprobable == 'COMMENT':
                        text_sentencias.insert(
                            END, linea + '\t' + comprobable + '\n')
                        break
                    # Comprueba si una directiva empieza con '.', si es asi todo lo de adelante sera contado como directiva
                    if comprobable == '.DIRECTIVES':
                        text_sentencias.insert(
                            END, linea + '\t' + 'DIRECTIVES' + '\n')
                        break

                    # Comprueba si una macro o una función, si es asi todo lo de adelante es una macro o función
                    if comprobable == 'MACROS_AND_FUNCTIONS':
                        text_sentencias.insert(
                            END, linea + '\t' + comprobable + '\n')
                        break

                    # Comprobando si es una cadena, la primera vez que reciba STRING_CONSTANT, volvera isString = True, por lo que cada palabra siguiente la agregara
                    # a una lista para cuando vuelva a recibir STRING_CONSTANT cierre la cadena (isString = False) e imprima la lista con la cadena completa
                    if comprobable == "STRING_CONSTANT":
                        if isString == True:
                            stringConstant = stringConstant + lexema + '\t'
                            continue
                        if isString == False:
                            stringConstant = stringConstant + lexema + '\t'
                            text_sentencias.insert(
                                END, stringConstant + comprobable + '\n')
                            stringConstant = ''
                            continue
                    if isString == True:
                        stringConstant = stringConstant + lexema + '\t'
                        continue

                    # Insertando palabra
                    text_sentencias.insert(
                        END, lexema + '\t' + comprobable + '\n')

        text_dataSegment.configure(state='disable')
        text_codeSegment.configure(state='disable')
        text_sentencias.configure(state='disable')
        text_bien.configure(state='disable')

    else:
        saveAs()


def saveAs():
    # Cambiar el tipo de archivo por defecto a asm

    textFile = filedialog.asksaveasfilename(defaultextension=".txt", initialdir="/home/danielperez/Documents/Textos",
                                            title="Guardar archivo", filetypes=(("Archivos de texto", "*.txt"), ("Archivos de ensamblador", "*.asm")))

    if textFile:
        # Guardar el archivo
        with open(textFile, 'w') as file:
            file.write(textBox.get(1.0, END))
            statusBar.config(text="Archivo guardado...")

        textFile.close()


def closeFile():

    textBox.delete("1.0", END)
    textBox.configure(state='disabled')

    text_sentencias.configure(state='normal')
    text_sentencias.delete("1.0", END)
    text_sentencias.configure(state='disabled')

    text_codeSegment.configure(state='normal')
    text_codeSegment.delete("1.0", END)
    text_codeSegment.configure(state='disabled')

    text_dataSegment.configure(state='normal')
    text_dataSegment.delete("1.0", END)
    text_dataSegment.configure(state='disabled')

    text_bien.configure(state='normal')
    text_bien.delete("1.0", END)
    text_bien.configure(state='disabled')

    statusBar.config(text="Archivo cerrado...")


def cutText(e):
    global selected
    if e:
        selected = root.clipboard_get()
    else:
        if textBox.selection_get():
            # Obtener el texto seleccionado
            selected = textBox.selection_get()
            # Eliminar el texto seleccionado
            textBox.delete("sel.first", "sel.last")
            root.clipboard_clear()
            root.clipboard_append(selected)


def pasteText(e):
    global selected
    if e:
        selected = root.clipboard_get()

    else:
        if selected:
            position = textBox.index(INSERT)
            textBox.insert(position, selected)


def copyText(e):
    global selected
    if e:
        selected = root.clipboard_get()
    else:
        if textBox.selection_get():
            selected = textBox.selection_get()
            textBox.delete("sel.first", "sel.last")
            root.clipboard_clear()
            root.clipboard_append(selected)

# Frame izquierdo (Editor)
editor = Frame(root)
editor.grid(row=0, column=0, rowspan=3, columnspan=3, sticky='nsew')

scrollBar = Scrollbar(editor)
scrollBar.pack(side=RIGHT, fill=Y)

hScroll = Scrollbar(editor, orient="horizontal")
hScroll.pack(side=BOTTOM, fill=X)

textBox = Text(editor, width=97, height=25, font=("Courier", 14), undo=True, yscrollcommand=scrollBar.set, wrap="none",
               xscrollcommand=hScroll.set)
textBox.configure(state='disabled')
textBox.pack(fill='both', expand=True)

scrollBar.config(command=textBox.yview)
hScroll.config(command=textBox.xview)

# Frame derecho (Verificador, data segmente, code segment)

verificadores = Frame(root)
verificadores.grid(row=0, column=3, rowspan=3, columnspan=1, sticky='nsew')

sentencias = Frame(verificadores)
sentencias.grid(row=0, column=0, sticky='nsew')

dataSegment = Frame(verificadores)
dataSegment.grid(row=1, column=0, sticky='nsew')

codeSegment = Frame(verificadores)
codeSegment.grid(row=2, column=0, sticky='nsew')

bien = Frame(verificadores)
bien.grid(row=3, column=0, sticky='nsew')

# Instancia del menu y agregación de comandos

myMenu = Menu(root)
root.config(menu=myMenu)

fileMenu = Menu(myMenu)
myMenu.add_cascade(label="Archivo", menu=fileMenu)
fileMenu.add_command(label="Nuevo", command=newFile)
fileMenu.add_command(label="Abrir", command=openFile)
fileMenu.add_command(label="Guardar como", command=saveAs)
fileMenu.add_command(label="Guardar", command=saveFile)
fileMenu.add_command(label="Cerrar archivo", command=closeFile)
fileMenu.add_separator()
fileMenu.add_command(label="Salir", command=root.quit)

editMenu = Menu(myMenu, tearoff=False)
myMenu.add_cascade(label="Editar", menu=editMenu)
editMenu.add_command(label="Cortar", command=lambda: cutText(
    False), accelerator="(Ctrl+X)")
editMenu.add_command(label="Copiar", command=lambda: copyText(
    False), accelerator="(Ctrl+C)")
editMenu.add_command(label="Pegar", command=lambda: pasteText(
    False), accelerator="(Ctrl+V)")
editMenu.add_separator()
editMenu.add_command(
    label="Deshacer", command=textBox.edit_undo, accelerator="(Ctrl+Z)")
editMenu.add_command(
    label="Rehacer", command=textBox.edit_redo, accelerator="(Ctrl+Y)")

root.bind('<Control-Key-x>', cutText)
root.bind('<Control-Key-c>', copyText)
root.bind('<Control-Key-v>', pasteText)

# Barra de estado
statusBar = Label(root, text="Listo...", anchor=W)
statusBar.grid(row=3, column=0, columnspan=4, sticky='nsew')

# Scrollbars de los cuadros de texto de los verificadores

scrollBar_sentencias = Scrollbar(sentencias)
scrollBar_sentencias.pack(side=RIGHT, fill=Y)

hscrollbar_sentencias = Scrollbar(sentencias, orient=HORIZONTAL)
hscrollbar_sentencias.pack(side=BOTTOM, fill=X)

scrollbar_dataSegment = Scrollbar(dataSegment, orient=VERTICAL)
scrollbar_dataSegment.pack(side=RIGHT, fill=Y)

hscrollbar_dataSegment = Scrollbar(dataSegment, orient=HORIZONTAL)
hscrollbar_dataSegment.pack(side=BOTTOM, fill=X)

scrollbar_codeSegment = Scrollbar(codeSegment, orient=VERTICAL)
scrollbar_codeSegment.pack(side=RIGHT, fill=Y)

hscrollbar_codeSegment = Scrollbar(codeSegment, orient=HORIZONTAL)
hscrollbar_codeSegment.pack(side=BOTTOM, fill=X)

hScrollbar_bien = Scrollbar(bien, orient=HORIZONTAL)
hScrollbar_bien.pack(side=BOTTOM, fill=X)

scrollbar_bien = Scrollbar(bien, orient=VERTICAL)
scrollbar_bien.pack(side=RIGHT, fill=Y)

# Instancia de secciones

Label(sentencias, text="Verificador de sentencias").pack(
    fill='both', expand=True)

# Crear un cuadro de texto no editable debajo de la etiqueta en sentencias
text_sentencias = Text(sentencias, yscrollcommand=scrollBar_sentencias.set, wrap=NONE,
                       xscrollcommand=hscrollbar_sentencias.set, state='disabled', width=97, height=10)
text_sentencias.pack(fill='both', expand=True)

Label(dataSegment, text="Data Segment").pack(fill='both', expand=True)

# Crear un cuadro de texto no editable debajo de la etiqueta en dataSegment
text_dataSegment = Text(dataSegment, yscrollcommand=scrollbar_dataSegment.set, wrap=NONE,
                        xscrollcommand=hscrollbar_dataSegment.set, state='disabled', width=97, height=10)
text_dataSegment.pack(fill='both', expand=True)

Label(codeSegment, text="Code segment").pack(fill='both', expand=True)

# Crear un cuadro de texto no editable debajo de la etiqueta en codeSegment
text_codeSegment = Text(codeSegment, yscrollcommand=scrollbar_codeSegment.set, wrap=NONE,
                        xscrollcommand=hscrollbar_codeSegment.set, state='disabled', width=97, height=10)
text_codeSegment.pack(fill='both', expand=True)

Label(bien, text="'Ta Bien").pack(fill='both', expand=True)

text_bien = Text(bien, yscrollcommand=scrollbar_bien.set ,wrap=NONE,xscrollcommand=hScrollbar_bien.set,state='disabled', width=97, height=10)
text_bien.pack(fill='both', expand=True)



scrollBar_sentencias.config(command=text_sentencias.yview)
hscrollbar_sentencias.config(command=text_sentencias.xview)

scrollbar_dataSegment.config(command=text_dataSegment.yview)
hscrollbar_dataSegment.config(command=text_dataSegment.xview)

scrollbar_codeSegment.config(command=text_codeSegment.yview)
hscrollbar_codeSegment.config(command=text_codeSegment.xview)

hScrollbar_bien.config(command=text_bien.xview)
scrollbar_bien.config(command=text_bien.yview)


# Configuración de geometría de las filas y columnas para hacerlas proporcionales
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)


root.mainloop()
