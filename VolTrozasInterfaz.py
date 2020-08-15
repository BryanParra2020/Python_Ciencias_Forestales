"""El siguiente algoritmo estima el volumen del arbol en pie y por trozas a traves de la ecuaciones mencionadas por la (FAO,1980)

Created by: Bryan Daniel Parra Prieto 

Forest Engineering; Industrial University of Santander 

Date: Friday 27-04-2018 

Hour: 06:52 """  

#INICIO 

#Creacion de Una Ventana para registro de Datos 
from tkinter import *
from tkinter import ttk #Paracreacion de Combobox 
from tkinter import messagebox 
import math #Libreria matematica

ventana = Tk() 
ventana.geometry("800x450+350+70")
ventana.title("Estimacion Volumetrica")
colorfondo = "#006" #0 en Rojo, 0 en Verde, 6 en Azul
colorletra = "#FFF" #Toda la letra es Blanca
ventana.configure (bg = colorfondo) 

#Definiendo a la funcion encargada de "Calcular" 
def calcula (): 
 if (var.get() == "Smallian"):  
	 d1 = entradaDm.get()  
	 d1m = (d1/100) 
	 d2 = entradaDmr.get()
	 d2m = (d2/100)  
	 pi = math.pi 
	 l = entradaA.get()
	 vt = pi/4*(((d1m)**2+(d2m)**2)/2)*l 
	 print("\nEl volumen de la troza es: "+str(round (vt,4)), "metros cubicos")
	 lblVt = Label (text = ("El volumen de la troza es: " + str (round (vt,4)), "metros cubicos"), bg = colorfondo, fg = "silver", font = ("Times New Roman",16)).place(x=2,y=310)
	 #messagebox.askquestion ("?", message = "Que deseas hacer?") #Mensaje de la ventana en forma de pregunta
 
 elif (var.get() == "Newton"):  
	 d1 = entradaDm.get() 
	 d1m = (d1/100) 
	 d2 = entradaDmr.get() 
	 d2m = (d2/100)  
	 dm = (d1m+d2m)/2
	 pi = math.pi 
	 l = entradaA.get() 
	 vt = (pi/24)*(((d1m)**(2)+(4*(dm)**(2))+(d2m)**(2)))*l 
	 print("\nEl volumen de la troza es: "+str(round (vt,4)), "metros cubicos") 
	 lblVt = Label (text = ("El volumen de la troza es: " + str (round (vt,4)), "metros cubicos"),  bg = colorfondo, fg = "silver", font = ("Times New Roman",16)).place(x=2,y=310)
	 
 elif (var.get() == "Huber"): 
	 d1 = entradaDm.get() 
	 d1m = (d1/100) 
	 d2 = entradaDmr.get() 
	 d2m = (d2/100) 
	 dm = ((d1m+d2m)/2) 
	 pi = math.pi 
	 l = entradaA.get()
	 vt = (pi/4)*(((dm)**(2))*l) 
	 print("\nEl volumen de la troza es: "+str(round (vt,4)), "metros cubicos")  
	 lblVt = Label (text = ("El volumen de la troza es: " + str (round (vt,4)), "metros cubicos"),  bg = colorfondo, fg = "silver", font = ("Times New Roman",16)).place(x=2,y=310)

 elif (var.get() == "Huber Modificado"): 
	 d1 = entradaDm.get()  
	 d1m = (d1/100) 
	 d2 = entradaDmr.get() 
	 d2m = (d2/100) 
	 pi = math.pi
	 l = entradaA.get()
	 vt = (pi/4)*(((d1m+d2m)/2)**(2))*l 
	 print("\nEl volumen de la troza es: "+str(round (vt,4)), "metros cubicos")
	 lblVt = Label (text = ("El volumen de la troza es: " + str (round (vt,4)), "metros cubicos"),  bg = colorfondo, fg = "silver", font = ("Times New Roman",16)).place(x=2,y=310) 
	 
 elif (var.get() == "Cono Truncado"): 
	 d1 = entradaDm.get()
	 d1m = (d1/100) 
	 d2 = entradaDmr.get()  
	 d2m = (d2/100) 
	 pi = math.pi 
	 l = entradaA.get() 
	 vt = (pi/12)*((d1m)**(2)+(d2m)**(2)+(d1m*d2m))*l  
	 print("\nEl volumen de la troza es: "+str(round (vt,4)), "metros cubicos") 
	 lblVt = Label (text = ("El volumen de la troza es: " + str (round (vt,4)), "metros cubicos"),  bg = colorfondo, fg = "silver", font = ("Times New Roman",16)).place(x=2,y=310)  
	 
 else: 
	 dap = entradaDap.get()
	 dap1 = (dap/100)
	 dapm = (dap1)**(2)
	 h = entradaAa.get()
	 Ff = entradaFF.get()
	 pi = math.pi 
	 va = (pi/4)*((dapm)*(h)*(Ff))
	 print ("\nEl volumen del arbol en pie estimado es: "+str(round (va,4)), "metros cubicos")
	 lblVa = Label (text = ("El volumen del arbol en pie estimado es: " + str (round (va,4)), "metros cubicos"),  bg = colorfondo, fg = "silver", font = ("Times New Roman",16)).place(x=2,y=340)  
	
