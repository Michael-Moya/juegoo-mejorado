import pygame
from constantes import *
from fondo import *
from auto import * 
from auto_principal import *
from funciones import *
from instacia_objetos import*
from nivel import *
from prueba_temporizador import iniciar_temporizador_carrera
from prueba12_menu import mostrar_menu, mostrar_pantalla_ranking
import os
os.system('cls')  # Limpia el terminal en Windows
pygame.init()
pygame.display.set_caption("Racing")
print(auto_cpu.posicion_relativa,"iniciooooooooooooooooooooooooooooooooo")
charcos = []
temporizador_iniciado = False 
seleccionado = False  # Bandera para controlar que solo se seleccione una vez

if mostrar_menu(ventana) == "jugar" :  
  lista_meta = lista_lineas_meta
  seleccionado, nivel_seleccionado = seleccionar_nivel(ventana)
  charcos = generar_charcos_por_nivel(nivel_seleccionado)
  iniciar_temporizador_carrera(ventana)
  temporizador_iniciado = True  # 🔥 Se activa la bandera para evitar que se ejecute nuevamente
  print(id(lista_meta),"iniciooo") # estoy utilizando la misma lista copiada en Temporizador como prueba

  while cerrar_ventana():   
    lista_meta = filtrar_linea_meta(lista_lineas_meta)

    # Ajustar la frecuencia de generación
    print(len(charcos))
    avance, charcos,lista_meta = iniciar_movimiento_juego(ventana, fondo, auto_principal, avance, auto_cpu, charcos, lista_meta)
    fundir_todo(ventana, fondo, auto_principal, auto_cpu, charcos, lista_meta)
    pygame.draw.line(ventana, (255, 0, 0), (100, 100), (700, 500), 1)
    #print(len(lista_meta))
    #print(auto_principal.posicion_relativa, "AUTO PRINCIPAL")
    j = 1
    for i in charcos:
      if isinstance(i, Charco):
        print("------------------------------------------")
        print(i.posicion_relativa, f" {j} posicion relativa")
        print(i.posicion)
      j+=1
    #print(auto_principal.posicion_real, "auto PRINCIPAL")
    #print( Meta._ultima_meta.posicion_relativa)

    pygame.display.flip()
    reloj.tick(FPS)
elif mostrar_menu(ventana) == "ranking" :
  mostrar_pantalla_ranking(ventana)
pygame.quit() 
