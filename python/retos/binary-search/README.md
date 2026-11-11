# Solución para el Algoritmo de Búsqueda Binaria (Binary Search)

Se generaron dos implementaciones para resolver el problema de encontrar un elemento objetivo en una lista que ya se encuentra **ordenada**. La búsqueda binaria es uno de los algoritmos fundamentales en ciencias de la computación gracias a su estrategia de divide y vencerás (*divide and conquer*).

## Descripción del Problema

Dada una lista de enteros `nums` ordenada de forma ascendente y un valor entero `target`, escribe una función que busque `target` en `nums`.

- Si `target` existe en la lista, devuelve su **índice**.
- Si `target` no existe, devuelve `-1`.

### Ejemplo

Entrada:
```python
nums = [-1, 0, 3, 5, 9, 12]
target = 9
```

Salida:
```python
4
# Explicación: 9 existe en nums y su índice es 4.
```

---

Entrada:
```python
nums = [-1, 0, 3, 5, 9, 12]
target = 2
```

Salida:
```python
-1
# Explicación: 2 no está presente en la lista, por lo que devuelve -1.
```

---

## Implementaciones

### 1. Función `solution` (Iterativa con dos punteros)

Implementación clásica con punteros `left` y `right`. En cada iteración calcula el punto medio `mid = (left + right) // 2` y descarta la mitad de la lista donde con seguridad no se encuentra el elemento.
- **Complejidad temporal:** $O(\log n)$, reduce el espacio de búsqueda a la mitad en cada paso.
- **Complejidad espacial:** $O(1)$, no requiere memoria adicional.
- **Ideal para:** Comprender la mecánica interna del algoritmo divide y vencerás.

### 2. Función `solution_pythonic` (Módulo estándar `bisect`)

Utiliza el módulo `bisect` integrado en la biblioteca estándar de Python (`bisect.bisect_left`), el cual está altamente optimizado a nivel de C.
- **Complejidad temporal:** $O(\log n)$.
- **Complejidad espacial:** $O(1)$.
- **Ideal para:** Aplicaciones reales y código de producción idiomático.

---

## Cómo Ejecutar el Código

1. Asegúrate de tener Python 3.8 o superior instalado.
2. Ejecuta directamente el script `binary-search.py`:
   ```bash
   python binary-search.py
   ```
3. O abre el notebook interactivo `binary-search.ipynb` para ver la comparativa de rendimiento con `timeit`.

### Casos de Prueba

**Ejemplo 1:**
```python
# Entrada:
nums = [-1, 0, 3, 5, 9, 12]
target = 9
# Salida Esperada:
4
```

**Ejemplo 2:**
```python
# Entrada:
nums = [-1, 0, 3, 5, 9, 12]
target = 2
# Salida Esperada:
-1
```

**Ejemplo 3 (Lista vacía):**
```python
# Entrada:
nums = []
target = 5
# Salida Esperada:
-1
```
