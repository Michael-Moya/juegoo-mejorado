import pygame
from constantes import *
from fondo import *
from auto import * 
from auto_principal import *
from auto_cpu import *
from linea_meta import * 
reloj = pygame.time.Clock()
#Se crea una ventana
ventana = pygame.display.set_mode((ANCHO_VENTANA,ALTURA_VENTANA)) 
# elementos del juego
fondo = Fondo("carretera.png")     
auto_principal = AutoPrincipal()
auto_cpu = AutoCpu(POSICION_INICIAL_CPU)
# meta_inicio = Meta([0,0])
# meta_final = Meta([0,-3000])
# lista_lineas_meta = [meta_inicio, meta_final]

# reloj = pygame.time.Clock()


# def reiniciar_objetos():
#     global ventana, fondo, auto_principal, auto_cpu, meta_inicio, meta_final, lista_lineas_meta, avance, charcos, ranking_ejemplo, reloj, tiempo_inicio

#     ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTURA_VENTANA))
    
#     fondo = Fondo("carretera.png")
#     auto_principal = AutoPrincipal()
#     auto_cpu = AutoCpu(POSICION_INICIAL_CPU)
    
#     meta_inicio = Meta([0, 0])
#     meta_final = Meta([0, -3000])
#     lista_lineas_meta = [meta_inicio, meta_final]

#     # 🔥 Verificar si la posición de la meta es la correcta
#     print(f"Meta Final después de reiniciar: {meta_final.rect}")

#     # Asegurar que `Meta._ultima_meta` se actualiza correctamente
#     Meta._ultima_meta = meta_final  # <--- IMPORTANTE

#     avance = 0
#     charcos = []
    
#     ranking_ejemplo = [
#         {"name": "______", "time": "00:05:30", "score": 1000},
#     ]
    
#     reloj = pygame.time.Clock()
# instacia_objetos.py
meta_inicio = Meta([0, 0])
meta_final = Meta([0, -3000])
Meta._ultima_meta = meta_final  # ✅ ACTUALIZA `Meta._ultima_meta` correctamente
lista_lineas_meta = [meta_inicio, meta_final]

def reiniciar_objetos():
    global auto_principal, auto_cpu, fondo, meta_final, lista_lineas_meta, avance, charcos, ranking_ejemplo, reloj, tiempo_inicio

    ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTURA_VENTANA))
    
    fondo = Fondo("carretera.png")
    auto_principal = AutoPrincipal()
    auto_cpu = AutoCpu(POSICION_INICIAL_CPU)
    
    meta_inicio = Meta([0, 0])
    meta_final = Meta([0, -3000])
    Meta._ultima_meta = meta_final  # ✅ 🔥 IMPORTANTE: Mantener la referencia actualizada
    lista_lineas_meta = [meta_inicio, meta_final]

    avance = 0
    charcos = []

    ranking_ejemplo = [
        {"name": "______", "time": "00:05:30", "score": 1000},
    ]

    reloj = pygame.time.Clock()
