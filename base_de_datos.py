import sqlite3

with sqlite3.connect("ranking.db") as conexion:
    try:
        sentencia = '''CREATE TABLE ranking (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            tiempo TEXT NOT NULL,
            puntaje INTEGER NOT NULL
        )'''
        conexion.execute(sentencia)
        print("🆕 Se creó la tabla ranking")                       
    except sqlite3.OperationalError:
        print("✅ La tabla ranking ya existe")

def guardar_ranking_db(nombre, tiempo_formateado, puntaje):
    """Guarda un nuevo puntaje en la base de datos."""
    with sqlite3.connect("ranking.db") as conexion:
        try:
            conexion.execute("INSERT INTO ranking(nombre, tiempo, puntaje) VALUES (?, ?, ?)", 
                             (nombre, tiempo_formateado, puntaje))
            conexion.commit()
            print(f"✅ Se guardó en el ranking: {nombre} - {tiempo_formateado}")
        except Exception as e:
            print("⚠️ Error al guardar en ranking:", e)

def obtener_top_5():
    """Obtiene los 5 mejores tiempos del ranking."""
    with sqlite3.connect("ranking.db") as conexion:
        cursor = conexion.execute("SELECT nombre, tiempo, puntaje FROM ranking ORDER BY puntaje ASC LIMIT 5")
        ranking = cursor.fetchall()  # Devuelve una lista de los 5 mejores

    return ranking
