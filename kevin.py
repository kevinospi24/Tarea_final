# main.py
import csv
import random
import math
import pandas as pd
import os
from tkinter import messagebox, simpledialog

archivo_csv = 'recetas.csv'
campos = ['etiqueta', 'parametro', 'valor_base', 'resultado']

def registrar_receta(nombre):
    if not nombre:
        messagebox.showerror("Error", "Nombre vacío")
        return
    tiempo = random.randint(15, 90)
    resultado = round(tiempo * 1.8 + 32, 2)
    fila = {
        'etiqueta': nombre,
        'parametro': 'minutos',
        'valor_base': tiempo,
        'resultado': resultado
    }
    existe = os.path.isfile(archivo_csv)
    with open(archivo_csv, 'a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=campos)
        if not existe:
            writer.writeheader()
        writer.writerow(fila)
    messagebox.showinfo("Registrado", f"{nombre} → {tiempo} min / {resultado} °F")

def ver_receta_por_numero():
    if not os.path.isfile(archivo_csv):
        messagebox.showinfo("Sin datos", "No hay recetas guardadas.")
        return
    try:
        numero = int(simpledialog.askstring("Buscar", "Número de receta:"))
        df = pd.read_csv(archivo_csv)
        if 1 <= numero <= len(df):
            r = df.iloc[numero - 1]
            msg = f"{r['etiqueta']}\nTiempo: {r['valor_base']} min\n°F: {r['resultado']}"
            messagebox.showinfo("Receta", msg)
        else:
            messagebox.showerror("Error", "Número fuera de rango.")
    except:
        messagebox.showerror("Error", "Entrada inválida.")

def eliminar_receta():
    if not os.path.isfile(archivo_csv):
        messagebox.showinfo("Sin datos", "No hay recetas.")
        return
    try:
        numero = int(simpledialog.askstring("Eliminar", "Número de receta:"))
        df = pd.read_csv(archivo_csv)
        if 1 <= numero <= len(df):
            df = df.drop(index=numero - 1)
            df.to_csv(archivo_csv, index=False)
            messagebox.showinfo("Éxito", "Receta eliminada.")
        else:
            messagebox.showerror("Error", "Número fuera de rango.")
    except:
        messagebox.showerror("Error", "Entrada inválida.")

def mostrar_todas():
    if os.path.isfile(archivo_csv):
        df = pd.read_csv(archivo_csv)
        messagebox.showinfo("Recetas", df.to_string(index=False))
    else:
        messagebox.showinfo("Sin datos", "Archivo no encontrado.")
