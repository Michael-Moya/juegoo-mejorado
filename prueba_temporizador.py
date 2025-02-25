import pygame
from constantes import FPS
from instacia_objetos import reloj, fondo,charcos,auto_principal,auto_cpu, lista_lineas_meta
from funciones import fundir_todo

# Colores
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
GRIS = (100, 100, 100)

# Posiciones de los círculos
posiciones_circulos = [(200,200),(350,200),(500,200),(650,200),(800,200)]
radio_circulo = 30
temporizador_iniciado = False


def dibujar_circulos(pantalla, indice_activo):
    """Dibuja los círculos en la pantalla iluminando según el índice activo."""
    for i, posicion in enumerate(posiciones_circulos):
        color = ROJO if i < indice_activo else GRIS
        pygame.draw.circle(pantalla, color, posicion, radio_circulo)
    
    pygame.display.flip()

def iniciar_temporizador(pantalla):
    """Ejecuta la animación del temporizador de carrera con control de tiempo sin bloquear el juego."""
    indice_activo = 0
    tiempo_espera = 1000  # Milisegundos (1 seg por círculo)
    tiempo_inicio = pygame.time.get_ticks()

    corriendo = True
    while corriendo:
        reloj.tick(FPS)  # Mantener la tasa de cuadros

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()

        tiempo_actual = pygame.time.get_ticks()

        # Si ha pasado el tiempo de espera, avanza el temporizador
        if tiempo_actual - tiempo_inicio >= tiempo_espera:
            indice_activo += 1
            tiempo_inicio = tiempo_actual  # Reiniciar el tiempo de espera

            if indice_activo > len(posiciones_circulos):
                corriendo = False  # Finalizar animación

        # Actualizar fondo y objetos mientras corre el temporizador
        fundir_todo(pantalla, fondo, auto_principal, auto_cpu, charcos, lista_lineas_meta )
        # Dibujar los círculos actualizados
        dibujar_circulos(pantalla, indice_activo)

    # Al final, todos los círculos en verde sin bloquear
    for posicion in posiciones_circulos:
        pygame.draw.circle(pantalla, VERDE, posicion, radio_circulo)

    pygame.display.flip()

    # Esperar 1 segundo sin bloquear
    tiempo_final = pygame.time.get_ticks()
    while pygame.time.get_ticks() - tiempo_final < 1000:
        reloj.tick(FPS)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()

def iniciar_temporizador_carrera(ventana):
    ventana.blit(fondo.imagen,fondo.posicion)
    """Lanza el temporizador si no ha sido ejecutado previamente."""
    global temporizador_iniciado
    if not temporizador_iniciado:
        iniciar_temporizador(ventana)
        temporizador_iniciado = True  # Evita repetir el temporizador