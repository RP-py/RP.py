import tkinter as tk 
from tkinter import messagebox

def enviar():
    nombre = entry_nombre.get().strip()
    genero = genero_var.get()
    acepta = acepta_var.get()

    if not nombre:
        resultado.config(text="escribe tu nombre", fg="red")
        return
    if not acepta:
        resultado.config(text="debes aceptar los términos", fg="red")
        return

    resultado.config(
        text=f"Nombre: {nombre} | Género: {genero}",
        fg="green"
    )

ventana = tk.Tk()
ventana.title("Formulario de Usuario")
ventana.geometry("350x300")

tk.Label(ventana, text="Escribe tu nombre completo:").pack(pady=(10, 2))

entry_nombre = tk.Entry(ventana, width=40)
entry_nombre.pack(pady=(0, 10))

genero_var = tk.StringVar(value="Masculino")  # Valor por defecto
tk.Label(ventana, text="Género:").pack()
tk.Radiobutton(ventana, text="Masculino", variable=genero_var, value="Masculino").pack()
tk.Radiobutton(ventana, text="Femenino", variable=genero_var, value="Femenino").pack()
tk.Radiobutton(ventana, text="Otro", variable=genero_var, value="Otro").pack()

acepta_var = tk.BooleanVar()
tk.Checkbutton(ventana, text="Acepto los términos", variable=acepta_var).pack(pady=5)

tk.Button(ventana, text="Enviar", command=enviar).pack(pady=10)

resultado = tk.Label(ventana, text="", fg="green")
resultado.pack()

ventana.mainloop()
