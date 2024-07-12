import pygame
from config import *
from modulos import *

#se carga las imagenes y se reescalan al tamaño deseado de manera global
img_inicio = pygame.image.load(IMAGEN_INICIO)
img_inicio = pygame.transform.scale(img_inicio,(ANCHO,ALTO))
img_boton_inicio = pygame.image.load(IMAGEN_BOTON_INICIO)
img_boton_inicio = pygame.transform.scale(img_boton_inicio,(194,124))
img_puntuacion = pygame.image.load(IMAGEN_PUNTUACION)
img_puntuacion = pygame.transform.scale(img_puntuacion,(ANCHO,ALTO))
img_juego = pygame.image.load(IMAGEN_JUEGO)
img_juego = pygame.transform.scale(img_juego,(ANCHO,ALTO))
img_llamada = pygame.image.load(IMAGEN_LLAMADA)
pantalla = pygame.display.set_mode((ANCHO,ALTO))


def pantalla_inicio (mouse_x:int, mouse_y:int):
    """
        pantalla_inicio (mouse_x:int, mouse_y:int)
        mouse_x: se ingresa por parametro la ubicacion en x del mouse al clickear
        mouse_y: se ingresa por parametro la ubicacion en y del mouse al clickear
        la funcion es para tener la primera ventana inicial en pantalla y esperar a que el usuario inicie el juego
    """
    boton_activado = False
    pantalla.fill(BLANCO)
    pantalla.blit(img_inicio,(0,0))

    if (mouse_x > 506 and mouse_x < 700) and (mouse_y > 500 and mouse_y < 630):
        pantalla.blit(img_boton_inicio,(506,506))
        boton_activado = True
    else:
        pantalla.blit(img_inicio,CORDENADA_CERO)
    return boton_activado

def pantalla_puntuacion(mouse_x:int, mouse_y:int ,nick:str ,matriz_puntuacion:list):

    """
        pantalla_puntuacion(mouse_x:int, mouse_y:int ,nick:str ,matriz_puntuacion:list)
        mouse_x: se ingresa por parametro la ubicacion en x del mouse al clickear
        mouse_y: se ingresa por parametro la ubicacion en y del mouse al clickear
        nick: se ingesa por parametro el estado del nick en el momento (hace referencia a lo que se ingresa por teclado)
        matriz_puntuacion: se ingresa la matriz con todos los records

        parte uno:
        en la primera parte(mitad de la pantalla) se muestra un recuadro en el que se le pide al usuario que ingrese su nick de max 3 digitos para poder continuar 
        
        parte dos:
        en esta parte de la funcion la matriz con la puntuacion se muestra por pantalla los 3 primero puestos que son los primeros de la lista(con anterioridad fue ordenado de mayor a menor) 
    """
    validar_nick = False
    fuente = pygame.font.SysFont(FUENTE,70)
    nickname = fuente.render(nick.upper(), True, NEGRO)
    pantalla.fill(BLANCO)
    pantalla.blit(img_puntuacion,CORDENADA_CERO)
    pygame.draw.rect(pantalla,OSCURO,(260,430,ANCHO_PUNTUACION,ALTO_PUNTUACION))
    pygame.draw.rect(pantalla,OSCURO2,(260,430,352,ALTO_PUNTUACION))
    pygame.draw.rect(pantalla,BLANCO,(375,465,140,50))
    pantalla.blit(nickname,(380,465))
    boton_activado = botones_tamanio(img_boton_inicio,(354,530),(354,550,530,650),mouse_y,mouse_x)
    if boton_activado == True and len(nick) == 3:
        validar_nick = True
    #*2
    fuente = pygame.font.SysFont(FUENTE,40)
    texto_alto_puntaje = fuente.render("HIGH SCORES",True,AZUL)
    texto_alto_puntaje = pantalla.blit(texto_alto_puntaje,(680,465))
    ubicacion_subtitulo_y = texto_alto_puntaje.top
    for i in range(len(matriz_puntuacion)):
        if i < 3:
            texto_top3 = f"{matriz_puntuacion[i][0].upper()}  {(matriz_puntuacion[i][1])}"
            texto_top3 = fuente.render(texto_top3,True,BLANCO,NEGRO)
            ubicacion_subtitulo_y += 50
            pantalla.blit(texto_top3,(700, ubicacion_subtitulo_y))
        else:
            break
    return validar_nick

