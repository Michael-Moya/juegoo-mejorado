import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

start_time = pygame.time.get_ticks()  # Tiempo de inicio en milisegundos
waiting = True

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Verificamos si han pasado 3000 milisegundos (3 segundos)
    if waiting and pygame.time.get_ticks() - start_time >= 3000:
        waiting = False
        print("Han pasado 3 segundos")

    # Aquí puedes seguir actualizando tu juego, dibujando, etc.
    screen.fill((0, 0, 0))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
