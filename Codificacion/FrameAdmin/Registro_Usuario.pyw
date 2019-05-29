from tkinter import *
from tkinter import messagebox #Ventanas emergentes

raiz=Tk()
raiz.title("Registro de Usuario")
raiz.resizable(0,0)
raiz.geometry("350x350")

#CUADRO DE VISUALIZACION
CuadroUsuario=Frame(raiz)
CuadroUsuario.pack(fill="both",expand="True")

barraMenu=Menu(raiz)
raiz.config(menu=barraMenu, width=200, height=200)

#-------------------FUNCIONES DE LA VENTANA--------------------------
def acercaDe():
	messagebox.showinfo("Acerca de...","Proyecto Sistema Registro de Inventario de Productos")

def Licencia():
	messagebox.showinfo("Licencia","Tokyo soft 2019 Todos los derechos reservados")



#---------------------ETIQUETAS DE TEXTO-------------------------------
IdusuarioLabel=Label(CuadroUsuario, text="ID:")
IdusuarioLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

NombreUsuarioLabel=Label(CuadroUsuario, text="Usuario:")
NombreUsuarioLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

TipoUsuarioLabel=Label(CuadroUsuario, text="Tipo de usuario:")
TipoUsuarioLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

CorreoUsuarioLabel=Label(CuadroUsuario, text="Correo electronico:")
CorreoUsuarioLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

CelUsuarioLabel=Label(CuadroUsuario, text="Celular:")
CelUsuarioLabel.grid(row=5, column=0, sticky="e", padx=10, pady=10)

PassUsuarioLabel=Label(CuadroUsuario, text="Contraseña:")
PassUsuarioLabel.grid(row=6, column=0, sticky="e", padx=10, pady=10)

#------------------------CAJAS DE TEXTO------------------------------------------
CuadroIdUsuario=Entry(CuadroUsuario)
CuadroIdUsuario.grid(row=1, column=1, padx=10, pady=10)

CuadroNombreUsuario=Entry(CuadroUsuario)
CuadroNombreUsuario.grid(row=2, column=1, padx=10, pady=10)

CuadroTipoUsuario=Entry(CuadroUsuario)
CuadroTipoUsuario.grid(row=3, column=1, padx=10, pady=10)

CuadroCorreoUsuario=Entry(CuadroUsuario)
CuadroCorreoUsuario.grid(row=4, column=1, padx=10, pady=10)

CuadroCelUsuario=Entry(CuadroUsuario)
CuadroCelUsuario.grid(row=5, column=1, padx=10, pady=10)

CuadroPassUsuario=Entry(CuadroUsuario)
CuadroPassUsuario.grid(row=6, column=1, padx=10, pady=10)

#----------------------------BOTON-----------------------------------------
botonAcceso=Button(CuadroUsuario, text="Aceptar")
botonAcceso.grid(row=7, column=1, padx=10, pady=10)


#-----------------------------BARRA DE MENU----------------------------------
bbddMenu=Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar")
bbddMenu.add_command(label="Salir")

borrarMenu=Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar campos")

crudMenu=Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Crear")
crudMenu.add_command(label="Leer")
crudMenu.add_command(label="Actualizar")
crudMenu.add_command(label="Borrar")

ayudaMenu=Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia", command=Licencia)
ayudaMenu.add_command(label="Acerca de...", command=acercaDe)

barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

raiz.mainloop()