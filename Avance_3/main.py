"""Ejecutar: python main.py datos/sentencia.txt  (o ruta a un PDF)."""

import argparse
from lectura import leer_archivo
from procesamiento import contar_con_spacy, contar_con_nltk, contar_silabas
from legibilidad import calcular_legibilidad, clasificar_legibilidad


def analizar(ruta):
    texto = leer_archivo(ruta)
    print("ANÁLISIS DE LEGIBILIDAD")
    print("Archivo:", ruta)
    for nombre, contar in (("spaCy", contar_con_spacy), ("NLTK", contar_con_nltk)):
        palabras, total_oraciones = contar(texto)
        total_silabas = sum(contar_silabas(p) for p in palabras)
        indice = calcular_legibilidad(len(palabras), total_oraciones, total_silabas)
        print("\nResultados con", nombre)
        print("Palabras:", len(palabras))
        print("Oraciones:", total_oraciones)
        print("Sílabas estimadas:", total_silabas)
        print("Índice Flesch-Szigriszt:", indice)
        print("Clasificación INFLESZ:", clasificar_legibilidad(indice))


def main():
    parser = argparse.ArgumentParser(description="Analizar texto judicial TXT o PDF")
    parser.add_argument("archivo", help="Ruta del TXT o PDF a analizar")
    args = parser.parse_args()
    try:
        analizar(args.archivo)
    except (OSError, ValueError, RuntimeError) as exc:
        parser.exit(1, f"Error: {exc}\n")


if __name__ == "__main__":
    main()
