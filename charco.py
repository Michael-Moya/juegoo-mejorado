import pygame
import random
from constantes import *
from auto import *
class Charco() :
  def __init__(self , speed) -> None:
    self.superficie = self.__crear_charco("charco.png")
    self.rect = self.superficie.get_rect()
    
    self.posicion = self.__posicionar()
    self.rect.width = 100
    self.rect.height = 100
    self.visible = True
    self.color_rect = COLOR_RECT_CHARCO

  def mover(self,velocidad):
    if self.rect != None:
      self.posicionar()
      self.rect.y = self.rect.y + velocidad
      self.posicion[1] = self.posicion[1] + velocidad

  def posicionar(self):
      self.rect.x = self.posicion[0]+50
      self.rect.y = self.posicion[1]+50

  def mover_desacelerado(self,avance):
    if avance < 0.3:
      return False
    else:
      self.mover(avance)
      return True
  
  def colisionar(self , auto ):
    flag = False
    if  auto.rect.colliderect(self.rect) :
      self.visible = False
      flag = True
    return flag
#considerar a eliminar
  def update_mover_charco(self, velocidad, movimiento = True):
    if movimiento:
      self.mover(velocidad)
    else:
      self.mover_desacelerado(velocidad)

  def __crear_charco(self,path):
    imagen_charco = pygame.image.load(path)
    imagen_charco = pygame.transform.scale(imagen_charco,(200,200))
    return imagen_charco
  def __posicionar(self):
    y = random.randrange(-900,-10,60)
    x = random.randrange(80,720,60)   
    return [x,y]

  def dibujar(self, pantalla):
    if self.visible:
      pantalla.blit(self.superficie,self.posicion)
      pygame.draw.rect(pantalla, self.color_rect, self.rect)     

  def limitar_posicion_por_ventana(self):
    if self.rect.left < 0 :
      self.rect.x = 0
    elif self.rect.right > ANCHO_VENTANA:
      self.rect.right = ANCHO_VENTANA  
      
  
  
    