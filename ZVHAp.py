"""El siguiente algoritmo se conecta a una API y en base a esa informacion realiza la clasificacion de las Zonas de Vida Ecologicas de acuerdo a la metodologia propuesta por Holdridge(1967) & Paramos segun Cuatercasas

Created by: Bryan Daniel Parra Prieto 

Forest Engineering; Industrial University of Santander 

Date: Friday 24-08-2018 

Hour: 20:46 """ 

#Inicio 

#instalar en el cmd el requests, a traves de (pip install requests), esto permite obtener los permisos del servidor climatico para posteriormente emplear dicha informacion en la interfaz 

#Creando la interfaz a traves del tkinter
from tkinter import *  
import requests #Importando los permisos del servidor
from tkinter import ttk #Paracreacion de Combobox 
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

#Creacion de ventana
ventana =Tk() 
ventana.geometry("535x600+380+70")
ventana.title("Zonas de Vida, Holdridge (1967)")
ventana.config (bg = "#062") #con este parametro puedo darle un color de fondo a la ventana a traves de bg (blackground) = color en ingles o "#0 en rojo, 6 en verde y 0 en azul" (RGB)

#Importando la API o copiando la Key del openweather              
#63630a4fc4631f8b377f2ac9c75bce29       

#Ir al current weather y copiar la llamada al API 
#api.openweathermap.org/data/2.5/weather?q={city name}              
                
#Estas funciones generalmente se programan a lo ultimo, conforme se van creando los botones

#Generando la funcion para obtener los permisos del servidor usado
def clima (ciudad):
    try:
     API_key = "63630a4fc4631f8b377f2ac9c75bce29"
     URL = "https://api.openweathermap.org/data/2.5/weather"
     parametros = {"APPID": API_key, "q": ciudad, "units": "metric", "lang": "es"} #Unidades del sistema metrico, para que la temperatura sea en grados celsius, parametro lang referente al lenguajes en este caso (es) para que la informacion aparezca en español
     respuesta = requests.get(URL, params = parametros)
     clima = respuesta.json()
     print ("\n1. Algunas variables climatologicas")
     print (respuesta.json())# json es el formato de salida de los datos de la API, de esta forma Python los interpreta como un diccionario para poder observar dicha informacion      
  
     print ("\n2. Descripcion resumida de variables")
     print ("Pais: " + clima ["sys"]["country"])
     print ("Nombre del lugar: " + clima ["name"])
     print ("Coordenadas: " + str (clima ["coord"]))
     print ("Tiempo atmosferico: " + clima ["weather"][0]["description"])#Es necesario ya que dentro de un diccionario se tiene una lista
     print ("Temperatura: " + str (clima ["main"]["temp"]), "°C")#Es necesario concatenar la variable cuantitativa a un string
     print ("Humedad relativa: "+ str (clima ["main"]["humidity"]), "%")
     print ("Presion atmosferica: "+ str (clima ["main"]["pressure"]), "hPa")
    except: 
     messagebox.showerror ("Error de Sintaxis", message = "Nombre invalido o ausente")
    
#Definiendo a la funcion encargada de "Salir" 
def salir ():
	lblSalir = Label (ventana, text = "Salir")
	
#Definiendo a la funcion encargada de "Calcular" 
def calcular (): 
 alt = entradaA.get()
 prec = entradaP.get()
 tem = entradaT.get() 
 
