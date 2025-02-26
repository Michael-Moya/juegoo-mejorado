# pantalla_resultado.py
import pygame
import sys
from instacia_objetos import fondo, ALTURA_VENTANA, ANCHO_VENTANA
import instacia_objetos
# Constantes (ajústalas según tu proyecto)
BLANCO  = (255, 255, 255)
NEGRO   = (0, 0, 0)
AZUL    = (0, 0, 255)
AMARILLO = (255, 215, 0)
ROJO    = (255, 0, 0)

def mostrar_pantalla_resultado(ventana, resultado, tiempo=""):
    print(f"⚠️ SE MUESTRA LA PANTALLA DE RESULTADOS | GANADOR: {resultado}")  # 🔥 Imprimir el resultado
    """
    Muestra una pantalla de resultado en la misma ventana.
    
    Parámetros:
      - ventana: la superficie de Pygame donde dibujar.
      - resultado: valor booleano; True si ganó el jugador, False si ganó la CPU.
      - tiempo: cadena con el tiempo obtenido (se muestra solo si ganó el jugador).
    
    Devuelve:
      - "volver_jugar" si se selecciona volver a jugar.
      - "menu" si se selecciona volver al menú.
    """
    global fondo
    reloj = pygame.time.Clock()
    fuente_titulo = pygame.font.Font(None, 72)
    fuente_texto = pygame.font.Font(None, 48)
    fuente_boton = pygame.font.Font(None, 36)
    
    # Intentar cargar imágenes para el resultado
    try:
        imagen_trofeo = pygame.image.load("trofeo.png")
        imagen_trofeo = pygame.transform.scale(imagen_trofeo, (400, 400))
        imagen_cara_triste = pygame.image.load("carita_triste.png")
        imagen_cara_triste = pygame.transform.scale(imagen_cara_triste, (400, 400))
    except Exception as error:
        print("No se pudo cargar alguna imagen:", error)
        imagen_trofeo = None
        imagen_cara_triste = None

    # Definir botones para "Volver a Jugar" y "Menú"
    ancho_boton = 200
    alto_boton = 50
    margen_boton = 20
    btn_volver_jugar = pygame.Rect(
        (ANCHO_VENTANA // 2 - ancho_boton - margen_boton // 2),
        ALTURA_VENTANA - alto_boton - margen_boton,
        ancho_boton,
        alto_boton
    )
    btn_menu = pygame.Rect(
        (ANCHO_VENTANA // 2 + margen_boton // 2),
        ALTURA_VENTANA - alto_boton - margen_boton,
        ancho_boton,
        alto_boton
    )

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Detectar clicks en los botones
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                pos_mouse = evento.pos
                if btn_volver_jugar.collidepoint(pos_mouse):
                    return "volver_jugar"
                elif btn_menu.collidepoint(pos_mouse):
                    return "menu"

        # Dibujar el fondo
        ventana.blit(fondo.imagen, fondo.posicion)
        
        # Configurar mensajes según el resultado
        if resultado == True:
            mensaje = f"¡Ganaste {instacia_objetos.auto_principal.nombre}!"
            submensaje = f"Tiempo: {tiempo}"
            color_mensaje = AZUL
        else:
            mensaje = "¡Perdiste!"
            submensaje = "La CPU llegó primero"
            color_mensaje = ROJO

        # Renderizar textos principales
        texto_mensaje = fuente_titulo.render(mensaje, True, color_mensaje)
        texto_submensaje = fuente_texto.render(submensaje, True, NEGRO)
        ventana.blit(texto_mensaje, (ANCHO_VENTANA // 2 - texto_mensaje.get_width() // 2, ALTURA_VENTANA // 2 - 220))
        ventana.blit(texto_submensaje, (ANCHO_VENTANA // 2 - texto_submensaje.get_width() // 2, ALTURA_VENTANA // 2 - 140))
        
        # Mostrar imagen o símbolo según el resultado
        if resultado == True:
            if imagen_trofeo:
                ventana.blit(imagen_trofeo, (350, 300))
            else:
                # Dibujar una estrella como alternativa
                puntos = [
                    (ANCHO_VENTANA // 2, ALTURA_VENTANA // 2 - 70),
                    (ANCHO_VENTANA // 2 + 20, ALTURA_VENTANA // 2 - 30),
                    (ANCHO_VENTANA // 2 + 60, ALTURA_VENTANA // 2 - 20),
                    (ANCHO_VENTANA // 2 + 30, ALTURA_VENTANA // 2 + 10),
                    (ANCHO_VENTANA // 2 + 40, ALTURA_VENTANA // 2 + 50),
                    (ANCHO_VENTANA // 2, ALTURA_VENTANA // 2 + 30),
                    (ANCHO_VENTANA // 2 - 40, ALTURA_VENTANA // 2 + 50),
                    (ANCHO_VENTANA // 2 - 30, ALTURA_VENTANA // 2 + 10),
                    (ANCHO_VENTANA // 2 - 60, ALTURA_VENTANA // 2 - 20),
                    (ANCHO_VENTANA // 2 - 20, ALTURA_VENTANA // 2 - 30)
                ]
                pygame.draw.polygon(ventana, AMARILLO, puntos)
        else:
            if imagen_cara_triste:
                ventana.blit(imagen_cara_triste, (350, 300))
            else:
                # Dibujar una cruz como alternativa
                pygame.draw.line(ventana, ROJO, (ANCHO_VENTANA // 2 - 50, ALTURA_VENTANA // 2 - 50),
                                 (ANCHO_VENTANA // 2 + 50, ALTURA_VENTANA // 2 + 50), 10)
                pygame.draw.line(ventana, ROJO, (ANCHO_VENTANA // 2 + 50, ALTURA_VENTANA // 2 - 50),
                                 (ANCHO_VENTANA // 2 - 50, ALTURA_VENTANA // 2 + 50), 10)
        
        # Dibujar botones en la parte inferior
        # Botón "Volver a Jugar"
        pygame.draw.rect(ventana, AZUL, btn_volver_jugar)
        texto_volver = fuente_boton.render("Volver a Jugar", True, BLANCO)
        ventana.blit(
            texto_volver,
            (
                btn_volver_jugar.x + (btn_volver_jugar.width - texto_volver.get_width()) // 2,
                btn_volver_jugar.y + (btn_volver_jugar.height - texto_volver.get_height()) // 2
            )
        )
        # Botón "Menú"
        pygame.draw.rect(ventana, AZUL, btn_menu)
        texto_menu = fuente_boton.render("Menú", True, BLANCO)
        ventana.blit(
            texto_menu,
            (
                btn_menu.x + (btn_menu.width - texto_menu.get_width()) // 2,
                btn_menu.y + (btn_menu.height - texto_menu.get_height()) // 2
            )
        )
        
        pygame.display.flip()
        reloj.tick(30)
