from tkinter import *
raiz=Tk()
raiz.title("Inicio Sesion")
raiz.resizable(0,0)
raiz.geometry("250x150")

#CUADRO DE VISUALIZACION
CuadroLogin=Frame(raiz)
CuadroLogin.pack()

#BOTON
botonAcceso=Button(raiz, text="Acceder")
botonAcceso.pack()

#ETIQUETAS CUADROS
usuarioLabel=Label(CuadroLogin, text="Usuario:")
usuarioLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

passwordLabel=Label(CuadroLogin, text="Contraseña:")
passwordLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

#CAMPO DE TEXTO (FORMULARIO)
CuadroUsuario=Entry(CuadroLogin)
CuadroUsuario.grid(row=1, column=1, padx=10, pady=10)

CuadroPasword=Entry(CuadroLogin)
CuadroPasword.grid(row=2, column=1, padx=10, pady=10)
CuadroPasword.config(show="*")


raiz.mainloop()