#CONDICIONANTES
 if alt<1000: 
	 if prec>=500 and prec<=1000: 
		 if tem>24: 
			 print ("\nLa Zona de Vida es: Bosque Muy Seco Tropical, bms-T")#Devuelve el resultado a la consola del cmd
			 lblZVH = Label (text = "Bosque Muy Seco Tropical, bms-T", bg = "#062", font = ("Times New Roman",12)).place (x=140, y=450) #Muestra una etiqueta con el resultado calculado
			 messagebox.showinfo ("Zona de Vida", message = "La Zona de Vida es:  bms-T")#Muestra un mensaje con el resultado calculado
			 		 
 if alt<1000: 
	 if prec>=1000 and prec<=2000: 
		 if tem>24: 
			 print ("\nLa Zona de Vida es: Bosque Seco Tropical, bs-T")  
			 lblZVH = Label (text = "Bosque Seco Tropical, bs-T", bg = "#062", font = ("Times New Roman",12)).place (x=140, y=450)
			 messagebox.showinfo ("Zona de Vida", message = "La Zona de Vida es:  bs-T")
			 
 if alt<1000: 
	 if prec>=2000 and prec<=4000: 
		 if tem>24: 
			 print("\nLa Zona de Vida es: Bosque Humedo Tropical, bh-T") 
			 lblZVH = Label (text = "Bosque Humedo Tropical, bh-T", bg = "#062", font = ("Times New Roman",12)).place (x=140, y=450)
			 messagebox.showinfo ("Zona de Vida", message = "La Zona de Vida es:  bh-T")
			 
 if alt<1000: 
	 if prec>=4000 and prec<=8000: 
		 if tem>24: 
			 print("\nLa Zona de Vida es: Bosque Muy Humedo Tropical, bmh-T") 
			 lblZVH = Label (text = "Bosque Muy Humedo Tropical, bmh-T", bg = "#062", font = ("Times New Roman",12)).place (x=140, y=450)
			 messagebox.showinfo ("Zona de Vida", message = "La Zona de Vida es:  bmh-T")
			 			 
 if alt<1000:
	 if prec>8000: 
		 if tem>24: 
			 print("\nLa Zona de Vida es: Bosque Pluvial Tropical, bp-T")  
			 lblZVH = Label (text = "Bosque Pluvial Tropical, bp-T", bg = "#062", font = ("Times New Roman",12)).place (x=140, y=450)
			 messagebox.showinfo ("Zona de Vida", message = "La Zona de Vida es:  bp-T")
			 
 if alt<1000: 
	 if prec>=125 and prec<250: 
		 if tem>=18 and tem<=24: 
			 print("\nLa Zona de Vida es: Matorral Desertico Subtropical, md-ST")
			 lblZVH = Label (text = "Matorral Desertico Subtropical, md-ST", bg = "#062", font = ("Times New Roman",12)).place (x=140, y=450)
			 messagebox.showinfo ("Zona de Vida", message = "La Zona de Vida es:  md-ST")
			 
 if alt<1000: 
	 if prec>=250 and prec<=500: 
		 if tem>=18 and tem<=24: 
			 print("\nLa Zona de Vida es: Monte Espinoso Subtropical, me-ST")
			 lblZVH = Label (text = "Monte Espinoso Subtropical, me-ST", bg = "#062", font = ("Times New Roman",12)).place (x=140, y=450)
			 messagebox.showinfo ("Zona de Vida", message = "La Zona de Vida es:  me-ST")
			 
 if alt>=1000 and alt<=2000: 
	 if prec>=250 and prec<=500: 
		 if tem>=18 and tem<=24: 
			 print("\nLa Zona de Vida es: Monte Espinoso Premontano, me-PM") 
			 lblZVH = Label (text = "Monte Espinoso Premontano, me-PM", bg = "#062", font = ("Times New Roman",12)).place (x=140, y=450)
			 messagebox.showinfo ("Zona de Vida", message = "La Zona de Vida es:  me-PM")
			 
 if alt>=1000 and alt<=2000: 
	 if prec>=500 and prec<=1000: 
		 if tem>=18 and tem<=24: 
			 print("\nLa Zona de Vida es: Bosque Seco Premontano, bs-PM")  
			 lblZVH = Label (text = "Bosque Seco Premontano, bs-PM", bg = "#062", font = ("Times New Roman",12)).place (x=140, y=450)
			 messagebox.showinfo ("Zona de Vida", message = "La Zona de Vida es:  bs-PM")
			 
 if alt>=1000 and alt<=2000: 
	 if prec>=1000 and prec<=2000: 
		 if tem>=18 and tem<=24: 
			 print("\nLa Zona de Vida es: Bosque Humedo Premontano, bh-PM")  
			 lblZVH = Label (text = "Bosque Humedo Premontano, bh-PM", bg = "#062", font = ("Times New Roman",12)).place (x=140, y=450)
			 messagebox.showinfo ("Zona de Vida", message = "La Zona de Vida es:  bh-PM")
			 
 if alt>=1000 and alt<=2000: 
	 if prec>=2000 and prec<=4000: 
		 if tem>=18 and tem<=24: 
			 print("\nLa Zona de Vida es: Bosque Muy Humedo Premontano, bmh-PM")  
			 lblZVH = Label (text = "Bosque Muy Humedo Premontano, bmh-PM", bg = "#062", font = ("Times New Roman",12)).place (x=140, y=450)
			 messagebox.showinfo ("Zona de Vida", message = "La Zona de Vida es:  bmh-PM")
			 
 if alt>=1000 and alt<=2000: 
	 if prec>4000: 
		 if tem>=18 and tem<=24: 
			 print("\nLa Zona de Vida es: Bosque Pluvial Premontano, bp-PM") 
			 lblZVH = Label (text = "Bosque Pluvial Premontano, bp-PM", bg = "#062", font = ("Times New Roman",12)).place (x=140, y=450)
			 messagebox.showinfo ("Zona de Vida", message = "La Zona de Vida es:  bp-PM")
		 
 if alt>=2000 and alt<=2600: 
    if prec>=500 and prec<=1000: 
	     if tem>=12 and tem<=18: 
		     print("\nLa Zona de Vida es: Bosque Seco Montano Bajo, bs-MB")  
		     lblZVH = Label (text = "Bosque Seco Montano Bajo, bs-MB", bg = "#062", font = ("Times New Roman",12)).place (x=140, y=450)
		     messagebox.showinfo ("Zona de Vida", message = "La Zona de Vida es:  bs-MB")
		     
 if alt>=2000 and alt<=2600: 
	 if prec>=1000 and prec<=2000: 
		 if tem>=12 and tem<=18:
			 print("\nLa Zona de Vida es: Bosque Humedo Montano Bajo, bh-MB") 
			 lblZVH = Label (text = "Bosque Humedo Montano Bajo, bh-MB", bg = "#062", font = ("Times New Roman",12)).place (x=140, y=450)
			 messagebox.showinfo ("Zona de Vida", message = "La Zona de Vida es:  bh-MB")
			 
 if alt>=2000 and alt<=2600: 
	 if prec>=2000 and prec<=4000:
		 if tem>=12 and tem<=18: 
			 print("\nLa Zona de Vida es: Bosque Muy Humedo Montano Bajo, bmh-MB") 
			 lblZVH = Label (text = "Bosque Muy Humedo Montano Bajo, bmh-MB", bg = "#062", font = ("Times New Roman",12)).place (x=140, y=450)
			 messagebox.showinfo ("Zona de Vida", message = "La Zona de Vida es:  bmh-MB")
			 
 if alt>=2000 and alt<=2600:
	 if prec>4000: 
		 if tem>=12 and tem<=18: 
			 print("\nLa Zona de Vida es: Bosque Pluvial Montano Bajo, bp-MB")
			 lblZVH = Label (text = "Bosque Pluvial Montano Bajo, bp-MB", bg = "#062", font = ("Times New Roman",12)).place (x=140, y=450)
			 messagebox.showinfo ("Zona de Vida", message = "La Zona de Vida es:  bp-MB") 
			 
 if alt>=2600 and alt<=3200: 
	 if prec>=500 and prec<=1000: 
		 if tem>=6 and tem<=12: 
			 print("\nLa Zona de Vida es: Bosque Humedo Montano, bh-M") 
			 lblZVH = Label (text = "Bosque Humedo Montano, bh-M", bg = "#062", font = ("Times New Roman",12)).place (x=140, y=450)
			 messagebox.showinfo ("Zona de Vida", message = "La Zona de Vida es:  bh-M") 
			 
 if alt>=2600 and alt<=3200: 
	 if prec>=1000 and prec<=2000:
		 if tem>=6 and tem<=12:
			 print("\nLa Zona de Vida es: Bosque Muy Humedo Montano, bmh-M")
			 lblZVH = Label (text = "Bosque Muy Humedo Montano, bmh-M", bg = "#062", font = ("Times New Roman",12)).place (x=140, y=450)
			 messagebox.showinfo ("Zona de Vida", message = "La Zona de Vida es:  bmh-M") 
			 
 if alt>=2600 and alt<=3200:
	 if prec>2000:
		 if tem>=6 and tem<=12: 
			 print("\nLa Zona de Vida es: Bosque Pluvial Montano, bp-M") 
			 lblZVH = Label (text = "Bosque Pluvial Montano, bp-M", bg = "#062", font = ("Times New Roman",12)).place (x=140, y=450)
			 messagebox.showinfo ("Zona de Vida", message = "La Zona de Vida es:  bp-M")  
			 
 if alt>=3000 and alt<=4400: 
	 if prec<=500: 
		 if tem>=3 and tem<=6: 
			 print("\nLa Zona de Vida es: Paramo Subalpino, P-SA")
			 lblZVH = Label (text = "Paramo Subalpino, P-SA", bg = "#062", font = ("Times New Roman",12)).place (x=140, y=450)
			 messagebox.showinfo ("Zona de Vida", message = "La Zona de Vida es:  P-SA") 
			 
 if alt>=3000 and alt<=4400: 
	 if prec>600:
		 if tem>=3 and tem<=6:
			 print("\nLa Zona de Vida es: Paramo Pluvial Subalpino, Pp-SA")
			 lblZVH = Label (text = "Paramo Pluvial Subalpino, Pp-SA", bg = "#062", font = ("Times New Roman",12)).place (x=140, y=450)
			 messagebox.showinfo ("Zona de Vida", message = "La Zona de Vida es:  Pp-SA")
			 
 if alt>=4200 and alt<=4400:
	 if prec>=500:
		 if tem<3:
			 print("\nLa Zona de Vida es: Tundra Pluvial Alpina, Tp-A") 
			 lblZVH = Label (text = "Tundra Pluvial Alpina, Tp-A", bg = "#062", font = ("Times New Roman",12)).place (x=140, y=450)
			 messagebox.showinfo ("Zona de Vida", message = "La Zona de Vida es:  Tp-A")
			 
 if alt>4400: 
	 if prec<=500:
		 if tem<3: 
			 print("\nLa Zona de Vida es: Nieves Perpetuas, NP") 
			 lblZVH = Label (text = "Nieves Perpetuas, NP", bg = "#062",font = ("Times New Roman",12)).place (x=140, y=450)
			 messagebox.showinfo ("Zona de Vida", message = "La Zona de Vida es:  NP")

