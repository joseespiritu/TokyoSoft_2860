#Implementacion de marco principal de registro de producto
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox #funcion de tkinter que permite la visualización de ventanas emergentes

#definicion de frame 
ventana_usuario=tk.Tk()
ventana_usuario.title("Inventario Usuarios")
ventana_usuario.geometry("450x350")
ventana_usuario.iconbitmap("tokyo.ico")

#definiendo contenedor
cuadroUsuario=Frame(ventana_usuario)
cuadroUsuario.pack(fill="both",expand="True")

#inicialización de la barra del menu
barraMenu=Menu(ventana_usuario)
ventana_usuario.config(menu=barraMenu, width=300, height=300)

#-------------------FUNCIONES----------------------
def salirAplicacion():
	valor=messagebox.askquestion("salir","¿Deseas salir de la aplicacion?")
	if valor=="yes":
		ventana_usuario.destroy()

def acercaDe():
	messagebox.showinfo("Acerca de...","Proyecto Sistema Registro de Inventario de Productos")

def Licencia():
	messagebox.showinfo("Licencia","Tokyo soft 2019 Todos los derechos reservados")



NombreAdmin_etiqueta=Label(cuadroUsuario,text="Bienvenido Usuario:")
NombreAdmin_etiqueta.grid(row=0,column=0,sticky='e',padx=10,pady=10)

busquedaEspecifica_campo=Entry(cuadroUsuario)
busquedaEspecifica_campo.grid(row=2,column=0,padx=10,pady=10)
busquedaEspecifica_campo=ttk.Label(busquedaEspecifica_campo,text="Busqueda especifica")
busquedaEspecifica_campo.grid(row=2,column=0)

botonBuscar=Button(cuadroUsuario, text="Buscar")
botonBuscar.grid(row=2,column=1,padx=10,pady=10)

cuadroUsuario_combo=ttk.Combobox(cuadroUsuario,width=15)
cuadroUsuario_combo['values']=("Ascendente","Descendente")
cuadroUsuario_combo.grid(row=2,column=3)

botonOrdena=Button(cuadroUsuario,text="Aplicar")
botonOrdena.grid(row=2,column=4,padx=10,pady=10)


#-----------------------------BARRA DE MENU----------------------------------
ayudaMenu=Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia", command=Licencia)
ayudaMenu.add_command(label="Acerca de...", command=acercaDe)
ayudaMenu.add_command(label="Salir", command=salirAplicacion)

barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

ventana_usuario.mainloop();