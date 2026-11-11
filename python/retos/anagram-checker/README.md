# Solución para Verificar si Dos Cadenas son Anagramas

Se generaron tres implementaciones para resolver el problema de determinar si dos cadenas de texto son **anagramas**. Un anagrama es una palabra o frase formada al reorganizar las letras de otra palabra o frase diferente, utilizando exactamente las mismas letras originales y la misma cantidad de veces (ignorando mayúsculas, espacios y caracteres especiales).

## Descripción del Problema

Dadas dos cadenas de texto `s1` y `s2`, determina si `s2` es un anagrama de `s1`.

### Ejemplo

Entrada:
```python
s1 = "listen"
s2 = "silent"
```

Salida:
```python
True
```

---

Entrada:
```python
s1 = "Amor"
s2 = "Roma"
```

Salida:
```python
True
```

---

Entrada:
```python
s1 = "rat"
s2 = "car"
```

Salida:
```python
False
```

---

Entrada:
```python
s1 = "A gentleman"
s2 = "Elegant man"
```

Salida:
```python
True
```

---

## Implementaciones

### 1. Función `solution` (Diccionario de frecuencias manual)

Esta implementación limpia ambas cadenas mediante expresiones regulares y luego utiliza un diccionario de Python estándar para contar las frecuencias de cada carácter en la primera cadena, restando luego con la segunda.
- **Complejidad temporal:** $O(n)$, donde $n$ es la cantidad de caracteres.
- **Complejidad espacial:** $O(1)$ o $O(k)$ donde $k$ es el tamaño del alfabeto (constante acotado).
- **Ideal para:** Comprender el algoritmo base de conteo sin depender de librerías especializadas.

### 2. Función `solution_pythonic` (Uso de `collections.Counter`)

Esta es una implementación concisa y eficiente que utiliza `Counter` de la librería estándar de Python. `Counter` crea internamente una tabla hash optimizada en C que compara directamente la multiset de caracteres.
- **Complejidad temporal:** $O(n)$.
- **Complejidad espacial:** $O(k)$.
- **Ideal para:** Código idiomático (*pythonic*) y legible en proyectos reales.

### 3. Función `solution_sorted` (Ordenamiento)

Esta implementación normaliza las cadenas, las ordena alfabéticamente usando la función integrada `sorted()` y comprueba si las listas resultantes son idénticas.
- **Complejidad temporal:** $O(n \log n)$, debido al algoritmo Timsort de Python.
- **Complejidad espacial:** $O(n)$, para almacenar las listas ordenadas.
- **Ideal para:** Soluciones de una sola línea cuando las cadenas son cortas y la legibilidad prima sobre la complejidad asintótica.

---

## Cómo Ejecutar el Código

1. Asegúrate de tener Python instalado en tu sistema (versión 3.8 o superior).
2. Puedes ejecutar directamente el script `anagram-checker.py`:
   ```bash
   python anagram-checker.py
   ```
3. O abrir el notebook interactivo `anagram-checker.ipynb` en Jupyter Notebook o VS Code para ver la comparativa de tiempos con `timeit`.

### Casos de Prueba

**Ejemplo 1:**
```python
# Entrada:
s1 = "listen"
s2 = "silent"
# Salida Esperada:
True
```

**Ejemplo 2:**
```python
# Entrada:
s1 = "A gentleman"
s2 = "Elegant man"
# Salida Esperada:
True
```

**Ejemplo 3:**
```python
# Entrada:
s1 = "hello"
s2 = "world"
# Salida Esperada:
False
```
