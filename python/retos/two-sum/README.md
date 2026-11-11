# Solución para el Problema de Suma de Dos Números (Two Sum)

Se generaron dos implementaciones para resolver el problema clásico de encontrar dos números en una lista cuya suma sea igual a un valor objetivo (`target`). Este es uno de los ejercicios fundamentales en entrevistas técnicas y aprendizaje de estructuras de datos, ya que permite comprender el paso de una solución de fuerza bruta a una solución optimizada con tablas hash.

## Descripción del Problema

Dada una lista de enteros `nums` y un entero `target`, el objetivo es devolver los **índices** de los dos números que sumados den como resultado el valor de `target`.

Se asume que cada entrada tiene exactamente una solución (o se devuelve una lista vacía `[]` si no hay solución) y no se puede usar el mismo elemento del mismo índice dos veces.

### Ejemplo

Entrada:
```python
nums = [2, 7, 11, 15]
target = 9
```

Salida:
```python
[0, 1]
# Explicación: nums[0] + nums[1] = 2 + 7 = 9
```

---

Entrada:
```python
nums = [3, 2, 4]
target = 6
```

Salida:
```python
[1, 2]
# Explicación: nums[1] + nums[2] = 2 + 4 = 6
```

---

## Implementaciones

### 1. Función `solution` (Fuerza Bruta)

Esta es una implementación clásica y directa que utiliza dos bucles anidados (`for`) para comparar cada par posible de elementos en la lista.
- **Complejidad temporal:** $O(n^2)$, ya que evalúa todas las parejas posibles.
- **Complejidad espacial:** $O(1)$, pues no requiere memoria adicional.
- **Ideal para:** Estudiantes que están aprendiendo a recorrer listas y anidar bucles.

### 2. Función `solution_pythonic` (Tabla Hash / Diccionario)

Esta es una implementación optimizada que utiliza un diccionario para almacenar los números que ya han sido visitados y sus índices correspondientes. En cada paso, calcula el complemento (`target - num`) y verifica si ya existe en el diccionario en tiempo promedio constante $O(1)$.
- **Complejidad temporal:** $O(n)$, ya que recorre la lista una sola vez.
- **Complejidad espacial:** $O(n)$, para almacenar los elementos en el diccionario.
- **Ideal para:** Comprender el compromiso de memoria vs. tiempo (*time-space tradeoff*) y el poder de los diccionarios en Python.

---

## Cómo Ejecutar el Código

1. Asegúrate de tener Python instalado en tu sistema (versión 3.8 o superior).
2. Puedes ejecutar directamente el script `two-sum.py`:
   ```bash
   python two-sum.py
   ```
3. O abrir el notebook interactivo `two-sum.ipynb` en Jupyter Notebook o VS Code para ver la comparativa de tiempos con `timeit`.

### Casos de Prueba

**Ejemplo 1:**
```python
# Entrada:
nums = [2, 7, 11, 15]
target = 9
# Salida Esperada:
[0, 1]
```

**Ejemplo 2:**
```python
# Entrada:
nums = [3, 2, 4]
target = 6
# Salida Esperada:
[1, 2]
```

**Ejemplo 3:**
```python
# Entrada:
nums = [3, 3]
target = 6
# Salida Esperada:
[0, 1]
```

**Ejemplo 4 (Sin solución):**
```python
# Entrada:
nums = [1, 2, 3]
target = 10
# Salida Esperada:
[]
```