#Importamos la imagen 
ImagenL = PhotoImage (file = "SedeMa.png")#PhotoImage me permite cargar imagenes en solo tres formatos .gif, .pgm, .ppm, .png; despues del file = se coloca el nombre del archivo, este debe estar guardado dentro de la misma carpeta en donde esta el algoritmo creado seguido del (formato en el que esta por ejemplo, Forestal.png)

lblImagen = Label (ventana, image = ImagenL). place(x=489, y=170) #Posicion esquinera 

#Creacion de labels o etiquetas
lblVtroz = Label (text = "VOLUMEN TROZAS", bg = colorfondo, fg = colorletra, font = ("Times New Roman",16)).place(x=110, y=4)

lblVAa = Label (text = "VOLUMEN ARBOL EN PIE", bg = colorfondo, fg = colorletra, font = ("Times New Roman",16)).place(x=490, y=4)

lblF = Label (text = "Formulas: ", bg = colorfondo, fg = "silver", font = ("Times New Roman",16)).place(x=4,y=45)

lblDm = Label (text = "Diametro mayor (cm): " , bg = colorfondo, fg = "silver",font = ("Times New Roman",16)).place(x=4,y=85)

lblDmr = Label (text = "Diametro menor (cm): " , bg = colorfondo, fg = "silver", font = ("Times New Roman",16)).place(x=4,y=125)

lblLT = Label (text = "Longitud de la troza (m): " , bg = colorfondo, fg = "silver", font = ("Times New Roman",16)).place(x=4,y=165)

#Etiquetas para arbol en pie
lblDap = Label (ventana, text = "Dap (cm): ", bg = colorfondo, fg = "silver", font = ("Times New Roman",16)).place(x=440,y=45)
	 
lblFF = Label (ventana, text = "Factor Morfico: ", bg = colorfondo, fg = "silver", font = ("Times New Roman",16)).place(x=440, y=85)
	 
lblAa = Label (ventana, text = "Altura del arbol (m): ", bg = colorfondo, fg = "silver", font = ("Times New Roman",16)).place(x=440, y=125)

#Creando el Combobox para formulas (Para este modulo es necesario llamar la libreria "ttk")
var = StringVar()
ComF = ttk.Combobox (ventana,  values = ("", "Smallian", "Newton", "Huber", "Huber Modificado", "Cono Truncado"), textvariable = var,font = ("Comic Sans MS",12),width = 22).place(x=147, y=45) #Esto para valores textuales, ((""), funciona como cero valores)


#Creando un campo numerico para Diametro mayor
entradaDm = DoubleVar()
txtDm = Entry (ventana, textvariable = entradaDm, font = ("Comic Sans MS",12), width = 14).place(x=245, y=86)#width elonga la casilla de escritura

#Creando un campo numerico para Diametro menor
entradaDmr = DoubleVar()
txtDmr = Entry (ventana, textvariable = entradaDmr, font = ("Comic Sans MS",12), width = 14).place(x=245, y=126)

#Creando un campo numerico para Altura
entradaA = DoubleVar()
txtA = Entry (ventana, textvariable = entradaA,font = ("Comic Sans MS",13), width = 14).place(x=245, y=166)

#Creando campo numerico para Dap
entradaDap = DoubleVar()
txtDap = Entry (ventana, textvariable = entradaDap,font = ("Comic Sans MS",12), width = 14).place(x=645, y=45)

#Creando campo numerico para Factor morfico
entradaFF = DoubleVar()
txtFF = Entry (ventana, textvariable = entradaFF,font = ("Comic Sans MS",12), width = 14).place(x=645, y=85)
entradaFF.set ("0.6")

#Creando campo numerico para Altura del arbol
entradaAa = DoubleVar()
txtAa = Entry (ventana, textvariable = entradaAa,font = ("Comic Sans MS",12), width = 14).place(x=645, y=125)

#Creacion de Botones 
btnCalcular = Button (ventana, text="Calcular",command = calcula, bg = "#159",fg = colorletra, font = ("Times New Roman", 16), width = 6).place(x=360, y=243)

btnSalir = Button (ventana, text="Salir",command = ventana.quit, bg = "white", fg = "red", font = ("Times New Roman", 16), width = 5).place(x=730, y=410)


#
ventana.mainloop()

