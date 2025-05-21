# interfaz_jose.py
import tkinter as tk
from tkinter import messagebox, simpledialog
import main  # Importa las funciones desde main.py

def lanzar_interfaz():
    ventana = tk.Tk()
    ventana.title("Gestor de Recetas")
    ventana.geometry("420x300")

    tk.Label(ventana, text="Nombre de la receta:").pack(pady=10)
    entry_nombre = tk.Entry(ventana, width=40)
    entry_nombre.pack()

    def registrar():
        nombre = entry_nombre.get()
        main.registrar_receta(nombre)
        entry_nombre.delete(0, tk.END)

    tk.Button(ventana, text="Registrar Receta", command=registrar).pack(pady=5)
    tk.Button(ventana, text="Ver receta por número", command=main.ver_receta_por_numero).pack(pady=5)
    tk.Button(ventana, text="Eliminar receta", command=main.eliminar_receta).pack(pady=5)
    tk.Button(ventana, text="Mostrar todas", command=main.mostrar_todas).pack(pady=5)

    ventana.mainloop()

if __name__ == "__main__":
    lanzar_interfaz()
