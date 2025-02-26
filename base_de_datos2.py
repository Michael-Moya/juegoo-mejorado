import sqlite3

import sqlite3

with sqlite3.connect("ranking.db") as conexion:
    cursor = conexion.execute("SELECT * FROM ranking")
    filas = cursor.fetchall()
    print("📊 Datos en la tabla ranking:", filas)

# with sqlite3.connect("ranking.db") as conexion:
#     try:
#         conexion.execute("DROP TABLE IF EXISTS ranking")  # Eliminar tabla antigua
#         conexion.execute('''
#             CREATE TABLE ranking (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 nombre TEXT NOT NULL,
#                 tiempo TEXT NOT NULL
#             )
#         ''')
#         print("✅ Tabla 'ranking' actualizada sin la columna 'puntaje'.")
#     except sqlite3.Error as e:
#         print("⚠️ Error al actualizar la tabla:", e)

# with sqlite3.connect("ranking.db") as conexion:
#     cursor = conexion.execute("PRAGMA table_info(ranking)")
#     columnas = cursor.fetchall()
#     for columna in columnas:
#         print(columna)
        
# with sqlite3.connect("ranking.db") as conexion:
#     cursor = conexion.execute("SELECT * FROM ranking")
#     for fila in cursor:
#         print(fila)     

def crear_base_de_datos():
    """Crea la base de datos y la tabla ranking si no existen."""
    with sqlite3.connect("ranking.db") as conexion:
        try:
            conexion.execute('''
                CREATE TABLE IF NOT EXISTS ranking (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    tiempo TEXT NOT NULL
                 
                )
            ''')
            print("✅ Tabla 'ranking' verificada o creada correctamente.")
        except sqlite3.Error as e:
            print("⚠️ Error al crear la tabla:", e)

import sqlite3

def guardar_ranking_db(nombre, tiempo_formateado):
    """Guarda un nuevo tiempo en la base de datos."""
    with sqlite3.connect("ranking.db") as conexion:
        try:
            print(f"⏳ Intentando guardar en BD: {nombre} - {tiempo_formateado}")  # 🔥 Debugging

            conexion.execute("INSERT INTO ranking (nombre, tiempo) VALUES (?, ?)", 
                             (nombre, tiempo_formateado))
            conexion.commit()

            print(f"✅ Guardado en BD: {nombre} - {tiempo_formateado}")  # 🔥 Confirmación
        except sqlite3.Error as e:
            print("⚠️ Error al guardar en ranking:", e)

def obtener_top_5():
    """Obtiene los 5 mejores tiempos del ranking (ordenados correctamente)."""
    with sqlite3.connect("ranking.db") as conexion:
        try:
            # 🟢 Convertimos el formato de tiempo HH:MM:SS:MS en orden numérico
            cursor = conexion.execute("""
                SELECT nombre, tiempo 
                FROM ranking 
                ORDER BY 
                    CAST(SUBSTR(tiempo, 1, 2) AS INTEGER) ASC,  -- HH
                    CAST(SUBSTR(tiempo, 4, 2) AS INTEGER) ASC,  -- MM
                    CAST(SUBSTR(tiempo, 7, 2) AS INTEGER) ASC,  -- SS
                    CAST(SUBSTR(tiempo, 10, 3) AS INTEGER) ASC  -- MS
                LIMIT 5
            """)
            ranking = cursor.fetchall()
            return ranking
        except sqlite3.Error as e:
            print("⚠️ Error al obtener el ranking:", e)
            return []

def actualizar_nombre(id_jugador, nuevo_nombre):
    """Actualiza el nombre de un jugador en el ranking."""
    with sqlite3.connect("ranking.db") as conexion:
        try:
            cursor = conexion.execute("UPDATE ranking SET nombre = ? WHERE id = ?", (nuevo_nombre, id_jugador))
            conexion.commit()
            if cursor.rowcount > 0:
                print(f"✅ Nombre actualizado a {nuevo_nombre} para el ID {id_jugador}")
            else:
                print("⚠️ No se encontró el ID en el ranking.")
        except sqlite3.Error as e:
            print("⚠️ Error al actualizar nombre:", e)


def eliminar_jugador(id_jugador):
    """Elimina un jugador del ranking por ID."""
    with sqlite3.connect("ranking.db") as conexion:
        try:
            cursor = conexion.execute("DELETE FROM ranking WHERE id = ?", (id_jugador,))
            conexion.commit()
            if cursor.rowcount > 0:
                print(f"✅ Jugador con ID {id_jugador} eliminado.")
            else:
                print("⚠️ No se encontró el ID en el ranking.")
        except sqlite3.Error as e:
            print("⚠️ Error al eliminar jugador:", e)

# def eliminar_ranking():
#     """Elimina todos los registros del ranking al cerrar el juego."""
#     with sqlite3.connect("ranking.db") as conexion:
#         try:
#             conexion.execute("DELETE FROM ranking")
#             conexion.commit()
#             print("🗑️ Ranking eliminado al cerrar el juego.")
#         except sqlite3.Error as e:
#             print("⚠️ Error al eliminar el ranking:", e)



