import pygame
import sys
from constantes import ALTURA_VENTANA, ANCHO_VENTANA
from instacia_objetos import fondo
from fondo import Fondo
fondo_ = Fondo("carretera.png")     

# Inicializar Pygame
pygame.init()

COLOR_TEXTO = (255, 255, 255)
COLOR_TEXTO_RESALTADO = (255, 255, 0)  # Amarillo cuando se resalta
FUENTE = pygame.font.Font(None, 50)

# Posiciones de los textos
posicion_nivel1 = (ANCHO_VENTANA // 2 - 100, ALTURA_VENTANA // 2 - 50)
posicion_nivel2 = (ANCHO_VENTANA // 2 - 100, ALTURA_VENTANA // 2 + 50)

# Rectángulos invisibles para la detección de colisión
rect_nivel1 = pygame.Rect(posicion_nivel1[0], posicion_nivel1[1], 200, 50)
rect_nivel2 = pygame.Rect(posicion_nivel2[0], posicion_nivel2[1], 200, 50)

def seleccionar_nivel(ventana):
    """
    Función que muestra la pantalla de selección de nivel y detecta la elección del usuario.
    """
    global fondo
    seleccionado = False
    nivel_seleccionado = None

    while not seleccionado:
        ventana.blit(fondo_.imagen, fondo_.posicion)  # Fondo negro solo para la selección de nivel

        # Obtener la posición actual del mouse
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Determinar si el mouse está sobre las opciones
        resaltar_nivel1 = rect_nivel1.collidepoint(mouse_x, mouse_y)
        resaltar_nivel2 = rect_nivel2.collidepoint(mouse_x, mouse_y)

        # Renderizar los textos con color resaltado si el mouse está sobre ellos
        color_nivel1 = COLOR_TEXTO_RESALTADO if resaltar_nivel1 else COLOR_TEXTO
        color_nivel2 = COLOR_TEXTO_RESALTADO if resaltar_nivel2 else COLOR_TEXTO

        texto_nivel1 = FUENTE.render("Nivel 1", True, color_nivel1)
        texto_nivel2 = FUENTE.render("Nivel 2", True, color_nivel2)

        ventana.blit(texto_nivel1, posicion_nivel1)
        ventana.blit(texto_nivel2, posicion_nivel2)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Click izquierdo
                if resaltar_nivel1:
                    nivel_seleccionado = 1
                    seleccionado = True
                elif resaltar_nivel2:
                    nivel_seleccionado = 2
                    seleccionado = True

    # Mostrar mensaje del nivel seleccionado
    ventana.blit(fondo_.imagen, fondo_.posicion)  # Fondo negro solo para la selección de nivel
    texto_nivel = FUENTE.render(f"Nivel {nivel_seleccionado} Seleccionado", True, COLOR_TEXTO)
    ventana.blit(texto_nivel, (ANCHO_VENTANA // 2 - 150, ALTURA_VENTANA // 2))
    pygame.display.update()
    pygame.time.wait(2000)  # Esperar 2 segundos antes de iniciar la carrera

    return True, nivel_seleccionado