#Definiendo a la funcion encargada de "Guardar en menu" 
def guardar (): 
 entradaA.set("")
 entradaP.set("")
 entradaT.set("")

#Definiendo a la funcion encargada de "Imprimir" 
def imprime (): 
	lblImprimir = Label (ventana, text = "Imprimir")
		
#Definiendo a la funcion encargada de agregar elementos a la lista 
def agregar ():
	#print("Si Agrega")
	lstdatos.insert (END,entrada.get())#END me permite agregar al final los campos de texto digitados		
		
#Importamos la imagen 
ImagenL = PhotoImage (file = "Forestal.png")#PhotoImage me permite cargar imagenes en solo tres formatos .gif, .pgm, .ppm, .png; despues del file = se coloca el nombre del archivo, este debe estar guardado dentro de la misma carpeta en donde esta el algoritmo creado seguido del (formato en el que esta por ejemplo, Forestal.png)

lblImagen = Label (ventana, image = ImagenL). place(x=0, y=0) #Posicion esquinera 

#Creacion de labels o etiquetas

#lblUsuario = Label (text = "Usuario: ",bg = "yellow",font = ("Times New Roman",12)).place(x=1, y=180)#font, hace referencia a la fuente, en este caso copiada y pegada de word, seguida del tama de la letra, en este caso de 14

