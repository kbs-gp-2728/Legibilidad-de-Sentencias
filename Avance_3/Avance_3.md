# Avance 3 — Lectura de TXT/PDF y comparación de librerías

## Objetivo

Leer textos en formatos TXT y PDF y comparar los conteos de palabras y oraciones mediante spaCy y NLTK, utilizando la estimación de sílabas y el índice Flesch-Szigriszt.

## Actividades realizadas

1. Se implementó la lectura de archivos TXT y extracción de texto de PDF con PyMuPDF.
2. Se compararon los conteos de palabras y oraciones con spaCy y NLTK.
3. Se integró la estimación silábica propia.
4. Se calcularon el índice Flesch-Szigriszt y la clasificación INFLESZ.
5. Se identificó un caso de segmentación que separa incorrectamente la abreviatura jurídica `Art. 76`.

## Funcionamiento

Los programas están en esta carpeta: `lectura.py` para lectura, `procesamiento.py` para análisis lingüístico, `legibilidad.py` para el índice y `main.py` para integrar la ejecución.

Instalación de las librerías y modelos (desde `Avance_3`):

```powershell
python -m pip install -r requirements.txt
python -m spacy download es_core_news_sm
python -c "import nltk; nltk.download('punkt_tab')"
```

Para ejecutar con un archivo de texto o PDF siempre y cuando este autorizado para analizar:

```powershell
python main.py datos/sentencia.txt
python main.py datos/sentencia.pdf
```
## Carpeta de Datos

Se utilizó la carpeta datos para almacenar los documentos empleados en las pruebas de lectura y procesamiento de texto.

Dentro de esta carpeta se encuentra el archivo LEEME.txt, que contiene indicaciones sobre la ubicación de los documentos utilizados para el análisis y la verificación de su publicación.
Se trabajó con 2 formatos:
- TXT: permite leer directamente el contenido del documento mediante Python.
- PDF: requiere extraer el texto utilizando la librería PyMuPDF.

El programa main.py recibe la ruta del documento, utiliza lectura.py para obtener su contenido y posteriormente procesa el texto mediante spaCy y NLTK para calcular los indicadores de legibilidad.
Durante las pruebas se utilizaron los archivos sentencia.txt y sentencia.pdf, que se conservaron localmente y no se incluyeron en el repositorio de GitHub.

## Resultados  

Se ejecutó el programa main.py utilizando el archivo PDF de prueba datos/sentencia.pdf.

Los resultados obtenidos fueron los siguientes:
| Indicador | spaCy | NLTK |
|---|---:|---:|
| Palabras | 126 | 126 |
| Oraciones | 8 | 8 |
| Sílabas estimadas | 273 | 273 |
| Índice Flesch-Szigriszt | 56,10 | 56,10 |
| Clasificación INFLESZ | Normal | Normal |

En esta prueba, spaCy y NLTK produjeron los mismos resultados.

Además, se ejecutaron los archivos test_lectura.py y test_legibilidad.py, con 4 pruebas automáticas correctas cada uno, para un total de 8 pruebas superadas.

Los documentos utilizados en la demostración se conservan localmente y no se incluyen en el repositorio de GitHub.
