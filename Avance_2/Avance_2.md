# Avance 2 — Índice Flesch-Szigriszt y clasificación INFLESZ

## Objetivo

Implementar el cálculo de Flesch-Szigriszt y la clasificación de su puntuación mediante INFLESZ.

## Actividades realizadas

1. Implementación de `calcular_legibilidad(palabras, oraciones, silabas)`.
2. Implementación de `clasificar_legibilidad(indice)`.
3. Implementación de `demo_avance_2.py` para demostrar el cálculo del índice y la clasificación INFLESZ mediante valores de ejemplo.

## Fórmula utilizada

```text
Índice = 206.835 - 62.3 × (sílabas / palabras) - (palabras / oraciones)
```

## Funcionamiento

El cálculo del índice Flesch-Szigriszt y la clasificación INFLESZ se encuentran implementados en el archivo legibilidad.py.

Para demostrar su funcionamiento se incorporó el archivo demo_avance_2.py, que utiliza las funciones calcular_legibilidad y clasificar_legibilidad.

La demostración emplea los siguientes valores de ejemplo:

- Palabras: 100
- Oraciones: 5
- Sílabas: 200


Al aplicar la fórmula se obtiene un índice de 62,24, correspondiente a la categoría Normal según la escala INFLESZ.
Desde la carpeta Avance_2 se debe ejecutar: python demo_avance_2.py
Estos valores son ilustrativos y se utilizan para comprobar el funcionamiento del programa; no corresponden al análisis de una sentencia judicial real.

## Resultados
Se comprobó el funcionamiento del cálculo del índice Flesch-Szigriszt y su clasificación mediante la escala INFLESZ.
Para la demostración se utilizaron 100 palabras, 5 oraciones y 200 sílabas, obteniendo los siguientes resultados:

- Palabras: 100                  
- Oraciones: 5                   
- Sílabas: 200                   
- Índice Flesch-Szigriszt: 62.24 
- Clasificación INFLESZ: Normal  

Además, se ejecutó test_legibilidad.py, que contiene cuatro pruebas automáticas. Todas finalizaron correctamente con el mensaje OK.