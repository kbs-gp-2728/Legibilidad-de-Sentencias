# Avance 1 — Procesamiento lingüístico

## Objetivo

Implementar un módulo inicial en Python para identificar palabras, separar oraciones y estimar el número de sílabas de textos en español.

## Actividades realizadas

1. Identificación y conteo de palabras con expresiones regulares.
2. Separación de oraciones mediante signos de puntuación.
3. Implementación de una función propia para estimar sílabas.
4. Prueba de seis palabras con valores esperados de sílabas.
5. Presentación de conteos globales y por palabra en la terminal.

## Funcionamiento

El programa se encuentra en `procesamiento.py`. Para ejecutarlo desde esta carpeta:

```powershell
python procesamiento.py
```

## Resultados

El módulo ejecuta conteos de palabras, oraciones y sílabas estimadas sobre el texto incluido en el programa. También informa si las seis pruebas coinciden con los valores esperados. La estimación silábica es preliminar y puede fallar con ciertas combinaciones del español.

El código fue publicado originalmente en el commit `8d48536` del repositorio del grupo. En esta carpeta se conserva esa versión con los caracteres acentuados reparados para su lectura.
