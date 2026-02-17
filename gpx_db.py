import fast_gpx
import folium
import glob
import time
import random

def color_aleatorio():
    colores = ['red', 'blue', 'green', 'purple', 'orange', 'darkred', 'cadetblue', 'darkgreen']
    return random.choice(colores)

inicio_global = time.time()
archivos = glob.glob("./gpx/*.gpx")

mapa = folium.Map()
todos_los_puntos = []

print(f"🚀 Procesando {len(archivos)} rutas...")

for ruta in archivos:
    try:
        coordenadas = fast_gpx.leer_coordenadas(ruta)
        
        if coordenadas:
            # Añadimos la ruta con un color distinto cada vez
            folium.PolyLine(
                coordenadas, 
                weight=3, 
                color=color_aleatorio(), 
                opacity=0.8,
                tooltip=ruta
            ).add_to(mapa)
            
            # Guardamos todos los puntos para calcular el encuadre final
            todos_los_puntos.extend(coordenadas)
            print(f"✅ Añadida: {ruta}")
            
    except Exception as e:
        print(f"❌ Error en {ruta}: {e}")

# 2. El paso CRUCIAL: Ajustar el zoom para que se vean TODAS
if todos_los_puntos:
    # Esto busca el punto más al norte, sur, este y oeste de todas las rutas juntas
    mapa.fit_bounds([min(todos_los_puntos), max(todos_los_puntos)])
    
    print("🌍 Generando archivo HTML...")
    mapa.save("mis_rutas_strava.html")
    
    fin_global = time.time()
    print(f"\n✨ ¡TERMINADO! Tiempo total: {fin_global - inicio_global:.2f}s")
else:
    print("No se encontraron puntos para mostrar.")