# Solución para Conversión de Números Romanos a Enteros

Se generaron dos implementaciones para convertir una cadena que representa un número romano válido en un número entero decimal. Pregunta clásica de entrevista (Palantir).

## Descripción del Problema

Dado un número romano válido `s`, devuelve su valor entero correspondiente.
Símbolos: `I=1`, `V=5`, `X=10`, `L=50`, `C=100`, `D=500`, `M=1000`.
Regla de resta: Si un símbolo de menor valor aparece antes de uno de mayor valor (ej. `IV=4`, `IX=9`, `XL=40`, `XC=90`, `CD=400`, `CM=900`), se resta.

### Ejemplo

Entrada:
```python
s = "MCMXCIV"
```

Salida:
```python
1994
# M (1000) + CM (900) + XC (90) + IV (4) = 1994
```

---

## Implementaciones

### 1. Función `solution` (Recorrido con avance variable)

Recorre la cadena de izquierda a derecha. Si el símbolo siguiente tiene un valor mayor, toma ambos caracteres como pareja de resta y avanza 2 posiciones; si no, suma el valor del símbolo actual y avanza 1 posición.
- **Complejidad temporal:** $O(n)$.
- **Complejidad espacial:** $O(1)$.

### 2. Función `solution_pythonic` (Recorrido inverso)

Recorre la cadena de derecha a izquierda manteniendo el valor máximo visto. Si el valor actual es menor que el anterior más grande, se resta; de lo contrario, se suma.
- **Complejidad temporal:** $O(n)$.
- **Complejidad espacial:** $O(1)$.

---

## Cómo Ejecutar el Código

1. Ejecuta el script: `python roman-to-integer.py`
2. O abre el notebook interactivo: `roman-to-integer.ipynb`
