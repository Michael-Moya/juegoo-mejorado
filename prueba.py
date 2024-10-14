import pygame
from constantes import *
from Fondo import *
from auto import * 
from auto_principal import *
from funciones import *
from instacia_objetos import*

pygame.init() 
pygame.display.set_caption("Racing")
while cerrar_ventana():     
  lista_meta = generar_linea_meta(lista_lineas_meta)
  if not juego_pausado:
    if random.randint(1, 30) == 1:  # Ajustar la frecuencia de generación
      charcos = generar_charcos(charcos, avance) 
  avance, charcos,lista_meta = iniciar_movimiento_juego(ventana, fondo, auto_principal, avance, auto_cpu, charcos, lista_meta)
  fundir_todo(ventana, fondo, auto_principal, auto_cpu, charcos, lista_meta)
  
  print(len(lista_meta))
  #print(auto_principal.posicion_relativa, "AUTO PRINCIPAL")
  #print(auto_cpu.posicion_relativa, "auto CPU")
  pygame.display.flip()
  reloj.tick(FPS)
pygame.quit() 
"""try:
    persona.edad = -5
except ValueError as e:
    print(e) 
    """  
