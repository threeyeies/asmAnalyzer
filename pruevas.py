import tkinter as tk

def on_content_change(event=None):
    # Esta función se llamará cada vez que el contenido del cuadro de texto cambie
    content = text_widget.get("1.0", "end-1c")  # Obtener todo el contenido del Text
    print("Contenido modificado:", content)

# Crear la ventana principal
root = tk.Tk()
root.title("Detectar cambios en TextBox")

# Crear un cuadro de texto
text_widget = tk.Text(root, width=30, height=10)
text_widget.pack(padx=10, pady=10)

# Asociar la función `on_content_change` al evento de modificación del cuadro de texto
text_widget.bind("<KeyRelease>", on_content_change)

# Ejecutar el bucle principal
root.mainloop()
