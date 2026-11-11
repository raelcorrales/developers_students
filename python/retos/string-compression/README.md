# Solución para Compresión de Cadenas (Run-Length Encoding)

Se generaron dos implementaciones para resolver el problema de compresión de cadenas utilizando el algoritmo **Run-Length Encoding (RLE)**. Este problema enseña el manejo cuidadoso de punteros, índices y condiciones de frontera en secuencias contiguas.

## Descripción del Problema

Dada una cadena de texto `s`, comprime la cadena reemplazando las secuencias repetidas consecutivamente de caracteres por el carácter seguido del conteo de repeticiones (por ejemplo, `"a3b2c1"`).

- Si la cadena comprimida **no es más corta** que la cadena original, la función debe devolver la **cadena original**.
- Si la cadena está vacía, devuelve `""`.

### Ejemplo

Entrada:
```python
s = "aabcccccaaa"
```

Salida:
```python
"a2b1c5a3"
# Explicación: La longitud de "a2b1c5a3" (8) es menor que "aabcccccaaa" (11).
```

---

Entrada:
```python
s = "abc"
```

Salida:
```python
"abc"
# Explicación: La versión comprimida sería "a1b1c1" (longitud 6), que es mayor que la original (3).
```

---

## Implementaciones

### 1. Función `solution` (Recorrido con contador acumulativo)

Recorre la cadena con un bucle mientras cuenta las apariciones consecutivas del carácter actual. Al cambiar de carácter o llegar al final, acumula en una lista (evitando la concatenación ineficiente de strings $O(n^2)$) y compara las longitudes finales.
- **Complejidad temporal:** $O(n)$.
- **Complejidad espacial:** $O(n)$.
- **Ideal para:** Aprender control de flujo y gestión de secuencias consecutivas.

### 2. Función `solution_pythonic` (Uso de `itertools.groupby`)

Aprovecha el iterador `groupby` de la librería estándar `itertools`, que agrupa de forma nativa elementos consecutivos idénticos.
- **Complejidad temporal:** $O(n)$.
- **Complejidad espacial:** $O(n)$.
- **Ideal para:** Soluciones idiomáticas y concisas en Python.

---

## Cómo Ejecutar el Código

1. Asegúrate de tener Python 3.8 o superior.
2. Ejecuta el script `string-compression.py`:
   ```bash
   python string-compression.py
   ```
3. O abre el notebook interactivo `string-compression.ipynb` para evaluar la velocidad con `timeit`.

### Casos de Prueba

**Ejemplo 1:**
```python
# Entrada:
s = "aabcccccaaa"
# Salida Esperada:
"a2b1c5a3"
```

**Ejemplo 2:**
```python
# Entrada:
s = "abcd"
# Salida Esperada:
"abcd"
```

**Ejemplo 3 (Cadena vacía):**
```python
# Entrada:
s = ""
# Salida Esperada:
""
```
