import pygame
from constantes import *
from colores import *
from auto import *
class Meta():
  _ultima_meta = 0# Estado compartido
  """class Meta:
    # Clase para rastrear el último objeto tocado
    _last_touched = None

    def __init__(self, name):
        self.name = name

    def touch(self):
        # Actualizar el objeto tocado más recientemente
        Meta._last_touched = self
        print(f"{self.name} ha sido tocado.")

    @classmethod
    def last_touched_action(cls):
        # Ejecutar acción en el último objeto tocado
        if cls._last_touched:
            print(f"Ejecutando acción en {cls._last_touched.name}.")
        else:
            print("No se ha tocado ningún objeto aún.") 
  """
  """
  class Meta:
    # Clase que rastrea la última meta creada
    _ultima_meta = None  # Estado compartido

    def __init__(self, name):
        self.name = name
        Meta._ultima_meta = self  # Actualizar la última meta creada

    @classmethod
    def es_ultima_meta(cls, other):
        "Verifica si el objeto es la última meta."
        return cls._ultima_meta is other

    @staticmethod
    def detectar_colision(objeto, meta):
        ""Detecta si el objeto colisiona con la última meta.""
        if Meta.es_ultima_meta(meta):
            print(f"¡Colisión detectada con la última meta: {meta.name}!")
            return True
        else:
            print(f"No es la última meta: {meta.name}.")
            return False
  """
  """
  class Ejemplo:
    def __init__(self):
        self._atributo = None

    @property
    def atributo(self):
        "Obtiene el valor del atributo."
        return self._atributo

    @atributo.setter
    def atributo(self, valor):
        "Establece el valor del atributo con validación."
        if valor == "Valor no permitido":
            raise ValueError("Este valor no es válido.")
        self._atributo = valor

    def metodo(self):
        "Modifica el valor del atributo de manera controlada."
        self._atributo = "Valor actualizado en el método"
  """
  def __init__(self,posicion) -> None:
    self.superficie = self.__crear_Meta("linea_de_meta.jpg")
    self.rect = self.superficie.get_rect()
    self.rect.topleft = posicion
    self.posicion_relativa = posicion
    Meta._ultima_meta = self
    
  def colisionar(self, auto: Auto):
    if self.rect.colliderect(auto.rect):
      self.ganador = auto
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
    #print(self.rect) es para el la posicion en x ,y ,ancho, alto
    #ancho, alto = self.superficie.get_size()
    #print(f"Ancho: {ancho}, Alto: {alto}")

    #pygame.draw.rect(pantalla, BROWN , self.rect)     

  def __crear_Meta(self,path):
    imagen_meta = pygame.image.load(path)
    imagen_meta = pygame.transform.scale(imagen_meta,(1000,200))
    return imagen_meta
  


 
     