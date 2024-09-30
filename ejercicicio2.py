import tkinter as tk

ventana = tk.Tk()
ventana.title("Interfaces gráficas de usuario.")
ventana.geometry("400x300")

etiqueta_bienvenida = tk.Label(ventana, text="Bienvenidos.")
etiqueta_bienvenida.pack()

etiqueta_integrantes = tk.Label(ventana, text="Integrantes: Victoria Flores, Anita Jaime")
etiqueta_integrantes.pack()

etiqueta_info = tk.Label(ventana, text="Curso: 5to año - Materia: Programación - Colegio: divina misericordia")
etiqueta_info.pack()

ventana.mainloop()
