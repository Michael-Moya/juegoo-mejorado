import pygame
from constantes import *
from fondo import *
from auto import * 
from auto_principal import *
from auto_cpu import *
from charco import *
from linea_meta import *
#from constantes import flag_ganador, ganador_auto_principal
import constantes
import sys
x_presionada = False
x_presionada_previamente = False


def iniciar_movimiento_juego(ventana_, fondo_, auto_: AutoPrincipal, avance_, auto_cpu:AutoCpu, list_charcos:list, lista_meta:list ):
  global x_presionada_previamente
  global x_presionada
  meta_final = Meta._ultima_meta
  ganador_auto_principal = constantes.ganador_auto_principal
  avance_ = round(generar_movimiento_juego(ventana_, fondo_, auto_, avance_))
  if (x_presionada == False and x_presionada_previamente == True) or auto_.is_stabilizing:
    avance_ = disminuir_movimiento_juego(ventana_, fondo_, auto_, avance_)

  
  generar_movimiento_charcos(list_charcos, avance_)
  generar_movimiento_cpu(auto_cpu, avance_)

  list_charcos = revisar_colisiones_entre_autos(auto_, auto_cpu, list_charcos)
  controlar_desestabilizacion_autos(auto_, auto_cpu)

  generar_movimiento_metas(lista_meta,avance_)
  if not constantes.flag_ganador and definir_ganador(meta_final,[auto_,auto_cpu]):
    print("-------------------el auto gano =  ",constantes.ganador_auto_principal)
    constantes.flag_ganador = True
    print(f"🚀 flag_ganador CAMBIADO A {constantes.flag_ganador} en iniciar_movimiento_juego()")

    #mostrar_pantalla_resultado(ventana_, ganador_auto_principal,  ranking_ejemplo)
  return (avance_, list_charcos, lista_meta, constantes.flag_ganador , constantes.ganador_auto_principal)

def definir_ganador(meta_final, lista_auto:list ):
    flag = False
    for auto in lista_auto:
        if isinstance(meta_final, Meta) and meta_final.colisionar(auto):
            flag = True
            if isinstance(auto, AutoPrincipal):
                constantes.ganador_auto_principal = True
                print("✅ Auto Principal ha ganado la carrera (definir_ganador)")
            else:
                constantes.ganador_auto_principal = False
                print("❌ Auto CPU ha ganado la carrera (definir_ganador)")

            print(f"🚀 definir_ganador() -> ganador_auto_principal={constantes.ganador_auto_principal}")
            break

    return flag

def generar_movimiento_metas(lista_meta_:list,avance_):
  for meta in lista_meta_:
    if isinstance(meta, Meta):
      meta.mover(avance_)

def filtrar_linea_meta(lista_meta:list):#EN REALIDAD SERIA ELIMINAR LINEA DE META , PERO SOLO QUEDARIA 1
  lista_meta_ = list(filter( lambda x: (x.rect.y < ALTURA_VENTANA), lista_meta ))    
  return lista_meta_  

def generar_charcos(cantidad:int):
  list_charcos = []
  for i in range(cantidad):  # Usamos un guion bajo porque no necesitamos el valor de 'i'
    charco = Charco()  # Creamos una instancia de Charco
    list_charcos.append(charco)  # Añadimos la instancia a la lista
  return list_charcos

def generar_charcos_por_nivel(nivel:int):
  cantidad = 0
  match nivel:
    case 1:
      cantidad = 3
    case 2:
      cantidad = 8
    case _:
      print("Nivel desconocido")  # Caso """
  return generar_charcos(cantidad)
  
def controlar_desestabilizacion_autos(auto_: AutoPrincipal, auto_cpu: AutoCpu):
  auto_.controlar_la_desestabilización()
  auto_cpu.controlar_la_desestabilización()

