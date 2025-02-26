import pygame
import random
import sys
from instacia_objetos import *


# Configuración de la ventana
WIDTH, HEIGHT = 1000, 700
pygame.display.set_caption("Carreras Heavy------")

# Colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
# Variables del juego
circUlos = []
radio_circulo = 20
velocidad_circulo = 5
tamano_cuadrado = 50
square_pos = [WIDTH // 2, HEIGHT - 100]
vidas = 3
game_paused = False

# Función para crear círculos

# Función para mover los círculos hacia abajo
def mover_circulos():
    for circulo in circulos:
        circulo[1] += velocidad_circulo  # Mover hacia abajo

# Función para comprobar colisiones
def comprobar_colision(posicion_cuadrado):
    global circulos, vidas
    for circulo in circulos:
        if (circulo[0] - posicion_cuadrado[0]) ** 2 + (circulo[1] - posicion_cuadrado[1]) ** 2 < (radio_circulo + tamano_cuadrado / 2) ** 2:
            circulos.remove(circulo)  # Eliminar el círculo si hay colisión
            vidas -= 1  # Perder una vida
            if vidas <= 0:
                return True  # Indicar que el juego debe pausar
    return False  # Indicar que el juego puede continuar

# Función para mostrar el menú
def mostrar_menu(pantalla):
    while True:
        ventana.blit(fondo.imagen, fondo.posicion)

        fuente = pygame.font.Font(None, 74)
        texto_titulo = fuente.render("Heavy Racing", True, BLACK)
        pantalla.blit(texto_titulo, (WIDTH // 2 - texto_titulo.get_width() // 2, HEIGHT // 2 - 100))

        # Opciones del menú
        fuente = pygame.font.Font(None, 48)
        texto_jugar = fuente.render("JUGAR", True, BLUE)
        texto_ranking = fuente.render("RANKING", True, BLACK)
        texto_salir = fuente.render("SALIR", True, BLACK)

        rect_jugar = texto_jugar.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        rect_ranking = texto_ranking.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
        rect_salir = texto_salir.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))

        pantalla.blit(texto_jugar, rect_jugar)
        pantalla.blit(texto_ranking, rect_ranking)
        pantalla.blit(texto_salir, rect_salir)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Botón izquierdo del ratón
                    if rect_jugar.collidepoint(event.pos):
                        return "jugar"
                    elif rect_ranking.collidepoint(event.pos):
                        return "ranking"
                    elif rect_salir.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()

# Función para mostrar la pantalla de ranking
def mostrar_pantalla_ranking(pantalla):
    while True:
        pantalla.fill(BLUE)
        fuente = pygame.font.Font(None, 74)
        texto_ranking = fuente.render("RANKING", True, WHITE)
        texto_volver = fuente.render("Presiona ESC para volver", True, WHITE)

        pantalla.blit(texto_ranking, (WIDTH // 2 - texto_ranking.get_width() // 2, HEIGHT // 2 - 100))
        pantalla.blit(texto_volver, (WIDTH // 2 - texto_volver.get_width() // 2, HEIGHT // 2))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Volver al menú
                    return
# # Función para mostrar la pantalla de fin del juego
# def show_game_over_screen():
#     while True:
#         screen.fill(WHITE)
#         font = pygame.font.Font(None, 74)
#         game_over_text = font.render("¡GAME OVER!", True, RED)
#         restart_text = font.render("REINICIAR", True, BLACK)
#         menu_text = font.render("VOLVER AL MENU", True, BLACK)

#         game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
#         restart_rect = restart_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
#         menu_rect = menu_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))

#         screen.blit(game_over_text, game_over_rect)
#         screen.blit(restart_text, restart_rect)
#         screen.blit(menu_text, menu_rect)

#         pygame.display.flip()

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if event.button == 1:  # Botón izquierdo del ratón
#                     if restart_rect.collidepoint(event.pos):
#                         return "restart"
#                     elif menu_rect.collidepoint(event.pos):
#                         return "menu"

# # Bucle principal del juego
# clock = pygame.time.Clock()

# # Mostrar menú
# while True:
#     choice = show_menu()

#     if choice == "play":
#         # Reiniciar el juego
#         circles.clear()
#         lives = 3
#         square_pos = [WIDTH // 2, HEIGHT - 100]
#         game_paused = False

#         while True:
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     pygame.quit()
#                     sys.exit()

#             if not game_paused:
#                 # Crear nuevos círculos
#                 if random.randint(1, 20) == 1:  # Ajustar la frecuencia de generación
#                     create_circle()

#                 # Mover círculos
#                 move_circles()
                
#                 # Comprobar colisiones
#                 if check_collision(square_pos):
#                     game_paused = True  # Pausar el juego si no hay vidas

#                 # Controlar el cuadrado
#                 keys = pygame.key.get_pressed()
#                 if keys[pygame.K_LEFT] and square_pos[0] > 0:
#                     square_pos[0] -= 5
#                 if keys[pygame.K_RIGHT] and square_pos[0] < WIDTH - square_size:
#                     square_pos[0] += 5

#             # Dibujar todo
#             screen.fill(WHITE)
#             for circle in circles:
#                 pygame.draw.circle(screen, RED, (circle[0], circle[1]), circle_radius)
#             pygame.draw.rect(screen, BLUE, (square_pos[0], square_pos[1], square_size, square_size))

#             # Mostrar el número de vidas
#             font = pygame.font.Font(None, 36)
#             text = font.render(f'Vidas: {lives}', True, BLACK)
#             screen.blit(text, (10, 10))

#             # Mostrar pausa si el juego está pausado
#             if game_paused:
#                 if lives <= 0:
#                     # Mostrar la pantalla de fin del juego
#                     final_choice = show_game_over_screen()
#                     if final_choice == "restart":
#                         # Reiniciar el juego
#                         circles.clear()
#                         lives = 3
#                         square_pos = [WIDTH // 2, HEIGHT - 100]
#                         game_paused = False
#                     elif final_choice == "menu":
#                         break  # Salir del bucle del juego para volver al menú
#                 else:
#                     pause_text = font.render('¡Juego Pausado! Presiona R para reiniciar', True, BLACK)
#                     screen.blit(pause_text, (WIDTH // 2 - pause_text.get_width() // 2, HEIGHT // 2))

#                     # Comprobar si se presiona R para reiniciar
#                     keys = pygame.key.get_pressed()
#                     if keys[pygame.K_r]:
#                         lives = 3
#                         circles.clear()
#                         square_pos = [WIDTH // 2, HEIGHT - 100]
#                         game_paused = False

#             pygame.display.flip()
#             clock.tick(30)  # Limitar a 30 FPS

#     elif choice == "ranking":
#         show_ranking_screen()  # Mostrar la pantalla de ranking
