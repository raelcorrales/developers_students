# Solución para Aplanar Listas Anidadas (Flatten Nested List)

Se generaron dos implementaciones para resolver el problema de transformar una estructura de listas arbitrariamente anidadas en una lista plana unidimensional. Este reto es excelente para introducir y dominar la **recursividad** y los **generadores** en Python.

## Descripción del Problema

Dada una lista que puede contener elementos individuales u otras listas anidadas con cualquier nivel de profundidad, escribe una función que devuelva una sola lista plana con todos los elementos en el mismo orden original.

### Ejemplo

Entrada:
```python
nested = [1, [2, [3, 4], 5], 6, [7, 8]]
```

Salida:
```python
[1, 2, 3, 4, 5, 6, 7, 8]
```

---

Entrada:
```python
nested = [[[[1]]], 2, [3]]
```

Salida:
```python
[1, 2, 3]
```

---

## Implementaciones

### 1. Función `solution` (Recursividad clásica)

Recorre cada elemento de la lista; si el elemento es una lista (`isinstance(item, list)`), se llama a sí misma recursivamente y extiende la lista resultado. Si no es lista, simplemente lo añade.
- **Complejidad temporal:** $O(N)$, donde $N$ es el total de elementos individuales.
- **Complejidad espacial:** $O(D)$ en la pila de llamadas, donde $D$ es la profundidad máxima de anidación.
- **Ideal para:** Estudiantes aprendiendo el caso base y el caso recursivo.

### 2. Función `solution_pythonic` (Generador con `yield from`)

Utiliza una función generadora con la palabra clave `yield from`. Esto permite producir los elementos uno a uno sin crear copias intermedias en memoria, convirtiéndose finalmente a lista.
- **Complejidad temporal:** $O(N)$.
- **Complejidad espacial:** $O(D)$ de profundidad de llamada.
- **Ideal para:** Manejo eficiente de memoria y dominio del modelo de iteración de Python.

---

## Cómo Ejecutar el Código

1. Asegúrate de tener Python 3.8 o superior.
2. Ejecuta el script `flatten-list.py`:
   ```bash
   python flatten-list.py
   ```
3. O abre el notebook interactivo `flatten-list.ipynb` para ver la comparativa de rendimiento con `timeit`.

### Casos de Prueba

**Ejemplo 1:**
```python
# Entrada:
nested = [1, [2, [3, 4], 5], 6, [7, 8]]
# Salida Esperada:
[1, 2, 3, 4, 5, 6, 7, 8]
```

**Ejemplo 2:**
```python
# Entrada:
nested = []
# Salida Esperada:
[]
```

**Ejemplo 3:**
```python
# Entrada:
nested = [1, 2, 3]
# Salida Esperada:
[1, 2, 3]
```
