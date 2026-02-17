use pyo3::prelude::*;
use gpx::read;
use std::fs::File;
use std::io::BufReader;

// Esta es la función que Python verá
#[pyfunction]
fn leer_coordenadas(ruta_gpx: String) -> PyResult<Vec<(f64, f64)>> {
    // 1. Abrimos el archivo
    let file = File::open(ruta_gpx).map_err(|e| PyErr::new::<pyo3::exceptions::PyFileNotFoundError, _>(e.to_string()))?;
    let reader = BufReader::new(file);

    // 2. Procesamos el GPX
    let gpx_data = read(reader).map_err(|_| PyErr::new::<pyo3::exceptions::PyValueError, _>("El archivo GPX está corrupto"))?;
    
    let mut coords = Vec::new();

    for track in gpx_data.tracks {
        for segment in track.segments {
            for p in segment.points {
                coords.push((p.point().y(), p.point().x()));
            }
        }
    }

    Ok(coords)
}

// Aquí registramos el módulo para Python
#[pymodule]
fn fast_gpx(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(leer_coordenadas, m)?)?;
    Ok(())
}