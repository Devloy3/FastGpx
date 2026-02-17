import fast_gpx  # Tu nueva librería de Rust
import folium
import time
import glob
# 1. Medimos el tiempo para que flipes con la diferencia
inicio = time.time()

print("🚀 Rust está procesando el GPX...")
for archivos in glob.glob("./gpx/*.gpx"):
    coordenadas = fast_gpx.leer_coordenadas("tu_archivo_pesado.gpx")

    fin = time.time()
    print(f"✅ ¡BRUTAL! Procesados {len(coordenadas)} puntos en {fin - inicio:.4f} segundos.")

# 2. Crear el mapa (esto es lo único que hace Python)
    if coordenadas:
        print("🌍 Dibujando el mapa...")
        mapa = folium.Map(location=coordenadas[0], zoom_start=13)
        folium.PolyLine(coordenadas, color="blue", weight=2.5, opacity=1).add_to(mapa)
    
    mapa.save("mapa_super_rapido.html")
    print("✨ Mapa listo en 'mapa_super_rapido.html'. ¡Ábrelo!")