#Implementacion de marco principal de registro de producto
from tkinter import *
import tkinter as tk
from tkinter import messagebox #Ventanas emergentes
import sqlite3

ventana=tk.Tk()
ventana.title("Registro de producto")
ventana.resizable (0,0)
ventana.geometry("350x350")
ventana.iconbitmap("tokyo.ico")

barraMenu=Menu(ventana)
ventana.config(menu=barraMenu, width=300, height=300)


#-------------------FUNCIONES DE LA VENTANA--------------------------
def conexionBBDD():
	miConexion=sqlite3.connect("Productos")
	miCursor=miConexion.cursor()
	try:
		miCursor.execute('''
			CREATE TABLE DATOSPRODUCTOS (
			ID INTEGER PRIMARY KEY AUTOINCREMENT,
			NOMBRE_PRODUCTO VARCHAR(50), 
			PRECIO_PRODUCTO INTEGER,
			CANTIDAD_PRODUCTO INTEGER, 
			TIPO_PRODUCTO VARCHAR(60),
			EXISTENCIA_PRODUCTO INTEGER)
			''')

		messagebox.showinfo("BBDD","BBDD creada con exito")
	except:
		messagebox.showwarning("!Atencion!","La BBDD ya existe")

def salirAplicacion():
	valor=messagebox.askquestion("Salir","¿deseas salir de la aplicacion?")
	if valor=="yes":
		ventana.destroy()
	
def limpiarCampos():
	IdProducto.set("")
	NombreProducto.set("")
	PrecioProducto.set("")
	CantidadProducto.set("")
	TipoProducto.set("")
	ExistenciaProducto.set("")

def crear():
	miConexion=sqlite3.connect("Productos")
	miCursor=miConexion.cursor()
	#CONSULTAS PARAMETRIZADAS EVITA INYECCIONES SQL
	datos=NombreProducto.get(),PrecioProducto.get(),CantidadProducto.get(),TipoProducto.get(),ExistenciaProducto.get()

	miCursor.execute("INSERT INTO DATOSPRODUCTOS VALUES(NULL,?,?,?,?,?)",(datos))

	miConexion.commit()
	messagebox.showinfo("BBDD", "Registro insertado con exito")

def leer():
	miConexion=sqlite3.connect("Productos")
	miCursor=miConexion.cursor()
	miCursor.execute("SELECT * FROM DATOSPRODUCTOS WHERE ID=" + IdProducto.get())
	elProducto=miCursor.fetchall()
	for producto in elProducto:
		IdProducto.set(producto[0])
		NombreProducto.set(producto[1])
		PrecioProducto.set(producto[2])
		CantidadProducto.set(producto[3])
		TipoProducto.set(producto[4])
		ExistenciaProducto.set(producto[5])
	miConexion.commit()	


def actualizar():
	miConexion=sqlite3.connect("Productos")
	miCursor=miConexion.cursor()
	miCursor.execute("UPDATE DATOSPRODUCTOS SET NOMBRE_PRODUCTO='" + NombreProducto.get() + 
		"', PRECIO_PRODUCTO='" + PrecioProducto.get() + 
		"', CANTIDAD_PRODUCTO='" + CantidadProducto.get() + 
		"', TIPO_PRODUCTO= ' " + TipoProducto.get() + 
		"', EXISTENCIA_PRODUCTO ='" + ExistenciaProducto.get()+
		"'WHERE ID="+ IdProducto.get())

	miConexion.commit()
	messagebox.showinfo("BBDD", "Registro actualizado con exito")

def eliminar():
	miConexion=sqlite3.connect("Productos")
	miCursor=miConexion.cursor()
	miCursor.execute("DELETE FROM DATOSPRODUCTOS WHERE ID=" + IdProducto.get())
	miConexion.commit()
	messagebox.showinfo("BBDD","Registro borrado con exito")
	

def acercaDe():
	messagebox.showinfo("Acerca de...","Proyecto Sistema Registro de Inventario de Productos")

def Licencia():
	messagebox.showinfo("Licencia","Tokyo soft 2019 Todos los derechos reservados")


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
IdProducto=StringVar()
NombreProducto=StringVar()
PrecioProducto=StringVar()
CantidadProducto=StringVar()
TipoProducto=StringVar()
ExistenciaProducto=StringVar()

IdProducto_campo=Entry(cuadroRegistro,textvariable=IdProducto)
IdProducto_campo.grid(row=0,column=1,padx=10,pady=15)

NombreProducto_campo=Entry(cuadroRegistro,textvariable=NombreProducto)
NombreProducto_campo.grid(row=1,column=1,padx=10,pady=15)

PrecioProducto_campo=Entry(cuadroRegistro,textvariable=PrecioProducto)
PrecioProducto_campo.grid(row=2,column=1,padx=10,pady=15)

CantidadProducto_campo=Entry(cuadroRegistro,textvariable=CantidadProducto)
CantidadProducto_campo.grid(row=3,column=1,padx=10,pady=15)

TipoProducto_campo=Entry(cuadroRegistro,textvariable=TipoProducto)
TipoProducto_campo.grid(row=4,column=1,padx=10,pady=15)

ExistenciaProducto_campo=Entry(cuadroRegistro,textvariable=ExistenciaProducto)
ExistenciaProducto_campo.grid(row=5,column=1,padx=10,pady=15)

#-----------------------------BARRA DE MENU----------------------------------
bbddMenu=Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar",command=conexionBBDD)
bbddMenu.add_command(label="Salir",command=salirAplicacion)

borrarMenu=Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar campos",command=limpiarCampos)

crudMenu=Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Crear",command=crear)
crudMenu.add_command(label="Leer",command=leer)
crudMenu.add_command(label="Actualizar",command=actualizar)
crudMenu.add_command(label="Borrar",command=eliminar)

ayudaMenu=Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia", command=Licencia)
ayudaMenu.add_command(label="Acerca de...", command=acercaDe)

barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

ventana.mainloop()