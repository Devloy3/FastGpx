# 🚀FastGpx 

Es una pequeña libreria de phyton escrita en Rust y expuesta a Python mediante
[PyO3](https://github.com/PyO3/pyo3). 

Su objetivo es ofrecer un procesamiento de archivos GPX **rápido** y **fácil de usar** desde Python.

## Características 

- Lectura rápida de archivos GPX usando Rust. 
- Sin dependencias pesadas en Python. 
- Ideal para análisis de rutas, tracking GPS o aplicaciones deportivas.

## Como instalarlo?

1. Creamos un entorno de phyton

```
python3 -m venv .venv
source .venv/bin/activate
```
2. Instalamos la conectividad con la libreria

```
pip install maturin
```
3. Creamos el archivo compilado

```
maturin develop
```
## 🐍 Ejemplo de como utilizarlo en Phyton

```
import fast_gpx

points = fast_gpx.LoadGpx("ruta.gpx")
print(points[:5])
```

## 🤝 Ideas de Contribucion

- Añadir más funciones equivalentes a gpxpy (parseo de tracks, segments, elevación, tiempo, etc.)

- Mejorar el rendimiento del parser actual.

- Añadir validación de datos GPX.

- Implementar conversión a otros formatos (GeoJSON, CSV…).

- Añadir benchmarks comparando Rust vs gpxpy.

- Mejorar la documentación o los ejemplos de uso.

- Reportar bugs o proponer nuevas funcionalidades.