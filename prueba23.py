import pygame
import math
import random

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
ANCHO, ALTO = 800, 600
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Carrera con Auto CPU")

# Colores
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)  # Auto del jugador
AZUL = (0, 0, 255)  # Auto de la CPU

# Tamaños de los autos
ANCHO_AUTO, ALTO_AUTO = 50, 100

# Posiciones iniciales
pos_x_jugador = ANCHO // 2
pos_y_jugador = ALTO - 150  # Jugador en la parte baja de la pantalla

pos_x_cpu = ANCHO // 2
pos_y_cpu = 100  # CPU más arriba en la pantalla

# Variables de control
velocidad_jugador = 5
velocidad_cpu = 2
amplitud_movimiento = 170  # Mayor amplitud de oscilación
tiempo = 0  
factor_aleatorio = random.uniform(0.7, 1.3)
ruido_aleatorio = 0  
cambio_brusco = 0  
zigzag = 0  
pos_x_cpu_objetivo = pos_x_cpu  # Posición objetivo para interpolación

# Bucle principal del juego
ejecutando = True
while ejecutando:
    pygame.time.delay(30)  # Controla la velocidad del juego
    
    # Manejo de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
    
    # Movimiento del auto del jugador (controlado por el usuario)
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and pos_x_jugador > 50:
        pos_x_jugador -= velocidad_jugador
    if teclas[pygame.K_RIGHT] and pos_x_jugador < ANCHO - 100:
        pos_x_jugador += velocidad_jugador

    # Movimiento del auto CPU
    tiempo += 0.07 * factor_aleatorio  # Más rápido

    # Aumento del ruido con fluctuaciones más agresivas
    ruido_aleatorio += random.uniform(-3, 3)  
    ruido_aleatorio = max(-15, min(ruido_aleatorio, 15))  # Ruido más fuerte pero controlado

    # Cambio brusco ocasional con corrección progresiva
    if random.random() < 0.03:  # 3% de probabilidad
        cambio_brusco = random.uniform(-60, 60)

    cambio_brusco *= 0.92  # Disminuir gradualmente

    # Zigzag aleatorio para simular correcciones en la dirección
    zigzag = math.sin(tiempo * 4) * random.randint(5, 15)

    # Nueva posición objetivo con más ruido y zigzags
    pos_x_cpu_objetivo = (ANCHO // 2) + math.sin(tiempo) * amplitud_movimiento + cambio_brusco + ruido_aleatorio + zigzag
    pos_x_cpu = pygame.math.lerp(pos_x_cpu, pos_x_cpu_objetivo, 0.2)  # Interpolación con más impacto

    # Dibujar elementos en pantalla
    VENTANA.fill(NEGRO)
    pygame.draw.rect(VENTANA, ROJO, (pos_x_jugador, pos_y_jugador, ANCHO_AUTO, ALTO_AUTO))  
    pygame.draw.rect(VENTANA, AZUL, (pos_x_cpu, pos_y_cpu, ANCHO_AUTO, ALTO_AUTO))  

    pygame.display.update()

pygame.quit()
