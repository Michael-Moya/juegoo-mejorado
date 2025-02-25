import pygame, sys, os
from constantes import *
from instacia_objetos import *
from nivel import seleccionar_nivel
from prueba_temporizador import iniciar_temporizador_carrera
from prueba12_menu import mostrar_menu  # Función que muestra el menú y devuelve "jugar" o "ranking"
from prueba_ranking import mostrar_ranking  # Pantalla del ranking
from funciones import iniciar_movimiento_juego, fundir_todo, filtrar_linea_meta, cerrar_ventana, generar_charcos_por_nivel
# Supongamos que existe una función para actualizar el ranking si se supera el último lugar:
from prueba_ranking import actualizar_ranking

from prueba_ventana_resultado2 import mostrar_pantalla_resultado  # Devuelve "volver_jugar" o "menu"
#from funciones import *
partida_terminada = False

def jugar():
  global temporizador_iniciado, seleccionado
  avance = 0
  # Reiniciamos todos los objetos y variables
  reiniciar_objetos()
  lista_meta = lista_lineas_meta
  seleccionado, nivel_seleccionado = seleccionar_nivel(ventana)
  charcos = generar_charcos_por_nivel(nivel_seleccionado)
  iniciar_temporizador_carrera(ventana)
  temporizador_iniciado = True  # 🔥 Se activa la bandera para evitar que se ejecute nuevamente
  #print(id(lista_meta),"iniciooo") # estoy utilizando la misma lista copiada en Temporizador como prueba
  
  flag_mostrar_pantalla_resultado = False
  tiempo_inicio_pantalla_resultado = None
  while cerrar_ventana():   
    lista_meta = filtrar_linea_meta(lista_lineas_meta)
    avance, charcos,lista_meta, flag_terminada = iniciar_movimiento_juego(ventana, fondo, auto_principal, avance, auto_cpu, charcos, lista_meta)
    fundir_todo(ventana, fondo, auto_principal, auto_cpu, charcos, lista_meta)   
    
    if flag_terminada :
      tiempo_inicio_pantalla_resultado = pygame.time.get_ticks()
      flag_mostrar_pantalla_resultado = True

    if flag_mostrar_pantalla_resultado:
      tiempo_actual = pygame.time.get_ticks()
      if tiempo_actual - tiempo_inicio_pantalla_resultado >= 3000:
        flag_espera = False
        print("Han pasado 3 segundos")
        accion = mostrar_pantalla_resultado(ventana, ranking_ejemplo)
      return accion
    
    pygame.display.flip()
    reloj.tick(FPS)
    # if avance > 1000:
    #   # Por ejemplo, si el jugador cruza primero:
    #   resultado_partida = True   # O False, según corresponda
    #   tiempo_juego = "00:05:30"    # Tiempo obtenido en la partida
    #   partida_terminada = True
    #   break

    # # Si ganó el jugador, se permite anotar en el ranking si supera el último puesto
    # if resultado_partida and supera_ultimo_ranking(auto_principal, ranking_ejemplo):
    #   # Se llama a una función que permita ingresar el nombre y actualice el ranking
    #   ranking_ejemplo = actualizar_ranking(auto_principal, tiempo_juego, ranking_ejemplo)
    

    #----------------------------------------
  #"""Función que encapsula la partida."""
  
  # # Selección de nivel y generación de elementos
  # seleccionado, nivel_seleccionado = seleccionar_nivel(ventana)
  # global charcos, avance
  # charcos = generar_charcos_por_nivel(nivel_seleccionado)
  # iniciar_temporizador_carrera(ventana)
  # avance = 0

  # # Variables de partida
  # partida_terminada = False
  # resultado_partida = None  # True = gana el jugador, False = gana la CPU
  # tiempo_juego = "00:00:00"  # Aquí se debe obtener el tiempo real

  # # Bucle principal de la partida
  # while cerrar_ventana():
  #   lista_lineas_meta = filtrar_linea_meta(lista_lineas_meta)
  #   avance, charcos, lista_lineas_meta = iniciar_movimiento_juego(
  #       ventana, fondo, auto_principal, avance, auto_cpu, charcos, lista_lineas_meta
  #   )
  #   fundir_todo(ventana, fondo, auto_principal, auto_cpu, charcos, lista_lineas_meta)
  #   pygame.display.flip()
  #   reloj.tick(FPS)
    
  #   # Condición de fin de partida (simulada; aquí se debe detectar el cruce de la meta)
  #   if avance > 1000:
  #       # Por ejemplo, si el jugador cruza primero:
  #       resultado_partida = True   # O False, según corresponda
  #       tiempo_juego = "00:05:30"    # Tiempo obtenido en la partida
  #       partida_terminada = True
  #       break

  #   # Si ganó el jugador, se permite anotar en el ranking si supera el último puesto
  #   if resultado_partida and supera_ultimo_ranking(auto_principal, ranking_ejemplo):
  #       # Se llama a una función que permita ingresar el nombre y actualice el ranking
  #       ranking_ejemplo = actualizar_ranking(auto_principal, tiempo_juego, ranking_ejemplo)
    
    # Mostrar la pantalla de resultado y obtener la acción: "volver_jugar" o "menu"


def main():
  """Bucle principal del juego."""
  while True:
    opcion_menu = mostrar_menu(ventana)
    
    if opcion_menu == "jugar":
      accion = jugar()
      # Según la acción del resultado, se vuelve al menú o se reinicia la partida
      if accion in ("volver_jugar", "menu"):
        continue  # Vuelve al menú principal y reinicia objetos en la siguiente iteración
            
    elif opcion_menu == "ranking":
      # Mostrar la pantalla del ranking con opción de regresar al menú
      mostrar_ranking(ventana, ranking_ejemplo)
    
    # Permitir salir del juego
    for evento in pygame.event.get():
      if evento.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
  os.system('cls')  # Limpia el terminal en Windows
  pygame.init()
  pygame.display.set_caption("Racing")
  main()
