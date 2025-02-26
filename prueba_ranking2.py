import pygame
import sys
import re
import json
import csv
import constantes
import os

# Colores y constantes
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE  = (0, 0, 255)
GRAY  = (200, 200, 200)
WIDTH, HEIGHT = 800, 600

def exportar_json():
    """Exporta el ranking a un archivo JSON solo si el usuario lo solicita."""
    try:
        with open("ranking.json", "w", encoding="utf-8") as f:
            json.dump(constantes.ranking, f, indent=4, ensure_ascii=False)
        print("✅ Ranking exportado a ranking.json")
    except Exception as e:
        print("❌ Error exportando JSON:", e)

def exportar_csv():
    """Exporta el ranking a un archivo CSV solo si el usuario lo solicita."""
    try:
        with open("ranking.csv", "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["name", "time"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for entry in constantes.ranking:
                writer.writerow(entry)
        print("✅ Ranking exportado a ranking.csv")
    except Exception as e:
        print("❌ Error exportando CSV:", e)

def mostrar_ranking(pantalla, ranking):
    clock = pygame.time.Clock()
    font_title = pygame.font.Font(None, 60)
    font = pygame.font.Font(None, 36)
    input_text = ""

    search_box = pygame.Rect(50, 100, 300, 40)
    btn_json = pygame.Rect(50, HEIGHT - 80, 150, 40)
    btn_csv  = pygame.Rect(220, HEIGHT - 80, 150, 40)
    btn_menu = pygame.Rect(WIDTH - 200, HEIGHT - 80, 150, 40)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                elif event.key == pygame.K_RETURN:
                    pass
                else:
                    input_text += event.unicode
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = event.pos
                if btn_json.collidepoint(mouse_pos):
                    exportar_json()  # 🔥 Solo exporta si se presiona el botón
                elif btn_csv.collidepoint(mouse_pos):
                    exportar_csv()  # 🔥 Solo exporta si se presiona el botón
                elif btn_menu.collidepoint(mouse_pos):
                    return  

        pantalla.fill(WHITE)
        titulo = font_title.render("Ranking", True, BLACK)
        pantalla.blit(titulo, (WIDTH // 2 - titulo.get_width() // 2, 20))

        pygame.draw.rect(pantalla, GRAY, search_box)
        search_surface = font.render(input_text, True, BLACK)
        pantalla.blit(search_surface, (search_box.x + 5, search_box.y + 5))

        try:
            pattern = re.compile(input_text, re.IGNORECASE)
        except re.error:
            pattern = re.compile(".*")
        ranking_filtrado = [entry for entry in ranking if pattern.search(entry["name"])]

        y_offset = 160
        for i, entry in enumerate(ranking_filtrado):
            texto = f"{i+1}. {entry['name']} - Tiempo: {entry['time']}"
            linea = font.render(texto, True, BLACK)
            pantalla.blit(linea, (50, y_offset))
            y_offset += 30

        pygame.draw.rect(pantalla, BLUE, btn_json)
        pygame.draw.rect(pantalla, BLUE, btn_csv)
        pygame.draw.rect(pantalla, BLUE, btn_menu)

        btn_json_text = font.render("Exportar JSON", True, WHITE)
        btn_csv_text  = font.render("Exportar CSV", True, WHITE)
        btn_menu_text = font.render("Menú", True, WHITE)

        pantalla.blit(btn_json_text, (btn_json.x + 5, btn_json.y + 5))
        pantalla.blit(btn_csv_text, (btn_csv.x + 5, btn_csv.y + 5))
        pantalla.blit(btn_menu_text, (btn_menu.x + 45, btn_menu.y + 5))

        pygame.display.flip()
        clock.tick(30)

# def actualizar_ranking(nombre, tiempo_total ):
#     """Agrega un nuevo tiempo al ranking si está dentro del top 5."""
    
#     tiempo_formateado = f"{tiempo_total // 60000:02}:{(tiempo_total // 1000) % 60:02}:{tiempo_total % 1000:03}"
#     nuevo_registro = {"name": nombre, "time": tiempo_formateado, "score": tiempo_total}

#     # Evitar duplicados
#     if nuevo_registro in constantes.ranking:
#         print("⚠️ Tiempo duplicado, no se agregará al ranking.")
#         return
    
#     constantes.ranking.append(nuevo_registro)
#     constantes.ranking = sorted(constantes.ranking, key=lambda x: x["score"])  # Ordenar por menor tiempo

#     if len(constantes.ranking) > 5:
#         constantes.ranking.pop()  # Mantener solo los 5 mejores tiempos


#     print("\n🏆 Ranking Actualizado:")
#     for i, entry in enumerate(constantes.ranking):
#         print(f"{i+1}. {entry['name']} - {entry['time']}")


# def guardar_ranking(vaciar=False):
#     """Guarda o elimina el ranking según `vaciar`:
    
#     - Si `vaciar=True`, borra la lista `ranking` y elimina `ranking.json` y `ranking.csv`.
#     - Si `vaciar=False`, guarda los datos en JSON y CSV solo si hay información.
#     """
#     """Guarda un nuevo puntaje en la base de datos."""
#     if vaciar:
#         constantes.ranking = []  # 🔥 Vaciar la lista antes de cerrar el juego
#         print("⚠️ Ranking vaciado.")

#         # 🗑️ Eliminar archivos si existen
#         if os.path.exists("ranking.json"):
#             os.remove("ranking.json")
#             print("🗑️ Archivo ranking.json eliminado.")

#         if os.path.exists("ranking.csv"):
#             os.remove("ranking.csv")
#             print("🗑️ Archivo ranking.csv eliminado.")
#         return  # 🔥 Salir de la función para no guardar nada más

#     # 🔥 Solo guardar si hay datos en el ranking
#     if constantes.ranking:
#         try:
#             with open("ranking.json", "w", encoding="utf-8") as f:
#                 json.dump(constantes.ranking, f, indent=4, ensure_ascii=False)
#             print("✅ Ranking guardado en ranking.json")
#         except Exception as e:
#             print("❌ Error guardando JSON:", e)

#         try:
#             with open("ranking.csv", "w", newline="", encoding="utf-8") as csvfile:
#                 fieldnames = ["name", "time", "score"]
#                 writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#                 writer.writeheader()
#                 for entry in constantes.ranking:
#                     writer.writerow(entry)
#             print("✅ Ranking guardado en ranking.csv")
#         except Exception as e:
#             print("❌ Error guardando CSV:", e)
#     else:
#         print("⚠️ No se guardó el ranking porque está vacío.")

# def cargar_ranking():
#     """Carga el ranking desde un archivo JSON al iniciar el juego."""
#     try:
#         with open("ranking.json", "r", encoding="utf-8") as f:
#             constantes.ranking = json.load(f)
#         print("✅ Ranking cargado desde ranking.json")
#     except FileNotFoundError:
#         constantes.ranking = []  # Si no hay archivo, iniciamos con una lista vacía
#         print("⚠️ No se encontró ranking.json, se inicia con un ranking vacío.")
#     except Exception as e:
#         print("❌ Error cargando ranking:", e)
#         constantes.ranking = []  # En caso de error, iniciamos con una lista vacía
