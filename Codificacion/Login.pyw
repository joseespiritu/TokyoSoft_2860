from tkinter import *
from tkinter import messagebox #Ventanas emergentes
import sqlite3

raiz=Tk()
raiz.title("Inicio Sesion")
raiz.resizable(0,0)
raiz.geometry("250x150")

#CUADRO DE VISUALIZACION
CuadroLogin=Frame(raiz)
CuadroLogin.pack()


#FUNCION VALIDACION DE DATOS
def leer():
	if (miUsuario.get()=="ADMIN" and miPassword.get()=="ADMIN"):
		from FrameAdmin import FrameAdmin
	else:
		messagebox.showwarning("!Atencion!","Usuario No Registrado")
	"""miConexion=sqlite3.connect("Usuarios")
	miCursor=miConexion.cursor()
	miCursor.execute("SELECT * FROM DATOSUSUARIOS WHERE NOMBRE_USUARIO=" + miUsuario.get() +"PASSWORD="+miPassword.get())
	from FrameAdmin import FrameAdmin
	miConexion.commit()"""
#BOTON
botonAcceso=Button(raiz, text="Acceder",command=leer)
botonAcceso.pack()

#ETIQUETAS CUADROS
usuarioLabel=Label(CuadroLogin, text="Usuario:")
usuarioLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

passwordLabel=Label(CuadroLogin, text="Contraseña:")
passwordLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

#CAMPO DE TEXTO (FORMULARIO)
miUsuario=StringVar()
miPassword=StringVar()

CuadroUsuario=Entry(CuadroLogin,textvariable=miUsuario)
CuadroUsuario.grid(row=1, column=1, padx=10, pady=10)

CuadroPasword=Entry(CuadroLogin,textvariable=miPassword)
CuadroPasword.grid(row=2, column=1, padx=10, pady=10)
CuadroPasword.config(show="*")

raiz.mainloop()