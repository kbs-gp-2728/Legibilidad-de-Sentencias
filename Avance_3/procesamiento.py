"""Conteo de palabras y oraciones con spaCy y NLTK; sílabas aproximadas."""

import nltk
import spacy


def contar_con_spacy(texto):
    # El modelo se carga cuando se usa; así los otros módulos se pueden importar.
    try:
        nlp = spacy.load("es_core_news_sm")
    except OSError as exc:
        raise RuntimeError(
            "Falta el modelo español de spaCy. Ejecuta: python -m spacy download es_core_news_sm"
        ) from exc
    doc = nlp(texto)
    palabras = [token.text for token in doc if token.is_alpha]
    oraciones = list(doc.sents)
    return palabras, len(oraciones)


def contar_con_nltk(texto):
    try:
        oraciones = nltk.sent_tokenize(texto, language="spanish")
        tokens = nltk.word_tokenize(texto, language="spanish")
    except LookupError as exc:
        raise RuntimeError(
            "Faltan los datos punkt_tab de NLTK. Ejecuta: "
            "python -m nltk.downloader punkt_tab"
        ) from exc
    palabras = [token for token in tokens if token.isalpha()]
    return palabras, len(oraciones)


def contar_silabas(palabra):
    """Estimación básica por grupos vocálicos (no es silabificación exacta)."""
    vocales = "aeiouáéíóúü"
    fuertes = "aeoáéó"
    debiles_tildadas = "íú"
    palabra = palabra.lower()
    if palabra == "y":
        return 1
    total = 0
    anterior = ""
    for letra in palabra:
        if letra not in vocales:
            anterior = ""
            continue
        if (not anterior or
            (anterior in fuertes and letra in fuertes) or
            anterior in debiles_tildadas or
            letra in debiles_tildadas):
            total += 1
        anterior = letra
    return total
