import sqlite3

# Crear base SQLite con SpatiaLite
conn = sqlite3.connect("./rutas.db")
conn.enable_load_extension(True)
conn.load_extension("mod_spatialite")

cur = conn.cursor()

cur.execute("SELECT InitSpatialMetadata(1);")
cur.execute("""
    CREATE TABLE rutas(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Nombre TEXT,
        DistanciaTotal REAL,
        TiempoTotal TEXT,
        ElevacionTotal REAL
    );
""")

# Crear columna geom si no existe
cur.execute("SELECT AddGeometryColumn('rutas', 'geom', 4326, 'LINESTRINGZ', 'XYZ');")

conn.commit()
conn.close()