"""El siguiente algoritmo calcula el numero de arboles por unidad de area (densidad de siembra)

Created by: Bryan Daniel Parra Prieto  

Forest Engineering; Industrial University of Santander 

Date: Saturday 10-03-2018 

Hour: 15:46 """ 

#INICIO 

#Creacion de Una Ventana para registro de Datos 
from tkinter import *
from tkinter import ttk #Paracreacion de Combobox 
from tkinter import messagebox 

ventana=Tk() 
ventana.geometry("500x450+400+70")
ventana.title("Industrial University of Santander - Forest Engineering")

#Definiendo a la funcion encargada de "Calcular" 
def calcula ():
 if (var.get() == "Triangulo"): 
	 at = (entradaNha.get()*10000)
	 a = entradaDisSA.get()
	 b = entradaDisSS.get() 
	 na = int((at/(a*b))*1.15)
	 #Crear label para respuesta
	 lblArb = Label (text = ("El Numero Total de Individuos es de: "+ str (na), "arboles"), fg = "black",  bg = "#FFF",font = ("Times New Roman",16)).place(x=4,y=305)
	 #Crear Messagebox 
	 messagebox.showinfo ("Total de Individuos", message = "Son: "+ str (na) + " arboles")
	 
 elif (var.get() == "Cuadrado"): 
	 at = (entradaNha.get()*10000)
	 a = entradaDisSA.get()
	 b = entradaDisSS.get() 
	 na = int(at/(a*b))
	 #Crear label para respuesta
	 lblArb = Label (text = ("El Numero Total de Individuos es de: "+ str (na), "arboles"), fg = "black",  bg = "#FFF",font = ("Times New Roman",16)).place(x=4,y=305)
	 #Crear Messagebox 
	 messagebox.showinfo ("Total de Individuos", message = "Son: "+ str (na) + " arboles")
     
 elif (var.get() == "Rectangulo"): 
	 at = (entradaNha.get()*10000)
	 a = entradaDisSA.get()
	 b = entradaDisSS.get() 
	 na = int(at/(a*b))
	 #Crear label para respuesta
	 lblArb = Label (text = ("El Numero Total de Individuos es de: "+ str (na), "arboles"), fg = "black", bg = "#FFF",font = ("Times New Roman",16)).place(x=4,y=305)
	 #Crear Messagebox 
	 messagebox.showinfo ("Total de Individuos", message = "Son: "+ str (na) + " arboles")

 #Definiendo a la funcion encargada de "Salir" 
def salir ():
	lblSalir = Label (ventana, text = "Salir")
	
#Definiendo a la funcion encargada de "Imprimir" 
def imprime ():
	lblImprimir = Label (ventana, text = "imprimir")

#Importamos la imagen 
ImagenL = PhotoImage (file = "MonterreyForestal.png ")

lblImagen = Label (ventana, image = ImagenL). place(x=0, y=-50) 

#Creacion de labels o etiquetas
lblDensiS = Label (text = "Densidad de Siembra",bg = "yellow",font = ("Times New Roman",16)).place(x=170, y=4)

lblSS = Label (text = "Sistema de Siembra: ",font = ("Times New Roman",16)).place(x=4,y=45)

lblNha = Label (text = "Numero de Hectareas (ha): " ,fg = "brown",font = ("Times New Roman",16)).place(x=4,y=85)

lblDisSA = Label (text = "Distancia de Siembra entre Arbol (m): " ,fg = "blue",font = ("Times New Roman",16)).place(x=4,y=125)

lblDisSS = Label (text = "Distancia de Siembra entre Surcos (m): " ,fg = "green",font = ("Times New Roman",16)).place(x=4,y=165)

#Creando el Combobox para sistemas de siembra (Para este modulo es necesario llamar la libreria "ttk")
var = StringVar()
ComSS = ttk.Combobox (ventana, values = ("Triangulo", "Cuadrado", "Rectangulo"), textvariable = var,font = ("Comic Sans MS",12),width = 18).place(x=187, y=45) #Esto para valores textuales
var.set ("Triangulo")

#Creando un campo numerico para Numero de Hectareas a Sembrar 
entradaNha = DoubleVar()
txtNha = Entry (ventana, textvariable = entradaNha,font = ("Comic Sans MS",12), width = 14).place(x=245, y=86)#width elonga la casilla de escritura
entradaNha.set ("1")

#Creando un campo numerico para Distancia de Siembra entre Arbol
entradaDisSA = DoubleVar()
txtDisSA = Entry (ventana, textvariable = entradaDisSA, font = ("Comic Sans MS",12), width = 5).place(x=335, y=126)
entradaDisSA.set ("3")

#Creando un campo numerico para Distancia de Siembra entre Surcos 
entradaDisSS = DoubleVar()
txtDisSS = Entry (ventana, textvariable = entradaDisSS,font = ("Comic Sans MS",13), width = 5).place(x=336, y=166)
entradaDisSS.set ("3")

#Creacion de Botones 
btnCalcular = Button (ventana, text="Calcular",command = calcula, bg = "white",fg = "black", font = ("Times New Roman", 16), width = 6).place(x=378, y=233)

btnSalir = Button (ventana, text="Salir",command = ventana.quit, fg = "red", font = ("Times New Roman", 16), width = 5).place(x=429, y=409)

btnImprimir = Button (ventana, text = "Imprimir", command = imprime, fg = "blue", font = ("Times New Roman", 16), width = 8).place(x=1, y=409)

#
ventana.mainloop()
