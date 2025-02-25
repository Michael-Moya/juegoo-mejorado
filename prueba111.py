import pygame, sys, os
from constantes import ANCHO_VENTANA, ALTURA_VENTANA, FPS  , seleccionado
from instacia_objetos import reiniciar_objetos, ventana, fondo, auto_principal, auto_cpu, lista_lineas_meta, avance, charcos, ranking_ejemplo, reloj
from nivel import seleccionar_nivel
from prueba_temporizador import iniciar_temporizador_carrera
from prueba12_menu import mostrar_menu  # Función que muestra el menú y devuelve "jugar" o "ranking"
from prueba_ventana_resultado import mostrar_pantalla_resultado  # Devuelve "volver_jugar" o "menu"
from prueba_ranking import mostrar_ranking  # Pantalla del ranking
from funciones import generar_charcos_por_nivel,iniciar_movimiento_juego, fundir_todo, filtrar_linea_meta, cerrar_ventana
# Supongamos que existe una función para actualizar el ranking si se supera el último lugar:
from ranking import actualizar_ranking
import pygame
from constantes import *
from fondo import *
from auto import * 
from auto_principal import *
from funciones import *
from instacia_objetos import*
from nivel import *
from prueba_temporizador import iniciar_temporizador_carrera
from prueba12_menu import mostrar_menu
from prueba_ranking import mostrar_ranking
import os
def jugar():	
  lista_meta = lista_lineas_meta
  seleccionado, nivel_seleccionado = seleccionar_nivel(ventana)
  charcos = generar_charcos_por_nivel(nivel_seleccionado)
  iniciar_temporizador_carrera(ventana)
  #temporizador_iniciado = False  # 🔥 Se activa la bandera para evitar que se ejecute nuevamente
  #print(id(lista_meta),"iniciooo") # estoy utilizando la misma lista copiada en Temporizador como prueba

  while cerrar_ventana():   
		lista_meta = filtrar_linea_meta(lista_lineas_meta)
		avance, charcos,lista_meta = iniciar_movimiento_juego(ventana, fondo, auto_principal, avance, auto_cpu, charcos, lista_meta)
		fundir_todo(ventana, fondo, auto_principal, auto_cpu, charcos, lista_meta)
		pygame.display.flip()
		reloj.tick(FPS)
		
		#----------------------------------------
		"""Función que encapsula la partida."""
		# Reiniciamos todos los objetos y variables
		reiniciar_objetos()
		
		# Selección de nivel y generación de elementos
		seleccionado, nivel_seleccionado = seleccionar_nivel(ventana)
		global  avance
		charcos = generar_charcos_por_nivel(nivel_seleccionado)
		iniciar_temporizador_carrera(ventana)
		avance = 0

		# Variables de partida
		partida_terminada = False
		resultado_partida = None  # True = gana el jugador, False = gana la CPU
		tiempo_juego = "00:00:00"  # Aquí se debe obtener el tiempo real

	# Bucle principal de la partida
	while cerrar_ventana():
	  lista_lineas_meta = filtrar_linea_meta(lista_lineas_meta)
		avance, charcos, lista_lineas_meta = iniciar_movimiento_juego(
			ventana, fondo, auto_principal, avance, auto_cpu, charcos, lista_lineas_meta
		)
		fundir_todo(ventana, fondo, auto_principal, auto_cpu, charcos, lista_lineas_meta)
		pygame.display.flip()
		reloj.tick(FPS)
		
		# Condición de fin de partida (simulada; aquí se debe detectar el cruce de la meta)
		if avance > 1000:
			# Por ejemplo, si el jugador cruza primero:
			resultado_partida = True   # O False, según corresponda
			tiempo_juego = "00:05:30"    # Tiempo obtenido en la partida
			partida_terminada = True
			break

	# Si ganó el jugador, se permite anotar en el ranking si supera el último puesto
	if resultado_partida and supera_ultimo_ranking(auto_principal, ranking_ejemplo):
		# Se llama a una función que permita ingresar el nombre y actualice el ranking
		ranking_ejemplo = actualizar_ranking(auto_principal, tiempo_juego, ranking_ejemplo)
	
	# Mostrar la pantalla de resultado y obtener la acción: "volver_jugar" o "menu"
	accion = mostrar_pantalla_resultado(ventana, resultado_partida, tiempo_juego)
	return accion

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
