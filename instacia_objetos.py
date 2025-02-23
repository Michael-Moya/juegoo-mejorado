import pygame
from constantes import *
from fondo import *
from auto import * 
from auto_principal import *
from auto_cpu import *
from linea_meta import * 
from funciones import generar_charcos
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