def revisar_colisiones_entre_autos(auto_:AutoPrincipal, auto_cpu:AutoCpu, list_charcos:list):
  colisionar_entre_autos(auto_, auto_cpu)
  #Maneja excepciones con try-except si existe la posibilidad de que el elemento no esté presente.
  lista_eliminar = []
  for charco in list_charcos:  
    if charco.colisionar(auto_):
      auto_.administrar_colision()
      lista_eliminar.append(charco)
      print("COLISION AUTO")
    elif charco.colisionar(auto_cpu):
      auto_cpu.administrar_colision()
      lista_eliminar.append(charco)
      print("COLISION AUTO CPU ----")

    if charco.rect.top > ALTURA_VENTANA:
      lista_eliminar.append(charco)
  list_charcos_ = list(filter(lambda x: x not in lista_eliminar, list_charcos))
  return list_charcos_

def generar_movimiento_charcos(list_charcos , incremento:int):
  list_charcos_filtradas = list(filter(lambda x: isinstance(x, Charco), list_charcos))
  for charco in list_charcos_filtradas:
    charco.mover(incremento)
  
def generar_movimiento_juego(ventana_, fondo_:Fondo ,auto_:AutoPrincipal ,avance_) ->float:
  global x_presionada 
  global x_presionada_previamente
  lista_key = pygame.key.get_pressed()
  if lista_key[pygame.K_x] and auto_.is_stabilizing == False:
    avance_ = MOV_FONDO
    fondo_.movimiento(ventana_, avance_ )    
    auto_.mover(avance_)
    if not x_presionada:
      constantes.sonido_aceleracion.play()  #Reproducir sonido solo si es la primera vez que se presiona X
    x_presionada = True
    x_presionada_previamente = True
  else:
    if x_presionada:
      constantes.sonido_aceleracion.stop()
    x_presionada = False
  return avance_
#check
def disminuir_movimiento_juego(ventana_, carril_: Fondo, auto_:AutoPrincipal, avance_):
  if (avance_ < 2):
    avance_ = 0
  avance_ = round(avance_*(1 - 0.4))  
  carril_.movimiento(ventana_, avance_)
  auto_.mover(avance_)
  return avance_
#--------funciones de cpu-----------
def generar_movimiento_cpu(auto_cpu:AutoCpu , incremento_fondo):
  auto_cpu.mover(incremento_fondo)

def dibujar_cpu(ventana_, auto_cpu:AutoCpu):
  auto_cpu.dibujar(ventana_)

def colisionar_entre_autos(auto_:AutoPrincipal, auto_cpu:AutoCpu):
  if auto_.rect.colliderect(auto_cpu.rect):
    if (auto_.rect.x < auto_cpu.rect.x + ANCHO_RECT_AUTO and
      auto_.rect.x + ANCHO_RECT_AUTO > auto_cpu.rect.x and
      auto_.rect.y < auto_cpu.rect.y + ALTURA_RECT_AUTO and
      auto_.rect.y + ALTURA_RECT_AUTO > auto_cpu.rect.y):
      # Separar los  ligeramente
      if auto_.rect.x < auto_cpu.rect.x:
        auto_.rect.x = auto_cpu.rect.x - ANCHO_RECT_AUTO   # Mover el auto a la izquierda
      else:
        auto_.rect.x = auto_cpu.rect.x + ANCHO_RECT_AUTO  # Mover el auto a la derecha
    #si ya movi el rect de cada auto tambien tengo reposicionar la imagen 
    # porque si no, se separan los rect y la imagen
    #auto_.posicion_real_imagen = auto_.posicionar()
    #auto_cpu.posicion_real = auto_cpu.posicionar()
    auto_.posicionar()
    auto_cpu.posicionar()
#-----------------------------------
#-------------check-----------------
def fundir_todo(ventana_, fondo_:Fondo , auto:AutoPrincipal , auto_cpu:AutoCpu, list_charcos:list, lista_meta):
  ventana_.blit(fondo_.imagen, fondo_.posicion)
  for meta in lista_meta:
    if isinstance(meta, Meta):
      meta.dibujar(ventana_)

  auto.dibujar(ventana_)
  dibujar_cpu(ventana_, auto_cpu)
  for charco in list_charcos:
    charco.dibujar(ventana_)
#------------------------------------

#------------------------------------
def cerrar_ventana():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
    return True