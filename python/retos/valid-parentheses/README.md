# Solución para Validar Paréntesis y Signos de Agrupación Balanceados

Se generaron dos implementaciones para resolver el problema clásico de verificar si una cadena compuesta por corchetes, paréntesis y llaves está correctamente balanceada y anidada. Este desafío es fundamental para comprender el funcionamiento de la estructura de datos **Pila (Stack)** y su principio LIFO (*Last In, First Out*).

## Descripción del Problema

Dada una cadena de texto `s` que contiene únicamente los caracteres `'('`, `')'`, `'{'`, `'}'`, `'['` y `']'`, determina si la cadena de entrada es válida.

Una cadena de entrada es válida si:
1. Los corchetes abiertos se cierran con el mismo tipo de corchete.
2. Los corchetes abiertos se cierran en el orden correcto.
3. Cada corchete cerrado tiene su corchete de apertura correspondiente.

### Ejemplo

Entrada:
```python
s = "()"
```

Salida:
```python
True
```

---

Entrada:
```python
s = "()[]{}"
```

Salida:
```python
True
```

---

Entrada:
```python
s = "(]"
```

Salida:
```python
False
```

---

Entrada:
```python
s = "([{}])"
```

Salida:
```python
True
```

---

## Implementaciones

### 1. Función `solution` (Pila con condicionales explícitos)

Esta es una implementación detallada y estructurada que utiliza una lista de Python simulando una **pila** (*stack*). Al encontrar un símbolo de apertura, lo almacena usando `append()`. Al encontrar un símbolo de cierre, verifica que la pila no esté vacía y que el último elemento coincida mediante `pop()`.
- **Complejidad temporal:** $O(n)$, donde $n$ es la longitud de la cadena.
- **Complejidad espacial:** $O(n)$, en el peor de los casos todos son caracteres de apertura.
- **Ideal para:** Estudiantes que quieren entender cómo funciona el seguimiento de estado y el principio LIFO paso a paso.

### 2. Función `solution_pythonic` (Pila con Diccionario de Mapeo)

Esta implementación optimiza la legibilidad del código utilizando un diccionario donde cada símbolo de cierre tiene como valor su correspondiente símbolo de apertura. Esto elimina la necesidad de múltiples bloques `elif` y hace que el código sea más limpio, mantenible y extensible a nuevos pares de caracteres.
- **Complejidad temporal:** $O(n)$.
- **Complejidad espacial:** $O(n)$.
- **Ideal para:** Código de producción y comprensión de abstracciones con diccionarios.

---

## Cómo Ejecutar el Código

1. Asegúrate de tener Python instalado en tu sistema (versión 3.8 o superior).
2. Puedes ejecutar el script `valid-parentheses.py`:
   ```bash
   python valid-parentheses.py
   ```
3. O abrir el notebook interactivo `valid-parentheses.ipynb` en Jupyter Notebook o VS Code para explorar las pruebas y mediciones con `timeit`.

### Casos de Prueba

**Ejemplo 1:**
```python
# Entrada:
s = "()"
# Salida Esperada:
True
```

**Ejemplo 2:**
```python
# Entrada:
s = "()[]{}"
# Salida Esperada:
True
```

**Ejemplo 3:**
```python
# Entrada:
s = "(]"
# Salida Esperada:
False
```

**Ejemplo 4:**
```python
# Entrada:
s = "([{}])"
# Salida Esperada:
True
```

**Ejemplo 5:**
```python
# Entrada:
s = "([)]"
# Salida Esperada:
False
```
