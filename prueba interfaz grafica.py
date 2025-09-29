import tkinter as tk

ventana = tk.Tk()
ventana.title("Entrada de texto")

entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack()

entrada_apellido = tk.Entry(ventana)
entrada_apellido.pack()

def mostrar():
    nombre = entrada_nombre.get()
    apellido = entrada_apellido.get()
    etiqueta.config(text=f"NOMBRE COMPLETO: {nombre.upper()} {apellido.upper()}\nLETRAS DEL NOMBRE: {len(nombre)}")

etiqueta = tk.Label(ventana, text="")
etiqueta.pack()

boton = tk.Button(ventana, text="Mostrar", command=mostrar)
boton.pack()

ventana.mainloop()
