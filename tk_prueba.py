import math                                                                    # math.ceil # pasa al valor siguiente 
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk

#-----------------------------------------------------------------------------------------------------------
ventana = tk.Tk()                                                              # Se crea la ventana
ventana.title("PV calculator")                                                 # Título de la ventana
ventana.resizable(0,0)                                                         # No deja redimensionar 
ventana.config(width=800, height=620)                                          # Dimensiones
ventana.config(bg='white')                                                     # color del fondo
#-----------------------------------------------------------------------------------------------------------------

entry = ttk.Label(text="CALCULADORA DE SISTEMAS FOTOVOLTAICOS")                # Nombre de la etiqueta
entry.place(x=250, y=10)                                                       # Posición de la etiqueta
#----------------------------------------------------------------------------------------------------------------
entry = ttk.Label(text="Datos baterías")                                       # Nombre de la etiqueta
entry.place(x=70, y=292)                                                       # Posición de la etiqueta
#--------------------------------- Pedir voltaje de baterias ----------------------------------------------
etiqueta_voltaje_baterias = ttk.Label(text="Voltaje Baterías(V):")             # Nombre de la etiqueta
etiqueta_voltaje_baterias.place(x=70, y=317)                                   # Posición de la etiqueta
#--------------------------------- Caja para voltaje de baterias ----------------------------------------------
list1 = ["2", "6", "12", "24", "48"]
caja_voltaje_baterias = ttk.Combobox(values= list1, state="readonly")          # Creación de la caja con los valores
caja_voltaje_baterias.place(x=174, y=316, width=50)                            # Posición y ancho de la caja

ventana.mainloop()                                                             # Se cierra el bucle