#lblNom = Label (text = "Nombre: ",bg = "white",font = ("Times New Roman",12), width = 6).place(x=1, y=210)

lblLug = Label (text = "Lugar: ",bg = "silver",font = ("Times New Roman",12)).place(x=1,y=180)

lblAlt = Label (text = "Altura (m.s.n.m): " ,fg = "brown",font = ("Times New Roman",12)).place(x=1,y=310)

lblPrec = Label (text = "Precipitacion (mm): " ,fg = "blue",font = ("Times New Roman",12)).place(x=1,y=340)

lblTemp = Label (text = "Temperatura (°C): " ,fg = "black",font = ("Times New Roman",12)).place(x=1,y=370)

lblZV = Label (text = "La Zona de Vida es: " ,fg = "green", font = ("Times New Roman",12)).place(x=1,y=450)

lblzv = Label (text = "ZV: ", bg = "#062",fg = "white",font = ("Times New Roman",11)).place(x=310,y=154) 

#Creando un campo de texto para Usuario
#entradaU = StringVar()
#txtUsuario = Entry (ventana, textvariable = entradaU, font = ("Times New Roman",12),width = 28).place(x=70, y=181)
#entradaU.set("2135238")#.set sirve para asignar un texto predefinido, en este caso "2135238"

#Creando un campo de texto para Nombre 
#entradaN = StringVar()
#txtNombre = Entry (ventana, textvariable = entradaN,font = ("Times New Roman",12), width = 28).place(x=70, y=211)#width elonga la casilla de escritura
#entradaN.set("Bryan Parra")

