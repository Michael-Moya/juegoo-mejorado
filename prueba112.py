# instancia_objetos.py
import pygame
from constantes import *
from fondo import Fondo
from auto_principal import AutoPrincipal
from auto_cpu import AutoCpu
from linea_meta import Meta

def reiniciar_objetos():
    """
    Reinicia y crea nuevamente todos los objetos y variables del juego.
    """
    global ventana, fondo, auto_principal, auto_cpu, meta_inicio, meta_final, lista_lineas_meta, avance, charcos, ranking_ejemplo, reloj, tiempo_inicio

    # Crear la ventana
    ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTURA_VENTANA))
    
    # Crear el fondo y los autos
    fondo = Fondo("carretera.png")
    auto_principal = AutoPrincipal()
    auto_cpu = AutoCpu(POSICION_INICIAL_CPU)
    
    # Crear las metas (por ejemplo, inicio y final)
    meta_inicio = Meta([0, 0])
    meta_final = Meta([0, -3000])
    lista_lineas_meta = [meta_inicio, meta_final]
    
    # Reiniciar variables de avance y elementos móviles
    avance = 0
    charcos = []
    
    # Reiniciar ranking (puedes mantenerlo o reiniciarlo según tu lógica)
    ranking_ejemplo = [
        {"name": "______", "time": "00:05:30", "score": 1000},
    ]
    
    # Reiniciar el reloj y el tiempo de inicio
    reloj = pygame.time.Clock()
    tiempo_inicio = pygame.time.get_ticks()

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

    temporizador_iniciado = False  # 🚀 Nueva bandera para controlar el temporizador

    lista_meta = []
    charcos = []
    autos_cpu = []

    seleccionado = False
    ranking_ejemplo = ranking_ejemplo = [
        {"name": "______", "time": "00:05:30", "score": 1000},    
    ]