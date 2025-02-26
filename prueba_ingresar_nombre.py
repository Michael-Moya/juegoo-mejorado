import pygame
from instacia_objetos import fondo
def ingresar_nombre(ventana):
    """Permite al jugador ingresar su nombre en Pygame antes de comenzar la carrera."""
    fuente = pygame.font.Font(None, 50)
    texto_ingresado = ""
    activo = True
    color_fondo = (0, 0, 0)  # Negro
    color_texto = (255, 255, 255)  # Blanco

    input_rect = pygame.Rect(300, 300, 400, 50)  # Posición y tamaño del cuadro de entrada

    while activo:
        ventana.blit(fondo.imagen, fondo.posicion)  # Limpiar pantalla con color de fondo

        # Renderizar instrucciones
        texto_instruccion = fuente.render("Ingresa tu nombre y presiona ENTER", True, color_texto)
        ventana.blit(texto_instruccion, (200, 200))

        # Manejo de eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:  # Enter para confirmar
                    return texto_ingresado
                elif evento.key == pygame.K_BACKSPACE:  # Borrar caracteres
                    texto_ingresado = texto_ingresado[:-1]
                else:
                    if len(texto_ingresado) < 15:  # Limitar a 15 caracteres
                        texto_ingresado += evento.unicode

        # Dibujar caja de entrada
        pygame.draw.rect(ventana, (255, 255, 255), input_rect, 2)  # Borde blanco

        # Renderizar texto ingresado
        superficie_texto = fuente.render(texto_ingresado, True, color_texto)
        ventana.blit(superficie_texto, (input_rect.x + 10, input_rect.y + 10))

        pygame.display.flip()  # Actualizar pantalla
        pygame.time.delay(50)  # Pequeña pausa para mejorar rendimiento