def pantalla_juego():
    """
        pantalla_juego()
        la funcion se encarga de borrar pantalla a la plantilla base en el juego
    """
    pantalla.fill(BLANCO)
    pantalla.blit(img_juego,CORDENADA_CERO)
    return True

def juego(mouse_x:int,mouse_y:int,dic_pregunta:dict,respuestas_lista:list,nivel:int,ayudas,tiempos):

    """
    
    """
    retorno = True
    letreto_bank = f"{total_premio(nivel)}"
    letrero_nivel = f"nivel : {nivel+1}"
    fuente = pygame.font.SysFont(FUENTE,40)
    
    letrero_tiempo = f"{tiempos}"
    letrero_tiempo = fuente.render(letrero_tiempo,True,BLANCO,NEGRO)
    if mouse_x > 60 and mouse_x < 415:
        if mouse_y > 550 and mouse_y < 615:
            respuestas_lista[nivel] = 1
        elif mouse_y > 630 and mouse_y < 700:
            respuestas_lista[nivel] = 3
    elif mouse_x > 450 and mouse_x < 805:
        if mouse_y > 550 and mouse_y < 615:
            respuestas_lista[nivel] = 2
        elif mouse_y > 630 and mouse_y < 700:
            respuestas_lista[nivel] = 4
    

    if ayudas[2] == True and mouse_x > 1200 and mouse_x < 1265 and mouse_y > 10 and mouse_y < 75 :
        ayudas[2] = False
    elif ayudas[2] == False and ayudas[3] == True:
        ayuda_cincuenta(dic_pregunta["resultado"],fuente,dic_pregunta,respuestas_lista[0])
    else:
        match respuestas_lista[nivel]:
            case 1:
                pantalla_juego()
                texto_pregunta = fuente.render(dic_pregunta["pregunta"],True,BLANCO)
                pantalla.blit(texto_pregunta,(70,460))
                texto_respuesta1 = fuente.render(dic_pregunta["respuestas"][0],True,NEGRO,CELESTE)
                texto_respuesta2 = fuente.render(dic_pregunta["respuestas"][1],True,NEGRO)
                texto_respuesta3 = fuente.render(dic_pregunta["respuestas"][2],True,NEGRO)
                texto_respuesta4 = fuente.render(dic_pregunta["respuestas"][3],True,NEGRO)
            case 2:
                pantalla_juego()
                texto_pregunta = fuente.render(dic_pregunta["pregunta"],True,BLANCO)
                pantalla.blit(texto_pregunta,(70,460))
                texto_respuesta1 = fuente.render(dic_pregunta["respuestas"][0],True,NEGRO)
                texto_respuesta2 = fuente.render(dic_pregunta["respuestas"][1],True,NEGRO,CELESTE)
                texto_respuesta3 = fuente.render(dic_pregunta["respuestas"][2],True,NEGRO)
                texto_respuesta4 = fuente.render(dic_pregunta["respuestas"][3],True,NEGRO)
            case 3:
                pantalla_juego()
                texto_pregunta = fuente.render(dic_pregunta["pregunta"],True,BLANCO)
                pantalla.blit(texto_pregunta,(70,460))
                texto_respuesta1 = fuente.render(dic_pregunta["respuestas"][0],True,NEGRO)
                texto_respuesta2 = fuente.render(dic_pregunta["respuestas"][1],True,NEGRO) 
                texto_respuesta3 = fuente.render(dic_pregunta["respuestas"][2],True,NEGRO,CELESTE)
                texto_respuesta4 = fuente.render(dic_pregunta["respuestas"][3],True,NEGRO)
            case 4:
                pantalla_juego()
                texto_pregunta = fuente.render(dic_pregunta["pregunta"],True,BLANCO)
                pantalla.blit(texto_pregunta,(70,460))
                texto_respuesta1 = fuente.render(dic_pregunta["respuestas"][0],True,NEGRO)
                texto_respuesta2 = fuente.render(dic_pregunta["respuestas"][1],True,NEGRO)
                texto_respuesta3 = fuente.render(dic_pregunta["respuestas"][2],True,NEGRO)
                texto_respuesta4 = fuente.render(dic_pregunta["respuestas"][3],True,NEGRO,CELESTE)
            case _:
                pantalla_juego()
                texto_pregunta = fuente.render(dic_pregunta["pregunta"],True,BLANCO)
                pantalla.blit(texto_pregunta,(70,460))
                texto_respuesta1 = fuente.render(dic_pregunta["respuestas"][0],True,NEGRO)
                texto_respuesta2 = fuente.render(dic_pregunta["respuestas"][1],True,NEGRO)
                texto_respuesta3 = fuente.render(dic_pregunta["respuestas"][2],True,NEGRO)
                texto_respuesta4 = fuente.render(dic_pregunta["respuestas"][3],True,NEGRO)
        pantalla.blit(texto_respuesta1,(85,570))
        pantalla.blit(texto_respuesta2,(470,570))
        pantalla.blit(texto_respuesta3,(85,660))
        pantalla.blit(texto_respuesta4,(470,660))
        pantalla.blit(letrero_tiempo,(0,0))


    if respuestas_lista[nivel] > 0 :
        texto_confirmar = fuente.render("confirmar",True,NEGRO,CELESTE)
        pantalla.blit(texto_confirmar,(30,30))
        if mouse_x > 30 and mouse_x < 160 and mouse_y > 30 and mouse_y < 60:
            if respuestas_lista[nivel] == (dic_pregunta["resultado"]):
                mensaje = fuente.render("correcto",True,NEGRO,CELESTE)
                pantalla.blit(mensaje,(30,70))
                retorno = "nivel+"
            else:
                mensaje = fuente.render("incorrecto",True,NEGRO,CELESTE)
                pantalla.blit(mensaje,(30,70))
                retorno = False
            if ayudas[2] == False:
                ayudas[3] = False
            pygame.display.update()
            pygame.time.delay(2000) 
    


    if ayudas[0] == True and mouse_x > 1040 and mouse_x < 1105 and mouse_y > 10 and mouse_y < 75 :
        ayuda_publico(dic_pregunta["resultado"],fuente)
        ayudas[0] = False
    if ayudas[1] == True and mouse_x > 1120 and mouse_x < 1185 and mouse_y > 10 and mouse_y < 75 :
        ayuda_amigo(dic_pregunta["resultado"],fuente)
        ayudas[1] = False
    letreto_bank = fuente.render(letreto_bank,True,BLANCO,NEGRO)
    letrero_nivel = fuente.render(letrero_nivel,True,BLANCO)
    pantalla.blit(letrero_nivel,(1030,110))
    pantalla.blit(letreto_bank,(55,195))
    return retorno


