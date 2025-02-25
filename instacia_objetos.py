import pygame
from constantes import *
from fondo import *
from auto import * 
from auto_principal import *
from auto_cpu import *
from linea_meta import * 
reloj = pygame.time.Clock()
#Se crea una ventana
ventana = pygame.display.set_mode((ANCHO_VENTANA,ALTURA_VENTANA)) 
# elementos del juego
fondo = Fondo("carretera.png")     
auto_principal = AutoPrincipal()
auto_cpu = AutoCpu(POSICION_INICIAL_CPU)
meta_inicio = Meta([0,0])
meta_final = Meta([0,-3000])
lista_lineas_meta = [meta_inicio, meta_final]

reloj = pygame.time.Clock()


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
