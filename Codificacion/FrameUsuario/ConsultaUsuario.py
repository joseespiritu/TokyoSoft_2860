#Implementacion de marco principal de registro de producto
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox #funcion de tkinter que permite la visualización de ventanas emergentes

#definicion de frame 
ventana_usuario=tk.Tk()
ventana_usuario.title("Inventario Admin")
ventana_usuario.geometry("650x350")

#definiendo contenedor
cuadroUsuario=Frame(ventana_usuario)
cuadroUsuario.pack(fill="both",expand="True")

#inicialización de la barra del menu
barraMenu=Menu(ventana_usuario)
ventana_usuario.config(menu=barraMenu, width=300, height=300)

NombreAdmin_etiqueta=Label(cuadroUsuario,text="Bienvenido Admin:")
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

botonEditar=Button(cuadroUsuario,text="Funciones Usuarios")
botonEditar.grid(row=2,column=5,padx=10,pady=10)

botonEliminar=Button(cuadroUsuario,text="Funciones Productos")
botonEliminar.grid(row=2,column=6,padx=10,pady=10)


#-----------------------------BARRA DE MENU----------------------------------
ayudaMenu=Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de...")
ayudaMenu.add_command(label="Salir")

barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)




#Creacion de la tabla para visualizar los datos

#Tabla_usuario=ttk.Treeview(cuadroUsuario)
#Tabla_usuario['columns']=('ID','Nombre Producto','Lugar','Precio')
#Tabla_usuario.grid(row=4,column=0,columnspan=2)
#Tabla_usuario.heading('#0',text='ID',anchor= CENTER)
#Tabla_usuario.heading('#1',text='Nombre producto',anchor=CENTER)
#Tabla_usuario.heading('#2',text='Lugar',anchor= CENTER)
#Tabla_usuario.heading('#3',text='Precio unitario',anchor= CENTER)#
ventana_usuario.mainloop();