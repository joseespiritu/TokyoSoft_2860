#Implementacion de marco principal de registro de producto
from tkinter import *
from tkinter import ttk
import tkinter as tk

ventana_usuario=tk.Tk()
ventana_usuario.title("Inventario Admin")
ventana_usuario.geometry("650x350")

cuadroUsuario=Frame(ventana_usuario)
cuadroUsuario.pack(fill="both",expand="True")


NombreAdmin_etiqueta=Label(cuadroUsuario,text="Bien venido Admin:")
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

botonEditar=Button(cuadroUsuario,text="Editar")
botonEditar.grid(row=3,column=4,padx=10,pady=10)

botonEliminar=Button(cuadroUsuario,text="Eliminar")
botonEliminar.grid(row=4,column=4,padx=10,pady=10)
 
botonCrear=Button(cuadroUsuario,text="Crear")
botonCrear.grid(row=5,column=4,padx=10,pady=10)

botonActualizar=Button(cuadroUsuario,text="Actualizar")
botonActualizar.grid(row=6,column=4,padx=10,pady=10)

#Creacion de la tabla para visualizar los datos

#Tabla_usuario=ttk.Treeview(cuadroUsuario)
#Tabla_usuario['columns']=('ID','Nombre Producto','Lugar','Precio')
#Tabla_usuario.grid(row=4,column=0,columnspan=2)
#Tabla_usuario.heading('#0',text='ID',anchor= CENTER)
#Tabla_usuario.heading('#1',text='Nombre producto',anchor=CENTER)
#Tabla_usuario.heading('#2',text='Lugar',anchor= CENTER)
#Tabla_usuario.heading('#3',text='Precio unitario',anchor= CENTER)#
ventana_usuario.mainloop();