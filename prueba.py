import pygame, sys, os
#from constantes import  flag_ganador, ganador_auto_principal, tiempo_inicio
from instacia_objetos import *
from nivel import seleccionar_nivel
from prueba_temporizador import iniciar_temporizador_carrera
from prueba12_menu import mostrar_menu
from prueba_ranking import mostrar_ranking
from funciones import *
from prueba_ventana_resultado import mostrar_pantalla_resultado
from prueba_ingresar_nombre import ingresar_nombre
import constantes

def reiniciar_juego(nivel_seleccionado):
    """Reinicia los objetos y variables del juego sin volver al menú."""
    global auto_principal, auto_cpu, fondo, meta_final, lista_lineas_meta, charcos
    global  tiempo_inicio

    # 🔥 Limpiar listas para evitar acumulación de memoria
    lista_lineas_meta.clear()
    charcos.clear()

    # 🔄 Crear nuevas instancias de los objetos
    auto_principal = AutoPrincipal()
    auto_cpu = AutoCpu(POSICION_INICIAL_CPU)
    fondo = Fondo("carretera.png")

    meta_inicio = Meta([0, 0])
    meta_final = Meta([0, -3000])
    lista_lineas_meta.extend([meta_inicio, meta_final])

    charcos = generar_charcos_por_nivel(nivel_seleccionado)

    constantes.flag_ganador = False
    constantes.ganador_auto_principal = False
    constantes.temporizador_iniciado = False
    tiempo_inicio = None  # 🔥 Asegurar que el temporizador se reinicia correctamente
    print(f"🚀 flag_ganador REINICIADO a {constantes.flag_ganador} en reiniciar_juego()")
    # flag_ganador = False
    # ganador_auto_principal = False
    # tiempo_inicio = None  # 🔥 Asegurar que el temporizador se reinicia correctamente
    # # 🔄 Reiniciar variables de estado
    print(f"🔄 Reinicio: flag_ganador = {constantes.flag_ganador}, ganador_auto_principal = {constantes.ganador_auto_principal}")


def jugar():
    global  charcos, tiempo_inicio
    accion = None
    avance = 0

    seleccionado, nivel_seleccionado = seleccionar_nivel(ventana)
    auto_principal.nombre = ingresar_nombre(ventana)
    while True:  # 🔄 Este bucle permite reiniciar el juego sin volver al menú
        print(f"🔄 Reiniciando juego, flag_ganador antes de reset: {constantes.flag_ganador}")
        reiniciar_juego(nivel_seleccionado)  # 🔥 Reiniciar el juego
        print(f"✅ flag_ganador después de reset: {constantes.flag_ganador}")

        iniciar_temporizador_carrera(ventana)

        auto_principal.iniciar_tiempo_carrera()  # 🔥 Ahora el tiempo del auto comienza correctamente
        print("⏱️ Tiempo de carrera iniciado después del temporizador.")
        while cerrar_ventana():
            lista_meta = filtrar_linea_meta(lista_lineas_meta)

            avance, charcos, lista_meta, flag_ganador_, ganador_auto_principal_ = iniciar_movimiento_juego(
                ventana, fondo, auto_principal, avance, auto_cpu, charcos, lista_meta
            )
            #print(f"flag_ganador dentro de jugar(): {flag_ganador}")
            fundir_todo(ventana, fondo, auto_principal, auto_cpu, charcos, lista_meta)
            if flag_ganador_:
                
                if tiempo_inicio is None:  # ✅ SOLO asignamos el tiempo la primera vez
                    tiempo_inicio = pygame.time.get_ticks()
                    tiempo_total = auto_principal.obtener_tiempo_transcurrido()
                    tiempo_formateado = f"{tiempo_total // 60000:02}:{(tiempo_total // 1000) % 60:02}:{tiempo_total % 1000:03}"
                    print("tiempototal--------------------------------",tiempo_total)
                    #print(f"⏳ Nuevo tiempo_inicio asignado: {tiempo_inicio}")

            if constantes.flag_ganador and tiempo_inicio is not None and pygame.time.get_ticks() - tiempo_inicio >= 1000:
                print(f"⚠️ SE MUESTRA LA PANTALLA DE RESULTADOS | GANADOR: {constantes.ganador_auto_principal}")
                accion = mostrar_pantalla_resultado(ventana, constantes.ganador_auto_principal, tiempo_formateado)
      
                break

            pygame.display.flip()
            reloj.tick(FPS)

        if accion == "menu":
            break  
        elif accion == "volver_jugar":
            print("🔄 VOLVER A JUGAR")  
            continue  

    return accion

def main():
    """Bucle principal del juego."""
    while True:
        opcion_menu = mostrar_menu(ventana)

        if opcion_menu == "jugar":
            accion = jugar()
            if accion == "menu":
                continue  
        elif opcion_menu == "ranking":
            mostrar_ranking(ventana, ranking_ejemplo)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    os.system('cls')  
    pygame.init()
    pygame.display.set_caption("Racing")
    main()
