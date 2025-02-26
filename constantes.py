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


lista_meta = []
charcos = []
autos_cpu = []

temporizador_iniciado = False  # 🚀 Nueva bandera para controlar el temporizador
seleccionado = False  # Bandera para controlar que solo se seleccione una vez

ganador_auto_principal = False
flag_ganador = False

ranking_ejemplo = ranking_ejemplo = [
    {"name": "______", "time": "00:05:30", "score": 1000},    
]
x_presionada = False
x_presionada_previamente = False
# constantes.py