#Crear la entrada de datos
entrada = StringVar()
lstdat = Entry (ventana, textvariable = entrada, width = 21).place(x=340,y=154)

#Creando un campo de texto para Lugar
entradaL = StringVar()#Variables declaradas de tipos string o de texto
txtLugar = Entry (ventana, textvariable = entradaL, font = ("Times New Roman",12), width = 28, justify = "center").place(x=56, y=181)
#entradaL.set("Bogota D.C")

#Creando un campo numerico para Altura 
entradaA = DoubleVar() #DoubleVar() sirve para declarar variables numericas reales
txtAltura = Entry (ventana, textvariable = entradaA,font = ("Times New Roman",12), width = 22).place(x=120, y=311)

#Creando un campo numerico para Precipitacion
entradaP = DoubleVar()
txtPrecipitacion = Entry (ventana, textvariable = entradaP,font = ("Times New Roman",12), width = 20).place(x=136, y=341)

#Creando un campo numerico para Temperatura
entradaT = DoubleVar()
txtTemperatura = Entry (ventana, textvariable = entradaT,font = ("Times New Roman",12), width = 21).place(x=128, y=371)

#Creando una lista
lstdatos = Listbox (ventana, width = 35, height = 12)
#lstdatos.insert (0, "Bogota D.C , bs-MB") #El indice me indica (primer numero) la posicion vertical que va ocupando cada lista generada, .insert me permite ir agregando datos
lstdatos.insert (1, "Malaga, bh-MB")

#Crear Botones 
btnGetV = Button (ventana, text = "Get Values", command = lambda : clima(entradaL.get()), bg = "#062", fg = "white", relief = "raised", font = ("Times New Roman", 11),width = 8).place(x=130, y=211)#el parametro command es necesario para generar estos eventos o asignar o devolver el saludo cuando se haga clic sobre el boton generado

#btnDespedir = Button (ventana, text = "Despedir", command = despide, font = ("Times New Roman", 12),width = 10).place(x=1, y=565)

btnSalir = Button (ventana, text="Salir", command = ventana.quit, fg = "red", font = ("Times New Roman", 12), width = 6).place(x=470, y=565)  #boton para Salir

btnCalcular = Button (ventana, text = "Run",bg = "white", fg = "darkgreen", command = calcular, relief = "groove", font = ("Times New Roman", 12), width = 4).place(x=380, y=410)

#btnImprimir = Button (ventana, text = "Imprimir", command = imprime,fg = "blue", font =("Times New Roman", 12), width = 7).place(x=120, y=565)

btnAgregar = Button (ventana, text = "Agregar", fg = "black", bg = "white" , width = 6, command = agregar, font =("Times New Roman", 10)).place(x=475,y=150)

#
lstdatos.place(x=312,y=184) #Solo de esta manera me permite ubicar mi lista, al final.  

#Receta para crear menus

#Paso 1. Crear la Barra de Menus 
barraMenu = Menu (ventana, )

#Paso 2. Creare los Menus
mnuArchivo = Menu (barraMenu)
mnuEdicion = Menu (barraMenu)

#Paso 3. Crear los comandos de los menus (add.command llama los comandos)

def abrirfichero (): 
    fichero = filedialog.askopenfile (title = "Abrir")
    print (fichero)

mnuArchivo.add_command (label = "Abrir", command = abrirfichero)
mnuArchivo.add_command (label = "Nuevo")
mnuArchivo.add_command (label = "Guardar", command = guardar)
mnuArchivo.add_command (label = "Cerrar")

#Crear Separadores 
mnuArchivo.add_separator ()#-------------------------------------------
mnuArchivo.add_command (label = "Salir", command = ventana.quit)

#######
mnuEdicion.add_command (label = "Copiar")
mnuEdicion.add_command (label = "Pegar")
mnuEdicion.add_command (label = "Deshacer")
mnuEdicion.add_command (label = "Rehacer")

#Paso 4. Agregar los Menus a la Barra de Menus
barraMenu.add_cascade (label = "Archivo", menu = mnuArchivo) #Metodo para agregar los menus en cascadas o orden descendente

######
barraMenu.add_cascade (label = "Edicion", menu = mnuEdicion) #Metodo para agregar los menus en cascadas o orden descendente

#Paso 5. Indicar que la Barra de Menus estara en la ventana
ventana.config (menu = barraMenu)

#
ventana.mainloop()#.mainloop siempre al final de la creacion 

