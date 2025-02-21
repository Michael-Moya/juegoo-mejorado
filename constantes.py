import colores
import pygame
ANCHO_VENTANA = 1000
ALTURA_VENTANA = 700
POSICION_FONDO_Y= 0
POSICION_FONDO_X= 0
FPS = 50
MOV_FONDO = 30

POSICION_INICIAL_CPU = [600, 400]

ANCHO_RECT_AUTO = 100
ALTURA_RECT_AUTO = 200
POSICION_CHARCO_X = 0
POSICION_CHARCO_Y = 0
COLOR_TIMER = colores.WHITE

COLOR_RECT_AUTO = colores.RED1
COLOR_RECT_CHARCO = colores.BROWN

#Variables iniciadoras
avance = 0
running = True
juego_pausado = False
# Variables de tiempo
tiempo_inicio = pygame.time.get_ticks()
tiempo_espera = 100  # Tiempo de espera en milisegundos
tiempo_diferencia = 0

charcos = []
autos_cpu = []
