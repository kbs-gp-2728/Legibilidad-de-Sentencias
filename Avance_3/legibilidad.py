# Calcular el índice de Flesch-Szigriszt
def calcular_legibilidad(palabras, oraciones, silabas):
    if palabras == 0 or oraciones == 0:
        return None

    indice = (
        206.835
        - 62.3 * (silabas / palabras)
        - (palabras / oraciones)
    )

    return round(indice, 2)


# Clasificación según la escala INFLESZ
def clasificar_legibilidad(indice):
    if indice is None:
        return "Sin datos suficientes"
    if indice < 40:
        return "Muy difícil"
    elif indice < 55:
        return "Algo difícil"
    elif indice < 65:
        return "Normal"
    elif indice < 80:
        return "Bastante fácil"
    else:
        return "Muy fácil"
