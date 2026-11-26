"""Lectura de sentencias en formato TXT y PDF con PyMuPDF."""

from pathlib import Path
import pymupdf


def leer_txt(ruta):
    return Path(ruta).read_text(encoding="utf-8-sig")


def leer_pdf(ruta):
    with pymupdf.open(ruta) as pdf:
        texto = "\n".join(pagina.get_text() for pagina in pdf)
    if not texto.strip():
        raise ValueError(
            "El PDF no contiene texto extraíble. Puede ser escaneado y requerir OCR."
        )
    return texto


def leer_archivo(ruta):
    ruta = Path(ruta)
    if not ruta.is_file():
        raise FileNotFoundError(f"No se encontró el archivo: {ruta}")
    if ruta.suffix.lower() == ".pdf":
        texto = leer_pdf(ruta)
    elif ruta.suffix.lower() == ".txt":
        texto = leer_txt(ruta)
    else:
        raise ValueError("Formato no compatible. Utiliza un archivo .txt o .pdf")
    if not texto.strip():
        raise ValueError("El archivo no contiene texto para analizar")
    return " ".join(texto.split())
