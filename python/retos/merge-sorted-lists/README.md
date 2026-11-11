# Solución para Fusión de Dos Listas Ordenadas (Merge Two Sorted Lists)

Se generaron dos implementaciones para resolver el problema clásico de fusionar dos listas que ya están ordenadas en una sola lista ordenada. Este es el paso clave (*merge*) del algoritmo **MergeSort** y enseña el patrón de diseño de **dos punteros (Two Pointers)**.

## Descripción del Problema

Dadas dos listas de números enteros `list1` y `list2`, ambas ordenadas de forma ascendente, fusiónalas en una única lista ordenada sin usar algoritmos de ordenamiento completos como `.sort()` desde cero.

### Ejemplo

Entrada:
```python
list1 = [1, 2, 4]
list2 = [1, 3, 4]
```

Salida:
```python
[1, 1, 2, 3, 4, 4]
```

---

Entrada:
```python
list1 = []
list2 = [0]
```

Salida:
```python
[0]
```

---

Entrada:
```python
list1 = []
list2 = []
```

Salida:
```python
[]
```

---

## Implementaciones

### 1. Función `solution` (Patrón de Dos Punteros)

Mantiene dos punteros `i` y `j` para recorrer simultáneamente `list1` y `list2`. En cada paso compara los elementos actuales, añade el menor a la lista final y avanza el puntero correspondiente. Al terminar uno de los recorridos, agrega los elementos sobrantes mediante slicing.
- **Complejidad temporal:** $O(n + m)$, lineal respecto al total de elementos combinados.
- **Complejidad espacial:** $O(n + m)$, para la lista resultante.
- **Ideal para:** Entender el principio de intercalación (*merge*) y algoritmos de divide y vencerás.

### 2. Función `solution_pythonic` (Uso de `heapq.merge`)

Utiliza `heapq.merge` de la biblioteca estándar de Python, que intercala eficientemente iterables previamente ordenados como un generador sin requerir cargar todo a la vez en memoria.
- **Complejidad temporal:** $O(n + m)$.
- **Complejidad espacial:** $O(n + m)$.
- **Ideal para:** Intercalar grandes volúmenes de datos ordenados de forma eficiente e idiomática.

---

## Cómo Ejecutar el Código

1. Asegúrate de tener Python 3.8 o superior.
2. Ejecuta el script `merge-sorted-lists.py`:
   ```bash
   python merge-sorted-lists.py
   ```
3. O abre el notebook interactivo `merge-sorted-lists.ipynb` para ver la comparativa de rendimiento con `timeit`.

### Casos de Prueba

**Ejemplo 1:**
```python
# Entrada:
list1 = [1, 2, 4]
list2 = [1, 3, 4]
# Salida Esperada:
[1, 1, 2, 3, 4, 4]
```

**Ejemplo 2:**
```python
# Entrada:
list1 = []
list2 = [0]
# Salida Esperada:
[0]
```

**Ejemplo 3:**
```python
# Entrada:
list1 = [2, 5, 8]
list2 = [1, 3, 9, 11]
# Salida Esperada:
[1, 2, 3, 5, 8, 9, 11]
```
