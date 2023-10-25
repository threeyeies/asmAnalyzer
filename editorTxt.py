from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from screeninfo import get_monitors
from tkinter import font
from ttkthemes import ThemedTk
from analysisForLine import show

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
root.iconbitmap("Akane.ico")  # Icono
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
        initialdir="/home/danielperez/Documents/Textos",
        title="Abrir archivo",
        filetypes=(("Archivos de ensamblador", "*.asm"),
                   ("Archivos de texto", "*.txt"))
    )

    if textFile:
        global statusName
        global lineaAnalizada
        statusName = textFile

        with open(textFile, 'r') as file:
            contenido = file.read()
            textBox.insert(END, contenido)
            statusBar.config(text="Archivo abierto...")

            # pasando cada linea al analysisForLine
            text_dataSegment.configure(state='normal')
            text_codeSegment.configure(state='normal')
            for linea in contenido.split('\n'):
                lineaAnalizada, type_segment = show(linea)
                if type_segment == 1:
                    text_dataSegment.insert(END, lineaAnalizada + '\n')
                elif type_segment == 2:
                    text_codeSegment.insert(END, lineaAnalizada + '\n')
            text_dataSegment.configure(state='disable')
            text_codeSegment.configure(state='disable')


def saveFile():

    global statusName

    if statusName:

        textFile = open(statusName, 'w')
        textFile.write(textBox.get(1.0, END))
        textFile.close()

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
scrollBards = Scrollbar(dataSegment)
scrollBards.pack(side=RIGHT, fill=Y)
hScrollds = Scrollbar(dataSegment, orient="horizontal")
hScrollds.pack(side=BOTTOM, fill=X)
text_dataSegment = Text(dataSegment, width=97, height=25, font=("Courier", 14), undo=True, yscrollcommand=scrollBards.set, wrap="none",
                        xscrollcommand=hScrollds.set)
scrollBards.config(command=text_dataSegment.yview)
hScrollds.config(command=text_dataSegment.xview)


codeSegment = Frame(verificadores)
codeSegment.grid(row=2, column=0, sticky='nsew')
scrollBarcs = Scrollbar(codeSegment)
scrollBar.pack(side=RIGHT, fill=Y)
hScrollcs = Scrollbar(codeSegment, orient="horizontal")
hScrollcs.pack(side=BOTTOM, fill=X)
text_codeSegment = Text(codeSegment, width=97, height=25, font=("Courier", 14), undo=True, yscrollcommand=scrollBarcs.set, wrap="none",
                        xscrollcommand=hScrollcs.set)
scrollBarcs.config(command=text_codeSegment.yview)
hScrollcs.config(command=text_codeSegment.xview)

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

# Instancia de secciones

Label(sentencias, text="Verificador de sentencias").pack(
    fill='both', expand=True)

# Crear un cuadro de texto no editable debajo de la etiqueta en sentencias
text_sentencias = Text(sentencias, wrap=NONE,
                       state='disabled', width=97, height=10)
text_sentencias.pack(fill='both', expand=True)

Label(dataSegment, text="Data Segment").pack(fill='both', expand=True)

# Crear un cuadro de texto no editable debajo de la etiqueta en dataSegment
text_dataSegment = Text(dataSegment, wrap=NONE,
                        state='disabled', width=97, height=10)
text_dataSegment.pack(fill='both', expand=True)

Label(codeSegment, text="Code segment").pack(fill='both', expand=True)

# Crear un cuadro de texto no editable debajo de la etiqueta en codeSegment
text_codeSegment = Text(codeSegment, wrap=NONE,
                        state='disabled', width=97, height=10)
text_codeSegment.pack(fill='both', expand=True)

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
