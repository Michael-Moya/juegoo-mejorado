import pygame
from colores import *
from constantes import *
# Colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WIDTH, HEIGHT = 800, 600

def show_menu(screen):
    while True:
        screen.fill(WHITE)
        font = pygame.font.Font(None, 74)
        title_text = font.render("Círculos que caen", True, BLACK)
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 2 - 100))

        # Opciones del menú
        font = pygame.font.Font(None, 48)
        play_text = font.render("JUGAR", True, BLUE)
        ranking_text = font.render("RANKING", True, BLACK)
        exit_text = font.render("SALIR", True, BLACK)

        play_rect = play_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        ranking_rect = ranking_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
        exit_rect = exit_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))

        screen.blit(play_text, play_rect)
        screen.blit(ranking_text, ranking_rect)
        screen.blit(exit_text, exit_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Botón izquierdo del ratón
                    if play_rect.collidepoint(event.pos):
                        return "play"
                    elif ranking_rect.collidepoint(event.pos):
                        return "ranking"
                    elif exit_rect.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()