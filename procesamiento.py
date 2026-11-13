import re

# Texto de prueba de una sentencia judicial
texto = """ El tribunal examinó las pruebas presentadas por las partes.
La jueza determinó que la resolución debía estar debidamente motivada.
Finalmente, se notificó la sentencia a todas las personas involucradas.
"""

# Contar las palabras
palabras = re.findall(r"[a-záéíóúüñ]+", texto.lower())

# Identificar las oraciones
oraciones = re.split(r"[.!?]+", texto)
oraciones = [o.strip() for o in oraciones if o.strip()]

# Mostrar los resultados
print("ANÁLISIS DE TEXTO JUDICIAL")
print("Total de palabras:", len(palabras))
print("Total de oraciones:", len(oraciones))

# Contar las sílabas de cada palabra
def contar_silabas(palabra):
    vocales = "aeiouáéíóúü"
    fuertes = "aeoáéó"
    debiles_tildadas = "íú"

    total = 0
    anterior = ""

    for letra in palabra.lower():
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

# Calcular el total de sílabas
total_silabas = sum(contar_silabas(p) for p in palabras)

print("Total de sílabas:", total_silabas)

# Mostrar las sílabas por palabra
for palabra in palabras:
    print(palabra, ":", contar_silabas(palabra))


# Pruebas del conteo de sílabas
print("\nVALIDACIÓN DEL CONTEO DE SÍLABAS")

pruebas = {
    "tribunal": 3,
    "jueza": 2,
    "sentencia": 3,
    "resolución": 4,
    "país": 2,
    "río": 2
}

for palabra, esperado in pruebas.items():
    resultado = contar_silabas(palabra)

    if resultado == esperado:
        print(palabra, ":", resultado, "- CORRECTO")
    else:
        print(palabra, ":", resultado, "- ERROR")