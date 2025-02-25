import pygame
import sys
import re
import json
import csv

# Colores y constantes
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE  = (0, 0, 255)
GRAY  = (200, 200, 200)
WIDTH, HEIGHT = 800, 600

def exportar_json(ranking):
    """Exporta el ranking a un archivo JSON."""
    try:
        with open("ranking.json", "w", encoding="utf-8") as f:
            json.dump(ranking, f, indent=4, ensure_ascii=False)
        print("Ranking exportado a ranking.json")
    except Exception as e:
        print("Error exportando JSON:", e)

def exportar_csv(ranking):
    """Exporta el ranking a un archivo CSV."""
    try:
        with open("ranking.csv", "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["name", "time", "score"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for entry in ranking:
                writer.writerow(entry)
        print("Ranking exportado a ranking.csv")
    except Exception as e:
        print("Error exportando CSV:", e)

def mostrar_ranking(pantalla, ranking):
    clock = pygame.time.Clock()
    font_title = pygame.font.Font(None, 60)
    font = pygame.font.Font(None, 36)
    input_text = ""  # Texto ingresado en la barra de búsqueda
    
    # Definir áreas para la búsqueda y botones de exportación
    search_box = pygame.Rect(50, 100, 300, 40)
    btn_json = pygame.Rect(50, HEIGHT - 80, 150, 40)
    btn_csv  = pygame.Rect(220, HEIGHT - 80, 150, 40)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Captura de texto para la barra de búsqueda
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                elif event.key == pygame.K_RETURN:
                    # Puedes agregar una acción al presionar Enter si lo deseas
                    pass
                else:
                    input_text += event.unicode
            # Manejo de clicks para exportar
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = event.pos
                if btn_json.collidepoint(mouse_pos):
                    exportar_json(ranking)
                elif btn_csv.collidepoint(mouse_pos):
                    exportar_csv(ranking)
        
        # Fondo y título
        pantalla.fill(WHITE)
        titulo = font_title.render("Ranking", True, BLACK)
        pantalla.blit(titulo, (WIDTH // 2 - titulo.get_width() // 2, 20))
        
        # Dibujar la barra de búsqueda
        pygame.draw.rect(pantalla, GRAY, search_box)
        search_surface = font.render(input_text, True, BLACK)
        pantalla.blit(search_surface, (search_box.x + 5, search_box.y + 5))
        
        # Filtrar el ranking usando regex
        try:
            pattern = re.compile(input_text, re.IGNORECASE)
        except re.error:
            pattern = re.compile(".*")  # Muestra todo si hay error en la expresión
        ranking_filtrado = [entry for entry in ranking if pattern.search(entry["name"])]
        
        # Mostrar la lista filtrada en pantalla
        y_offset = 160
        for i, entry in enumerate(ranking_filtrado):
            texto = f"{i+1}. {entry['name']} - Tiempo: {entry['time']} - Puntaje: {entry['score']}"
            linea = font.render(texto, True, BLACK)
            pantalla.blit(linea, (50, y_offset))
            y_offset += 30
        
        # Dibujar botones de exportación
        pygame.draw.rect(pantalla, BLUE, btn_json)
        pygame.draw.rect(pantalla, BLUE, btn_csv)
        btn_json_text = font.render("Exportar JSON", True, WHITE)
        btn_csv_text  = font.render("Exportar CSV", True, WHITE)
        pantalla.blit(btn_json_text, (btn_json.x + 5, btn_json.y + 5))
        pantalla.blit(btn_csv_text, (btn_csv.x + 5, btn_csv.y + 5))
        
        pygame.display.flip()
        clock.tick(30)

def actualizar_ranking(pantalla):
    pass

# Ejemplo de datos de ranking (estos se agregarían cada vez que ganes una partida)
ranking_ejemplo = [
    {"name": "Jugador1", "time": "00:05:30", "score": 1000},
    {"name": "Florencia", "time": "00:04:45", "score": 1200},
    {"name": "Jriccardo", "time": "00:06:10", "score": 900},
]

if __name__ == "__main__":
    pygame.init()
    pantalla = pygame.display.set_mode((WIDTH, HEIGHT))
    mostrar_ranking(pantalla, ranking_ejemplo)
