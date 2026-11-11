# Solución para Determinar si un Año es Bisiesto

Se generaron dos implementaciones para verificar si un año determinado es bisiesto de acuerdo con las reglas del calendario gregoriano.

## Descripción del Problema

Un año es bisiesto si:
1. Es divisible entre 4, Y
2. NO es divisible entre 100, A MENOS QUE también sea divisible entre 400.

### Ejemplo

Entrada: `year = 2000` -> Salida: `True` (divisible entre 400)
Entrada: `year = 1900` -> Salida: `False` (divisible entre 100 pero no entre 400)
Entrada: `year = 2024` -> Salida: `True`
