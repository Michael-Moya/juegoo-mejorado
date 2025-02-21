import pygame
import sys
from constantes import ANCHO_VENTANA,ALTURA_VENTANA
# Inicializar Pygame

pygame.init()

# Definir tamaños de ventana y colores
ANCHO, ALTO = ANCHO_VENTANA, ALTURA_VENTANA
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
COLOR_FONDO = (0, 0, 0)
COLOR_TEXTO = (255, 255, 255)

# Fuentes
FUENTE = pygame.font.Font(None, 50)

# Variables de control
nivel_seleccionado = None  # Al principio no hay nivel seleccionado
seleccionado = False  # Bandera para controlar que solo se seleccione una vez

def seleccionar_nivel(ventana):
  global seleccionado
  global nivel_seleccionado
  # Si el nivel no ha sido seleccionado, mostrar opciones para seleccionar
  if not seleccionado:
    ventana.fill(COLOR_FONDO)
    
    # Mostrar opciones de nivel
    texto_nivel1 = FUENTE.render("Nivel 1", True, COLOR_TEXTO)
    texto_nivel2 = FUENTE.render("Nivel 2", True, COLOR_TEXTO)
    
    ventana.blit(texto_nivel1, (ANCHO // 2 - 100, ALTO // 2 - 50))
    ventana.blit(texto_nivel2, (ANCHO // 2 - 100, ALTO // 2 + 50))

    pygame.display.flip()

    # Detectar click del mouse para seleccionar un nivel
    if pygame.mouse.get_pressed()[0]:  # Si el botón izquierdo del mouse está presionado
      mouse_x, mouse_y = pygame.mouse.get_pos()
      
      # Verificar si se hizo clic en el Nivel 1
      if ANCHO // 2 - 100 <= mouse_x <= ANCHO // 2 + 100 and ALTO // 2 - 50 <= mouse_y <= ALTO // 2:
        nivel_seleccionado = 1
        seleccionado = True  # Cambiar la bandera a True para que no se seleccione más de una vez

      # Verificar si se hizo clic en el Nivel 2
      elif ANCHO // 2 - 100 <= mouse_x <= ANCHO // 2 + 100 and ALTO // 2 + 50 <= mouse_y <= ALTO // 2 + 150:
        nivel_seleccionado = 2
        seleccionado = True  # Cambiar la bandera a True para que no se seleccione más de una vez

  else:
    ventana.fill(COLOR_FONDO)
    if nivel_seleccionado == 1:
      texto_nivel = FUENTE.render("Nivel 1 Seleccionado", True, COLOR_TEXTO)
    elif nivel_seleccionado == 2:
      texto_nivel = FUENTE.render("Nivel 2 Seleccionado", True, COLOR_TEXTO)
    
    ventana.blit(texto_nivel, (ANCHO // 2 - 150, ALTO // 2))
    pygame.display.flip()
    # Esperar unos segundos antes de pasar al siguiente nivel
    pygame.time.wait(5000)
    #break  # Salir del bucle para continuar con el siguiente nivel del juego
  return seleccionado, nivel_seleccionado    

