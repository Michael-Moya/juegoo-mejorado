import pygame
from auto import *
from constantes import *
from auto_cpu import *

#timer_event = pygame.USEREVENT + 1  # Crear un nuevo evento
#pygame.time.set_timer(timer_event, 300)  # Evento cada 1000 ms (1 segundo)
class AutoPrincipal(Auto) :
  def __init__(self)-> None:
    super().__init__("auto_amarillo.jpg")
    self.nombre = "Auto_Principal-----"
    self.rect.topleft = [400,400]
    self.posicionar()
    self.rect.width = 100
    self.rect.height = 200
    self.color_rect = COLOR_RECT_AUTO
    self.cont = 0
    self.posicion_real = self.rect.topleft
    self.tiempo_inicio = None  # ⏳ Nuevo atributo para registrar tiempo de inicio

  def iniciar_tiempo_carrera(self):
      """Guarda el tiempo en que el auto comienza a moverse."""
      if self.tiempo_inicio is None:
          self.tiempo_inicio = pygame.time.get_ticks()

  def obtener_tiempo_transcurrido(self):
      """Calcula el tiempo en milisegundos desde el inicio hasta la meta."""
      if self.tiempo_inicio is not None:
          return pygame.time.get_ticks() - self.tiempo_inicio
      return 0  # Si nunca se inició, el tiempo es 0

  def reiniciar_tiempo_carrera(self):
      """Reinicia el tiempo de carrera al volver a jugar."""
      self.tiempo_inicio = None

  def mover(self, incremento):
    self.__direccionar()
    movimiento = self.__avanzar_o_retroceder()
    self.__avanzar_posicion_relativa(incremento, movimiento)
    #self.posicion_real_imagen = self.posicionar()
    self.posicionar()

  def __direccionar(self):
    keys = pygame.key.get_pressed() 
    if keys[pygame.K_RIGHT]:
      self.rect.x += 3
    elif keys[pygame.K_LEFT] :
      self.rect.x -= 3
    self.limitar_posicion_por_ventana()

  def __avanzar_o_retroceder(self)->int:
    movimiento = 0
    keys = pygame.key.get_pressed() 
    if keys[pygame.K_UP]:
      self.rect.y -= 1
      movimiento = 1
    elif keys[pygame.K_DOWN]:
      self.rect.y += 1   
      movimiento = -1   
    return movimiento
  
  def __avanzar_posicion_relativa(self, incremento:int, movimiento:int):
    self.posicion_relativa[1] = self.posicion_relativa[1] + incremento + movimiento
    self.posicion_relativa[0] = self.rect.x

  def __get_superficie(self, path, filas, columnas) -> list:
    lista = []
    superfice_imagen = pygame.image.load(path)
    fotograma_ancho = int(superfice_imagen.get_width()/columnas)
    fotograma_alto = int(superfice_imagen.get_height()/filas)
    for fila in range(filas):
      for columna in range(columnas ):
        x = columna * fotograma_ancho
        y = fila *  fotograma_alto
        #un pedazo de la superficie
        superficie_fotograma = superfice_imagen.subsurface(x,y,fotograma_ancho,fotograma_alto)
        lista.append(superficie_fotograma)
    return lista
  


        # Rebote en direcciones opuestas sin invertir el control del jugador
        #auto_cpu.rect *= -1
