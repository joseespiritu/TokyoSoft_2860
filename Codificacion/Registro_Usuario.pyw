from tkinter import *
raiz=Tk()
raiz.title("Registro de Usuario")
raiz.resizable(0,0)
raiz.geometry("350x350")

#CUADRO DE VISUALIZACION
CuadroUsuario=Frame(raiz)
CuadroUsuario.pack(fill="both",expand="True")


#ETIQUETAS DE TEXTO

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

#CAJAS DE TEXTO
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

#BOTON
botonAcceso=Button(CuadroUsuario, text="Aceptar")
botonAcceso.grid(row=7, column=1, padx=10, pady=10)

raiz.mainloop()