def ayuda_publico(respuesta:int,fuente:pygame.font.Font):
    """
        ayuda_publico(respuesta:int,fuente:pygame.font.Font)
        respuesta: se ingresa por parametro la respuesta correcta
        fuente: se ingresa la variable de tipo Font para obtener la surface de un texto
        la funcion es un mensaje para el usuario cuando usa la ayuda del publico
    """
    mensaje_ayuda = f"El publico voto por : {respuesta}"
    mensaje_ayuda = fuente.render(mensaje_ayuda,True,BLANCO)
    pantalla.blit(mensaje_ayuda,(315,180))
    pygame.display.update()
    pygame.time.delay(3000)

def ayuda_amigo(respuesta:int,fuente:pygame.font.Font):
    """
        ayuda_amigo(respuesta:int,fuente:pygame.font.Font)
        respuesta: se ingresa por  parametro la respuesta correcta
        fuente: se ingresa la variable de tipo Font para obtener la surface de un texto
        la funcion es para recibir mensaje de un amigo con la respuesta correcta como ayuda
    """
    mensaje_ayuda = f"Bro para mi es la {respuesta}"
    mensaje_ayuda = fuente.render(mensaje_ayuda,True,BLANCO)
    pantalla.blit(img_llamada,(335,70))
    pantalla.blit(mensaje_ayuda,(315,200))
    pygame.display.update()
    pygame.time.delay(3000)

