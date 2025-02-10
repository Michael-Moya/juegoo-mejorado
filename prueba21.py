import pygame
import random

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
ancho, alto = 800, 600
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Movimiento Aleatorio")

# Colores
blanco = (255, 255, 255)
rojo = (255, 0, 0)

# Posición y tamaño del cuadrado
x, y = ancho // 2, alto // 2
tamano = 50
velocidad = 5

# Reloj para controlar la tasa de refresco
clock = pygame.time.Clock()

# Bucle principal
corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # Elegir una dirección aleatoria
    direccion = random.choice([(5, 0), (-5, 0)])  # derecha, izquierda, abajo, arriba

    # Mover el cuadrado
    x += direccion[0] * velocidad
    y += direccion[1] * velocidad

    # Mantener el cuadrado dentro de la pantalla
    if x < 0: x = 0
    if x > ancho - tamano: x = ancho - tamano
    if y < 0: y = 0
    if y > alto - tamano: y = alto - tamano

    # Limpiar la pantalla
    pantalla.fill(blanco)

    # Dibujar el cuadrado
    pygame.draw.rect(pantalla, rojo, (x, y, tamano, tamano))

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la tasa de refresco
    clock.tick(30)  # 30 FPS

# Cerrar Pygame
pygame.quit()
