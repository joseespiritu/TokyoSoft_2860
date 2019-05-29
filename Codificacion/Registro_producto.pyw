#Implementacion de marco principal de registro de producto
from tkinter import *
import tkinter as tk
ventana=tk.Tk()
ventana.title("Registro de producto")
ventana.geometry("350x350")


#Implementacion de panel que contendra los campos 
cuadroRegistro=Frame(ventana)
cuadroRegistro.pack(fill="both",expand="True")

#Implamentacion de etiquetas
Id_etiqueta=Label(cuadroRegistro,text="Id producto")
Id_etiqueta.grid(row=0,column=0,sticky="e",padx=10,pady=10)

NombreProducto_etiqueta=Label(cuadroRegistro,text="Nombre producto")
NombreProducto_etiqueta.grid(row=1,column=0,sticky="e",padx=10,pady=10)

PrecioProducto_etiqueta=Label(cuadroRegistro,text="Precio producto")
PrecioProducto_etiqueta.grid(row=2,column=0,sticky="e",padx=10,pady=10)

CantidadProducto_etiqueta=Label(cuadroRegistro,text="Cantidad producto")
CantidadProducto_etiqueta.grid(row=3,column=0,sticky="e",padx=10,pady=10)

TipoProducto_etiqueta=Label(cuadroRegistro,text="Tipo producto")
TipoProducto_etiqueta.grid(row=4,column=0,sticky="e",padx=10,pady=10)

ExistenciaProducto_etiqueta=Label(cuadroRegistro,text="Existencia producto")
ExistenciaProducto_etiqueta.grid(row=5,column=0,sticky="e",padx=10,pady=10)

#Implementacion de los campos de captura
IdProducto_campo=Entry(cuadroRegistro)
IdProducto_campo.grid(row=0,column=1,padx=10,pady=15)

NombreProducto_campo=Entry(cuadroRegistro)
NombreProducto_campo.grid(row=1,column=1,padx=10,pady=15)

PrecioProducto_campo=Entry(cuadroRegistro)
PrecioProducto_campo.grid(row=2,column=1,padx=10,pady=15)

CantidadProducto_campo=Entry(cuadroRegistro)
CantidadProducto_campo.grid(row=3,column=1,padx=10,pady=15)

TipoProducto_campo=Entry(cuadroRegistro)
TipoProducto_campo.grid(row=4,column=1,padx=10,pady=15)

ExistenciaProducto_campo=Entry(cuadroRegistro)
ExistenciaProducto_campo.grid(row=5,column=1,padx=10,pady=15)

#inplementacion del boton para aceptar cambios

botonAceptar=Button(cuadroRegistro,text="Aceptar")
botonAceptar.grid(row=6, column=1, padx=10, pady=10)

ventana.mainloop()