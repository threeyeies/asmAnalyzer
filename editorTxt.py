from tkinter import *
from tkinter import filedialog
from tkinter import font

#Cambiar el directorio de acceso para uno de Windows
#Cambiar el tipo de archivos de abre de txt a asm}
#Agregar regleta y que se sombre la linea que se esta editando*
#Quitar codigo ineccesario para poder implementar en el proyecto final

global statusName
statusName = False

global selected
selected = False

def newFile():
  textBox.configure(state='normal')
  textBox.delete("1.0",END)
  statusBar.config(text="Nuevo archivo...")

def openFile():
   textBox.configure(state='normal')
   textBox.delete("1.0",END)

   #Abrir el explorador de archivos
   textFile = filedialog.askopenfilename(initialdir="/home/danielperez/Documents/Textos",title="Abrir archivo",filetypes=(("Archivos de texto","*.txt"),("Archivos de ensamblador","*.asm")))
   
   if textFile:
    global statusName
    statusName = textFile
   
   #Abrir el archivo
   textFile = open(textFile,'r')
   contenido = textFile.read()
   textBox.insert(END,contenido)
   statusBar.config(text="Archivo abierto...")
   textFile.close()
  

def saveFile():
   
   global statusName

   if statusName:

    textFile = open(statusName,'w')
    textFile.write(textBox.get(1.0,END))
    textFile.close()

   else:
    saveAs()
       
def saveAs():
    #Cambiar el tipo de archivo por defecto a asm
    textFile = filedialog.asksaveasfilename(defaultextension=".txt",initialdir="/home/danielperez/Documents/Textos",title="Guardar archivo",filetypes=(("Archivos de texto","*.txt"),("Archivos de ensamblador","*.asm")))
    
    if textFile:
        #guardar el archivo

        textFile = open(textFile,'w')
        textFile.write(textBox.get(1.0,END))
        statusBar.config(text="Archivo guardado...")
        textFile.close()

def closeFile():

    textBox.delete("1.0",END)
    textBox.configure(state='disabled')
    statusBar.config(text="Archivo cerrado...")

def cutText(e):
    global selected
    if e:
       selected = contenedor.clipboard_get()
    else:
     if textBox.selection_get():
        #Obtener el texto seleccionado
        selected = textBox.selection_get()
        #Eliminar el texto seleccionado
        textBox.delete("sel.first","sel.last")
        contenedor.clipboard_clear()
        contenedor.clipboard_append(selected)
        
def pasteText(e):
    global selected
    if e:
        selected = contenedor.clipboard_get()
    
    else:
     if selected:
      position = textBox.index(INSERT)
      textBox.insert(position,selected)

def copyText(e):
    global selected
    if e:
       selected = contenedor.clipboard_get()

    if textBox.selection_get():
        #Obtener el texto seleccionado
        selected = textBox.selection_get()
        contenedor.clipboard_clear()
        contenedor.clipboard_append(selected)
        
contenedor = Tk()
contenedor.title("Editor de texto")
contenedor.geometry("750x550")

frame1 = Frame(contenedor)
frame1.pack(pady=5)

scrollBar = Scrollbar(frame1)
scrollBar.pack(side=RIGHT,fill=Y)

hScroll = Scrollbar(frame1,orient="horizontal")
hScroll.pack(side=BOTTOM,fill=X)

textBox = Text(frame1,width=97,height=25,font=("Courier",14),undo=True,yscrollcommand=scrollBar.set,wrap="none",xscrollcommand=hScroll.set)
textBox.configure(state='disabled')
textBox.pack()

scrollBar.config(command=textBox.yview)
hScroll.config(command=textBox.xview)

myMenu = Menu(contenedor)
contenedor.config(menu=myMenu)

fileMenu = Menu(myMenu)
myMenu.add_cascade(label="Archivo",menu=fileMenu)
fileMenu.add_command(label="Nuevo",command=newFile)
fileMenu.add_command(label="Abrir",command=openFile)
fileMenu.add_command(label="Guardar como",command=saveAs)
fileMenu.add_command(label="Guardar",command=saveFile)
fileMenu.add_command(label="Cerrar archivo",command=closeFile)
fileMenu.add_separator()
fileMenu.add_command(label="Salir",command=contenedor.quit)

editMenu = Menu(myMenu,tearoff=False)
myMenu.add_cascade(label="Editar",menu=editMenu)
editMenu.add_command(label="Cortar",command=lambda:cutText(False),accelerator="(Ctrl+X)")
editMenu.add_command(label="Copiar",command=lambda:copyText(False),accelerator="(Ctrl+C)")
editMenu.add_command(label="Pegar",command=lambda:pasteText(False),accelerator="(Ctrl+V)")
editMenu.add_separator()
editMenu.add_command(label="Deshacer",command=textBox.edit_undo,accelerator="(Ctrl+Z)")
editMenu.add_command(label="Rehacer",command=textBox.edit_redo,accelerator="(Ctrl+Y)")

contenedor.bind('<Control-Key-x>',cutText)
contenedor.bind('<Control-Key-c>',copyText)
contenedor.bind('<Control-Key-v>',pasteText)

#Barra de estado
statusBar = Label(contenedor,text="Listo...",anchor=W)
statusBar.pack(side=BOTTOM,fill=X,ipady=5)

contenedor.mainloop()