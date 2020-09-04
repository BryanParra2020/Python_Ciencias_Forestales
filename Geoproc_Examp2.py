# -*- coding: utf-8 -*-
# Credits: QGIS Colombia
"""

Bryan Daniel Parra Prieto 

Forest Engineering; Industrial University of Santander 

Date: wednesday 27-08-2020 

Hour: 22:30 """ 


"""
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                    *
*   QGIS Colombia
*   
*******  
*    Documentacion empleada: 
*
*    CookBook QGIS: https://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/
*    QGIS API Documentation: https://qgis.org/api/group__core.html
*    Documentos de QGIS: https://docs.qgis.org/testing/en/docs/user_manual/processing/scripts.html
*    Definiendo parámetros de entrada: https://api.qgis.org/master/classQgsProcessingParameterDefinition.html
*    Definiendo parámetros de salida: https://api.qgis.org/master/classQgsProcessingOutputDefinition.html
*    Leyendo parámetros: https://api.qgis.org/master/classQgsProcessingAlgorithm.html
*    ¡GitHub!  https://github.com/qgis/QGIS 
                                                                     *
***************************************************************************
"""

""" 
El siguiente algoritmo usa el decorador @alg para:  
 
1. Renombrar un campo de una capa vectorial existente, para esto se necesitara como minimo los siguientes parametros de entrada (ver documentacion, parametros de entrada): 

a. Vector layer (Capa vectorial)
b. Campo a renombrar
c. Nombre nuevo para el campo 

cuyo parametro de salida será: 

a'. Vector layer
"""

#Importando los modulos necesarios 

from qgis.processing import alg #Para generar los decoradores o interfaces PyQt5
from qgis.core import edit #Para que me permita editar

#Definiendo los metadatos del metodo o funcion (en este caso son tres entradas)

#Definiendo el nombre del decorador para el nombre
@alg (name = "renombrar_campo", label = "Renombrar campo de capa vectorial",
     group = "examplescripts", group_label = "Example scripts")

#Definiendo la entrada vectorial, en este caso de tipo vectorial del algortimo que aparecera en el decorador
@alg.input (type = alg.VECTOR_LAYER, name = "INPUT", 
            label = "Input vector layer") #type hace referencia l tipo de entrada que deseo, en este caso una de tipo vectorial (alg.VECTOR_LAYER) revisar documentacion parametros de entrada segun sea el caso

#Definiendo la entrada para el campo, en este caso de tipo campo del algortimo que aparecera en el decorador
@alg.input (type = alg.FIELD, name = "INPUT_FIELD", 
            label = "Input field", parentLayerParameterName = "INPUT") # tipo campo (alg.FIELD), el argumento parentLayerParameterName permite asociar el valor del campo a la entrada o paraemtro de la capa padre, en este caso al vector de entrada, cuyo nombre es INPUT, si no se hace esto, QGIS no entiende de donde desea obtener el valor del campo

#Definiendo la entrada para el renombrar el campo, en este caso de tipo string, en este caso de tipo vectorial del algortimo que aparecera en el decorador
@alg.input (type = alg.STRING, name = "NEW_FIELD_NAME", 
            label = "New field name") # tipo campo a renombrar string (alg.STRING)

#Definiendo el parametro de salida (solo sera una salida en este caso)
@alg.output (type = alg.VECTOR_LAYER, name = "OUTPUT",
            label = "Vector layer rename field") # tipo vector layer, ya que su campo sera renombrado, REVISAR DOCUMENTACION PARA PARAMETROS DE SALIDA

#Definiendo el metodo o funcion 

def renombrar_campo (instance, parameters, context, feedback, inputs): #Parametros intactos, no se modifican
    
    #Documentacion sencilla del algoritmo
    """
    Description of the algorithm.
    (Rename fields)

    """

    #Leer los parametros de entrada, revisar documentacion para leer los paraemtros de entrada

    source = instance.parameterAsVectorLayer (parameters, 
                                              "INPUT", context) #Como es un parametro de tipo vectorial por eso a instance le pasamos la forma de leer vectores (parametersAsVectorLayer), Revisar documentacion 

    input_field = instance.parameterAsFields (parameters, 
                                             "INPUT_FIELD", context) [0] #Como es un parametro de tipo campo por eso a instance le pasamos la forma de leer campos (parametersAsFields), Revisar documentacion, el parametro por sintaxis de Python despliega una lista con una serie de campos, porque esta en plurar, en este caso como solo seleccionaremos un campo accedemos a esa lista a traves de [0], como primer indice
 
    new_name = instance.parameterAsString (parameters, 
                                             "NEW_FIELD_NAME", context) #Como es un parametro de tipo string por eso a instance le pasamos la forma de leer cadenas de texto campos (parametersAsString), Revisar documentacion

    #Buscar en documentacion para procesar nuestro algortimo utlizando los parametros, en la pagina QGIS API Documentation

    #Para el primer parametro, como es VectorLayer, buscar documentacion referente a procesar con capas vectoriales, dentro de la pagina anterior (QGIS API Documentation)
    
    #En este caso buscar un metodo (en Class VectorLayer) que permita renombrar campos en la capa vectorial 
    
    idx = source.fields().indexOf(input_field) #Obteniendo el indice que necesita renombrar 
    
    #Sesion de edicion para capas vectoriales, formato traido de la pagina de cookbook para desarrolladores en QGIS (Revisar documentacion)
    with edit (source):
        
        source.renameAttribute (idx, new_name) #Como parametros me pide el indice del campo y el nuevo nombre (revisar documentacion)

    return {"OUTPUT": source} #Nuetros algoritmo Retorna de valor un diccionario

#FIN DEL SCRIPT
