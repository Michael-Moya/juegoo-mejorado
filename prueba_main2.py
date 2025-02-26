import pygame, sys, os
from constantes import *
from instacia_objetos import *
from nivel import seleccionar_nivel
from prueba_temporizador import iniciar_temporizador_carrera
from prueba12_menu import mostrar_menu  # Función que muestra el menú y devuelve "jugar" o "ranking"
from prueba_ranking import mostrar_ranking  # Pantalla del ranking
from prueba_funciones import *
# Supongamos que existe una función para actualizar el ranking si se supera el último lugar:
from prueba_ranking import actualizar_ranking

from prueba_ventana_resultado import mostrar_pantalla_resultado  # Devuelve "volver_jugar" o "menu"
#from funciones import *

def jugar():
  print(f"Antes de reiniciar: Auto principal en id {id(auto_principal)}")
  print(f"Antes de reiniciar: Meta final ID = {id(meta_final)}")
 
  print(f"Después de reiniciar: Meta final ID = {id(meta_final)}")
  print(f"Después de reiniciar: Auto principal en  id {id (auto_principal )}")
  #reiniciar_objetos()
  accion = None
  avance = 0
  # Reiniciamos todos los objetos y variables
  lista_meta = lista_lineas_meta
  seleccionado, nivel_seleccionado = seleccionar_nivel(ventana)
  charcos = generar_charcos_por_nivel(nivel_seleccionado)
  iniciar_temporizador_carrera(ventana)
  #print(id(lista_meta),"iniciooo") # estoy utilizando la misma lista copiada en Temporizador como prueba
  
  global flag_ganador  # <-- Asegurar que se está usando la variable global
  global ganador_auto_principal
  flag_ganador = False  # <-- Reiniciarla aquí para evitar problemas

  # Variable para almacenar el tiempo en que se detectó el ganador
  tiempo_ganador = None  
  while cerrar_ventana():   
    lista_meta = filtrar_linea_meta(lista_lineas_meta)
    # Ajustar la frecuencia de generación
    avance, charcos,lista_meta, flag_ganador, ganador_auto_principal = iniciar_movimiento_juego(ventana, fondo, auto_principal, avance, auto_cpu, charcos, lista_meta)
    
    print(f"flag_ganador dentro de jugar(): {flag_ganador}")  # <-- Verificar si realmente cambia
    fundir_todo(ventana, fondo, auto_principal, auto_cpu, charcos, lista_meta)     
    
    # if flag_ganador == True :
    #   print(f"flag_ganador ============={flag_ganador}")
    #   print(ganador_auto_principal)
    #   mostrar_pantalla_resultado(ventana, ganador_auto_principal, ranking_ejemplo)
    #   break
    if flag_ganador:
      print(f"flag_ganador ============={flag_ganador}")
      print(ganador_auto_principal)

      # Guardar el tiempo en que se detectó el ganador (solo la primera vez)
      if tiempo_ganador is None:
          tiempo_ganador = pygame.time.get_ticks()

    # Si pasaron 3 segundos desde que se detectó un ganador, mostramos la pantalla de resultados
    if tiempo_ganador is not None and pygame.time.get_ticks() - tiempo_ganador >= 1000:
        accion = mostrar_pantalla_resultado(ventana, ganador_auto_principal, ranking_ejemplo)
        break  # Salimos del bucle para finalizar la partida
    pygame.display.flip()
    reloj.tick(FPS)
    
  print("-------------------SALIMOS Y ENTRAMOS A LOS 3 SEGUNDOS-------------")
  print("------------------MOSTRAMOS PANTALLA RESULTADO-------------")
 
  return accion  

def main():
  """Bucle principal del juego."""
  while True:
    opcion_menu = mostrar_menu(ventana)
    
    if opcion_menu == "jugar":
      accion = jugar()
      # Según la acción del resultado, se vuelve al menú o se reinicia la partida
      if accion == "menu":
        continue  # Vuelve al menú principal y reinicia objetos en la siguiente iteración
      elif accion == "volver_jugar":
        print ("VOLVER A JUGAR")
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
