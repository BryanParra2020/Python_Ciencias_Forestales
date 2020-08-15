"""El siguiente algoritmo calcula la correccion de pendiente denotada por la primera ecuacion

Created by: Bryan Daniel Parra Prieto 

Forest Engineering; Industrial University of Santander 

Date: Monday 20-08-2018 

Hour: 15:51 """ 

"""Es necesario llamar la libreria math que me permite realizar calculos, como los angulos por naturaleza se denotan en radianes, el sobreescribir
math.radians (x), entre paraentesis se toma el valor de cualquier variable de un angulo en grados y Python no calculara en radianes sino en grados"""
#INICIO 

#Creacion de Una Ventana para registro de Datos 
from tkinter import *
from tkinter import ttk #Paracreacion de Combobox 
from tkinter import messagebox 

ventana=Tk()
ventana.geometry("500x450+400+70")
ventana.title("")
ventana.configure(bg = "Medium Spring Green")

#Definiendo a la funcion encargada de "Calcular" 

def calcula (): 
 if ((var.get()) == "1.Calculo de Distancia Inclinada") : #Generalmente se emplea esta ecuacion, ya que calcula la distancia corregida.
  import math  #Libreria Matematica (en este caso para funciones trigonometricas, "Coseno empleado")
  dh = entradaDisH.get()
  ang = entradaAng.get()
  ang2 = math.radians(ang)
  di = (dh)/((math.cos(ang2))) # Relacion entre la dh y el cos del angulo (mostrado por el clinometro)
  print ("La distancia corregida es: " + str (round(di,2)), "metros")
  messagebox.showinfo (message = "La distancia corregida es: " + str (round(di,2)) + " m")
		
 elif ((var.get()) == "2.Calculo de Distancia Horizontal") : 
  import math
  di = entradaDisI.get()
  ang = entradaAng.get()
  ang2 = math.radians(ang)
  dh = (di)*((math.cos(ang2))) # Multiplicacion entre la di y el cos del angulo (mostrado por el clinometro)
  print ("La distancia horizontal es: " + str (round(dh,2)), "metros")
  messagebox.showinfo (message = "La distancia horizontal es: " + str (round(dh,2)) + " m")

#Definiendo a la funcion encargada de "Imprimir" 
def delete ():
	lblDelete = Label (ventana, text = "Delete", relief="raised",borderwidth=5)

#Creacion de labels o etiquetas
lblCp = Label (text = "Correccion de Pendiente", bg = "Green Yellow",font = ("Times New Roman",16)).place(x=170, y=4)

lblEc = Label (text = "Ecuaciones: ", bg = "Medium Spring Green",font = ("Times New Roman",16)).place(x=4, y=45)

lblDisH = Label (text = "Distancia Horizontal (m): ", bg = "Medium Spring Green", font = ("Times New Roman",16)).place(x=4,y=85)

lblAng = Label (text = "Angulo de Inclinacion (°): " , bg = "Medium Spring Green", fg = "blue",font = ("Times New Roman",16)).place(x=4,y=125)

lblDisI = Label (text = "Distancia Inclinada (m): " , bg = "Medium Spring Green", fg = "brown",font = ("Times New Roman",16)).place(x=4,y=165)

#Creando el Combobox para Distancias (Para este modulo es necesario llamar la libreria "ttk")
var = StringVar()
ComD = ttk.Combobox (ventana, values = ("1.Calculo de Distancia Inclinada" , "2.Calculo de Distancia Horizontal"),textvariable = var,font = ("Comic Sans MS",12),width = 25).place(x=117, y=45) #Esto para valores textuales

#Creando un campo numerico para Distancia Horizontal
entradaDisH = DoubleVar()
DisH = Entry (ventana, textvariable = entradaDisH, font = ("Comic Sans MS",12), width = 15).place(x=235, y=86)#width elonga la casilla de escritura

#Creando un campo numerico para Distancia Inclinada
entradaDisI = DoubleVar()
DisI = Entry (ventana, textvariable = entradaDisI, font = ("Comic Sans MS",12), width = 15).place(x=235, y=166)

#Creando un campo numerico para Angulo
entradaAng = DoubleVar()
Ang = Entry (ventana, textvariable = entradaAng, font = ("Comic Sans MS",13), width = 15).place(x=235, y=126)

#Creacion de Botones 
btnCalcular = Button (ventana, text="Calcular",command = calcula, bg = "white",fg = "black", font = ("Times New Roman", 16), relief="groove", borderwidth=7, width = 6).place(x=378, y=233)

btnSalir = Button (ventana, text="Salir",command = ventana.quit, fg = "red", font = ("Times New Roman", 16), relief="ridge", borderwidth="1.5p", width = 5).place(x=429, y=409)

btnDelete = Button (ventana, text = "Delete", command = delete, fg = "blue", font = ("Times New Roman", 16), relief="raised",borderwidth=3, width = 8).place(x=1, y=409)
 
 #
ventana.mainloop()
