import pygame
import json
import random

def leer_puntuacion_csv(matriz_puntuacion:list):
    """
        leer_puntuacion_csv(matriz_puntuacion:list)
        matriz_puntuacion: se ingresa por parametro la matriz donde se guardaran el historial de puntajes

        la funcion carga el archivo .csv guardando en una lista separado por , el nombre del jugador y record para guardarlo en la matriz 
    """
    with open("puntuacion.csv","r",encoding="utf-8") as archivo:
        for linea in archivo:
            fila = []
            nick_puntaje = linea.replace("\n","")
            nick_puntaje = nick_puntaje.split(",")
            fila.append(nick_puntaje[0])
            fila.append(int(nick_puntaje[1]))
            matriz_puntuacion.append(fila)

def ordenar_puntajes(matriz_puntuacion:list):
    """
        ordenar_puntajes(matriz_puntuacion:list)
        matriz_puntuacion: se ingresa por parametro la matriz que se ordenara
        la funcion ordena las filas de la matriz teniendo en cuenta la puntuacion de mayor a menor
    """
    for i in range(len(matriz_puntuacion)):
        for j in range(len(matriz_puntuacion)-i-1):
            if matriz_puntuacion[j][1] < matriz_puntuacion[j+1][1]:
                auxiliar = matriz_puntuacion[j]
                matriz_puntuacion[j] = matriz_puntuacion[j+1]
                matriz_puntuacion[j+1] = auxiliar

def leer_preguntas_json(lista_preguntas_respuestas:list):
    """
        leer_preguntas_json(lista_preguntas_respuestas:list)
        lista_preguntas_respuestas: se ingresa por parametro la lista donde se guardara las preguntas
        se carga la lista de diccionarios del archivo .json que contiene las preguntas, respuestas posibles y la respuesta correcta
    """
    with open("preguntas.json","r",encoding = "utf-8") as archivo:
        lista_preguntas_respuestas.extend(json.load(archivo))
        
def elegir_pregunta_random(lista_preguntas_respuestas:list):
    """
        elegir_pregunta_random(lista_preguntas_respuestas:list)
        lista_preguntas_respuestas: se ingresa por parametro la lista de preguntas
        la funcion busca un numero al azar entre 0 y la gantidad de preguntas cargadas
    """
    numero_pregunta = random.randint(0,len(lista_preguntas_respuestas)-1)
    return numero_pregunta

def guardar_puntuacion_csv(matriz_puntuacion:list):
    """
    guardar_puntuacion_csv(matriz_puntuacion:list)
    matriz_puntuacion: la matriz que se ingresa por parametro esta actualizada con nuevas puntuaciones
    la funcion guarda la matriz que tiene nuevas puntuaciones cargadas al archivo .csv cada fila de la matriz es una linea y se guarda separado por una coma
    """
    with open("puntuacion.csv","w",encoding="utf-8") as archivo:
        texto_lineas = ""
        for i in range(len(matriz_puntuacion)):
            nombre = matriz_puntuacion[i][0]
            puntaje_ronda = matriz_puntuacion[i][1]
            if i < len(matriz_puntuacion) - 1:
                texto_lineas += f"{nombre},{puntaje_ronda}\n"
            else:
                texto_lineas += f"{nombre},{puntaje_ronda}"
            
        archivo.write(texto_lineas)

def total_premio(nivel:int):
    """
       total_premio(nivel:int)
       nivel: se ingresa por parametro el nivel en el que se desea calcular el premio obtenido
       la funcion valida cual es el premio obtenido en la hasta el momento, se usa varios for en momentos donde se cumple un patron de premio
       retorna el numero con el premio 
    """
    premio = 0
    if nivel < 4 and nivel > 0:
        for _ in range(nivel):
            premio +=100
    if nivel >= 4 and nivel < 12:
        repeticiones = nivel - 4
        premio = 500
        if repeticiones > 0:    
            for _ in range(repeticiones):
                premio *=2
    if nivel >= 12 and nivel < 15:
        repeticiones = nivel - 13
        premio = 125000
        if repeticiones > 0:
            premio *=2
    return premio

