from tkinter import *
from tkinter import messagebox #Ventanas emergentes
import sqlite3

raiz=Tk()
raiz.title("Registro de Usuario")
raiz.resizable(0,0)
raiz.geometry("350x350")
raiz.iconbitmap("tokyo.ico")

#CUADRO DE VISUALIZACION
CuadroUsuario=Frame(raiz)
CuadroUsuario.pack(fill="both",expand="True")

barraMenu=Menu(raiz)
raiz.config(menu=barraMenu, width=200, height=200)

#-------------------FUNCIONES DE LA VENTANA--------------------------
def conexionBBDD():
	miConexion=sqlite3.connect("Usuarios")
	miCursor=miConexion.cursor()

	try:
		miCursor.execute('''
			CREATE TABLE DATOSUSUARIOS (
			ID INTEGER PRIMARY KEY AUTOINCREMENT,
			NOMBRE_USUARIO VARCHAR(50),
			TIPO_USUARIO INTEGER,
			CORREO_ELECTRONICO VARCHAR(60),
			TELEFONO INTEGER,
			PASSWORD VARCHAR(20))
			''')
		messagebox.showinfo("BBDD","BBDD creada con exito")
	except:
		messagebox.showwarning("!Atencion!","La BBDD ya existe")

def salirAplicacion():
	valor=messagebox.askquestion("salir","¿Deseas salir de la aplicacion?")
	if valor=="yes":
		raiz.destroy()

def limpiarCampos():
	miID.set("")
	miNombre.set("")
	miTipoUsuario.set("")
	miCorreo.set("")
	miTel.set("")
	miPass.set("")

def crear():
	miConexion=sqlite3.connect("Usuarios")
	miCursor=miConexion.cursor()
	#CONSULTAS PARAMETRIZADAS EVITA INYECCIONES SQL
	datos=miNombre.get(),miTipoUsuario.get(),miCorreo.get(),miTel.get(),miPass.get()

	miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,?,?,?,?,?)",(datos))

	"""miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,'"+ miNombre.get() + 
		"','" + miPass.get() +
		"','" + miApellido.get() + 
		"','" + miDireccion.get() +
		"','" + textoComentario.get("1.0", END) + "')")"""

	miConexion.commit()
	messagebox.showinfo("BBDD", "Registro insertado con exito")

def leer():
	miConexion=sqlite3.connect("Usuarios")
	miCursor=miConexion.cursor()
	miCursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID=" + miID.get())
	elUsuario=miCursor.fetchall()
	for usuario in elUsuario:
		miID.set(usuario[0])
		miNombre.set(usuario[1])
		miTipoUsuario.set(usuario[2])
		miCorreo.set(usuario[3])
		miTel.set(usuario[4])
		miPass.set(usuario[5])
	miConexion.commit()

def actualizar():
	miConexion=sqlite3.connect("Usuarios")
	miCursor=miConexion.cursor()
	miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO='" + miNombre.get() +
		"', TIPO_USUARIO='" + miTipoUsuario.get() +
		"', CORREO_ELECTRONICO='" + miCorreo.get() +
		"', TELEFONO='" + miTel.get() +
		"', PASSWORD='" + miPass.get() + 
		"' WHERE ID=" + miID.get())


	miConexion.commit()
	messagebox.showinfo("BBDD", "Registro actualizado con exito")

def eliminar():
	miConexion=sqlite3.connect("Usuarios")
	miCursor=miConexion.cursor()
	miCursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID=" + miID.get())
	miConexion.commit()
	messagebox.showinfo("BBDD","Registro borrado con exito")


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
miID=StringVar()
miNombre=StringVar()
miTipoUsuario=StringVar()
miCorreo=StringVar()
miTel=StringVar()
miPass=StringVar()

CuadroIdUsuario=Entry(CuadroUsuario, textvariable=miID)
CuadroIdUsuario.grid(row=1, column=1, padx=10, pady=10)

CuadroNombreUsuario=Entry(CuadroUsuario,textvariable=miNombre)
CuadroNombreUsuario.grid(row=2, column=1, padx=10, pady=10)

CuadroTipoUsuario=Entry(CuadroUsuario,textvariable=miTipoUsuario)
CuadroTipoUsuario.grid(row=3, column=1, padx=10, pady=10)

CuadroCorreoUsuario=Entry(CuadroUsuario,textvariable=miCorreo)
CuadroCorreoUsuario.grid(row=4, column=1, padx=10, pady=10)

CuadroCelUsuario=Entry(CuadroUsuario,textvariable=miTel)
CuadroCelUsuario.grid(row=5, column=1, padx=10, pady=10)

CuadroPassUsuario=Entry(CuadroUsuario,textvariable=miPass)
CuadroPassUsuario.grid(row=6, column=1, padx=10, pady=10)
CuadroPassUsuario.config(show="*")


#-----------------------------BARRA DE MENU----------------------------------
bbddMenu=Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar",command=conexionBBDD)
bbddMenu.add_command(label="Salir",command=salirAplicacion)

borrarMenu=Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar campos",command=limpiarCampos)

crudMenu=Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Crear",command=crear)
crudMenu.add_command(label="Leer", command=leer)
crudMenu.add_command(label="Actualizar",command=actualizar)
crudMenu.add_command(label="Borrar",command=eliminar)

ayudaMenu=Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia", command=Licencia)
ayudaMenu.add_command(label="Acerca de...", command=acercaDe)

barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

raiz.mainloop()