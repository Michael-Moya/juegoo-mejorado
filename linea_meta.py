import pygame
from constantes import *
from colores import *
from auto import *
class Meta():
  def __init__(self,posicion) -> None:
    self.superficie = self.__crear_Meta("linea_de_meta.jpg")
    self.rect = self.superficie.get_rect()
    self.rect.topleft = posicion
    self.posicion_relativa = posicion

  def colisionar(self, auto: Auto):
    if self.rect.colliderect(auto.rect):
      return True
    return False
  
  def mover(self, incremento):
    self.rect.y = self.rect.y + incremento

  def verificar_eliminar(self):
    if self.rect.top > ALTURA_VENTANA:
      return True
    return False
  
  def dibujar(self, pantalla):
    pantalla.blit(self.superficie, self.rect)
    #pygame.draw.rect(pantalla, BROWN , self.rect)     

  def __crear_Meta(self,path):
    imagen_meta = pygame.image.load(path)
    imagen_meta = pygame.transform.scale(imagen_meta,(1000,200))
    return imagen_meta
  
     