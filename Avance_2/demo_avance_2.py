from legibilidad import calcular_legibilidad, clasificar_legibilidad

# Datos de ejemplo para demostrar la fórmula
palabras = 100
oraciones = 5
silabas = 200

# Calcular el índice
indice = calcular_legibilidad(palabras, oraciones, silabas)

# Clasificar el resultado
categoria = clasificar_legibilidad(indice)

print("ANÁLISIS DE LEGIBILIDAD - AVANCE 2")
print("--------------------------------")
print("Palabras:", palabras)
print("Oraciones:", oraciones)
print("Sílabas:", silabas)
print()
print("Índice Flesch-Szigriszt:", indice)
print("Clasificación INFLESZ:", categoria)
