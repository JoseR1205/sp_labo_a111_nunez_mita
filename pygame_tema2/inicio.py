import pygame
from config import*
from pantalla import*
from modulos import*



pygame.init()

pygame.display.set_caption("¿Quién quiere ser millonario?")
fps = pygame.time.Clock()

ejecutar = True
texto = ""
ventana = 1
nivel = 0

matriz_puntaje = []
lista_preguntas = []
list_respuesta = [0]*15
ayudas = [True]*4
nuevo_jugador = []

leer_puntuacion_csv(matriz_puntaje)
ordenar_puntajes(matriz_puntaje)
leer_preguntas_json(lista_preguntas)

fondo_juego = True
pregunta_numero = elegir_pregunta_random(lista_preguntas)
aux_time = 30
while ejecutar : 
    x = -1
    y = -1


    for evento in pygame.event.get():
        print(evento)
        if evento.type == pygame.QUIT:
            ejecutar = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            x = evento.pos[0]
            y = evento.pos[1]
        elif evento.type == pygame.TEXTINPUT and ventana == 2:
            if len(texto) < 3:
                texto += evento.text
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_BACKSPACE and ventana == 2:
                texto = texto[0:len(texto)-1]
    
    match ventana:
        case 1 :
            siguiente = pantalla_inicio(x,y)
            if siguiente == True:
                ventana = 2
        case 2 :
            siguiente = pantalla_puntuacion(x,y,texto,matriz_puntaje)
            if siguiente == True:
                nuevo_jugador.append(texto)
                ventana = 3
        case 3 :
            tiempo = int(pygame.time.get_ticks()/1000)
            if fondo_juego == True:
                siguiente_nivel = pantalla_juego()
                fondo_juego = False

            juego_proceso = juego(x,y,lista_preguntas[pregunta_numero],list_respuesta,nivel,ayudas,tiempo)
            if juego_proceso == False or nivel == 15 or tiempo == aux_time:
                nuevo_jugador.append(total_premio(nivel))
                matriz_puntaje.append(nuevo_jugador)
                print(matriz_puntaje)
                guardar_puntuacion_csv(matriz_puntaje)
                #reseteo los valores para volver a jugar
                nuevo_jugador.clear()
                texto = ""
                ventana = 1
                nivel = 0
                matriz_puntaje = []
                lista_preguntas = []
                list_respuesta = [0]*15
                nuevo_jugador = []
                leer_puntuacion_csv(matriz_puntaje)
                ordenar_puntajes(matriz_puntaje)
                leer_preguntas_json(lista_preguntas)
                fondo_juego = True
                pregunta_numero = elegir_pregunta_random(lista_preguntas)
                ayudas = [True]*4

            elif juego_proceso == "nivel+":
                aux_time+=30
                pregunta_numero = elegir_pregunta_random(lista_preguntas)
                nivel+=1
            print(tiempo)
    
    fps.tick(60)

    pygame.display.update()

pygame.quit()