def ayuda_cincuenta(respuesta:int,fuente:pygame.font.Font,dic_pregunta:dict,opcion:int):
    """
        ayuda_cincuenta(respuesta:int,fuente:pygame.font.Font,dic_pregunta:dict,opcion:int)
        respuesta: se ingresa por  parametro la respuesta correcta
        fuente: se ingresa la variable de tipo Font para obtener la surface de un texto
        dic_pregunta : se ingresa por parametro el diccionario con toda la informacion de la pregunta
        opcion: la respuesta ingresada por el usuario
        la funcion muestra por pantalla dependiendo de la respuesta correcta la mitad de las respuestas para el usuario de  forma de ayuda
    """
    pantalla_juego()
    texto_pregunta = fuente.render(dic_pregunta["pregunta"],True,BLANCO)
    pantalla.blit(texto_pregunta,(70,460))
    texto_pregunta = fuente.render(dic_pregunta["pregunta"],True,BLANCO)
    pantalla.blit(texto_pregunta,(70,460))
    if respuesta == 1 or respuesta == 3:
        match opcion:
            case  1:
                texto_respuesta1 = fuente.render(dic_pregunta["respuestas"][0],True,NEGRO,CELESTE)
                texto_respuesta3 = fuente.render(dic_pregunta["respuestas"][2],True,NEGRO)
            case 3:
                texto_respuesta1 = fuente.render(dic_pregunta["respuestas"][0],True,NEGRO)
                texto_respuesta3 = fuente.render(dic_pregunta["respuestas"][2],True,NEGRO,CELESTE)
            case _:
                texto_respuesta1 = fuente.render(dic_pregunta["respuestas"][0],True,NEGRO)
                texto_respuesta3 = fuente.render(dic_pregunta["respuestas"][2],True,NEGRO)
        pantalla.blit(texto_respuesta1,(85,570))
        pantalla.blit(texto_respuesta3,(85,660))
    else:
        match opcion:
            case 2:
                texto_respuesta2 = fuente.render(dic_pregunta["respuestas"][1],True,NEGRO,CELESTE)
                texto_respuesta4 = fuente.render(dic_pregunta["respuestas"][3],True,NEGRO)
            case 4:
                texto_respuesta2 = fuente.render(dic_pregunta["respuestas"][1],True,NEGRO)
                texto_respuesta4 = fuente.render(dic_pregunta["respuestas"][3],True,NEGRO,CELESTE)
            case _:
                texto_respuesta2 = fuente.render(dic_pregunta["respuestas"][1],True,NEGRO)
                texto_respuesta4 = fuente.render(dic_pregunta["respuestas"][3],True,NEGRO)
        pantalla.blit(texto_respuesta2,(470,570))
        pantalla.blit(texto_respuesta4,(470,660))
    pygame.display.update()

def botones_tamanio(surface_boton:pygame.surface.Surface, cordenada:tuple, ubicacion:tuple, mouse_y:int, mouse_x:int):
    """
        botones_tamanio(surface_boton:pygame.surface.Surface, cordenada:tuple, ubicacion:tuple, mouse_y:int, mouse_x:int)
        surface_boton: se ingresa la surface del boton
        cordenada: es donde se pondra la surface del boton grande
        ubicacion: es un tupla de tamaño 4, las primeras 2 son para validar la pos x y las ultimas 2 para valida pos en y para hacer el boton mas grandre al ser clickeado durante un instante
    """
    boton_activado = False
    ancho = surface_boton.get_width()
    alto = surface_boton.get_height()
    if (mouse_x > ubicacion[0] and mouse_x < ubicacion[1] and mouse_y > ubicacion[2] and mouse_y < ubicacion[3]):
        surface_boton_tamanio = pygame.transform.scale(surface_boton,(ancho+10,alto+10))
        pantalla.blit(surface_boton_tamanio,(cordenada[0]-5,cordenada[1]-5))
        boton_activado = True
    else:
        pantalla.blit(surface_boton,cordenada)
    return boton_activado