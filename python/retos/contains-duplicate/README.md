# Solución para Determinar si una Lista Contiene Duplicados

Se generaron dos implementaciones para resolver el problema clásico de detectar elementos repetidos en una colección de datos. Esta es una pregunta clásica de entrevista (Apple).

## Descripción del Problema

Dada una lista de enteros `nums`, devuelve `True` si algún valor aparece al menos dos veces en la lista. Devuelve `False` si todos los elementos son distintos.

### Ejemplo

Entrada:
```python
nums = [1, 2, 3, 1]
```

Salida:
```python
True
```

---

Entrada:
```python
nums = [1, 2, 3, 4]
```

Salida:
```python
False
```

---

## Implementaciones

### 1. Función `solution` (Conjunto acumulativo paso a paso)

Recorre la lista elemento por elemento y mantiene un conjunto (`set`) de números ya vistos. Si encuentra un número que ya está en el conjunto, retorna `True` inmediatamente sin recorrer el resto (retorno temprano).
- **Complejidad temporal:** $O(n)$ en el peor caso, pero puede terminar mucho antes.
- **Complejidad espacial:** $O(n)$ para el conjunto de números visitados.

### 2. Función `solution_pythonic` (Comparativa de cardinalidad)

Compara la longitud del conjunto generado a partir de la lista con la longitud original: `len(set(nums)) < len(nums)`.
- **Complejidad temporal:** $O(n)$.
- **Complejidad espacial:** $O(n)$.
- **Ideal para:** Una línea de código idiomática y expresiva.

---

## Cómo Ejecutar el Código

1. Ejecuta el script: `python contains-duplicate.py`
2. O abre el notebook interactivo: `contains-duplicate.ipynb`
