import pygame
import random
from auto import *
class AutoCpu(Auto) :
  def __init__(self, posicion_inicial ) -> None:
    super().__init__("auto_amarillo.jpg")
    self.nombre = "Auto_CPU----------------------------------------------------------------"
    self.color_rect = WHITE
    self.rect.topleft = posicion_inicial #[600,400]
    #self.posicion_real_imagen = self.posicionar()
    self.posicionar()
    self.posicion_real = self.rect.topleft
    self.rect.width = 100
    self.rect.height = 200
    #Atributos para el movimiento automatico
    self.tiempo_cambio_direccion_automatico = random.randint(15, 40)
    self.frames_hasta_cambio_automatico = self.tiempo_cambio_direccion_automatico
    self.direccion_automatico = 1

  def mover(self, incremento_fondo:float):
    movimiento = 2
    variacion_movimiento = incremento_fondo - movimiento
    #print("variacion de movimiento",variacion_movimiento)
    self.rect.y += variacion_movimiento
    self.__direccionar_automatico()
    self.__avanzar_posicion_relativa(movimiento)
    #self.posicion_real_imagen = self.posicionar()
    self.posicionar()
    self.limitar_posicion_por_ventana()
  def __avanzar_posicion_relativa(self, movimiento:int):
    self.posicion_relativa[1] = self.posicion_relativa[1] + movimiento 
    self.posicion_relativa[0] = self.rect.x

  def __direccionar_automatico(self):
    self.frames_hasta_cambio_automatico -= 1
    if self.frames_hasta_cambio_automatico <= 0:
      self.direccion_automatico *= -1  # Cambiar la dirección
      #self.frames_hasta_cambio_automatico = self.tiempo_cambio_direccion_automatico  # Reiniciar el contador

      self.frames_hasta_cambio_automatico = random.randint(15, 60)
    # Mover el cuadrado automático
    self.rect.x += self.direccion_automatico * 5  

  def __get_superficie(self, path , filas, columnas) -> list:
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

