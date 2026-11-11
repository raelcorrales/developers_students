# Solución para el Problema de FizzBuzz Extensible

Se generaron dos implementaciones para el clásico ejercicio **FizzBuzz**. Este problema es ideal para principiantes y sirve para demostrar cómo refactorizar código de múltiples condicionales rígidos (`if/elif/else`) hacia un diseño extensible y limpio mediante diccionarios y concatenación.

## Descripción del Problema

Dado un número entero positivo `n`, devuelve una lista de cadenas del `1` al `n` donde:
- Si el número es divisible por `3`, agrega `"Fizz"`.
- Si el número es divisible por `5`, agrega `"Buzz"`.
- Si el número es divisible tanto por `3` como por `5`, agrega `"FizzBuzz"`.
- Si no es divisible por ninguno, agrega el número como cadena (ej. `"1"`, `"2"`).

### Ejemplo

Entrada:
```python
n = 5
```

Salida:
```python
["1", "2", "Fizz", "4", "Buzz"]
```

---

Entrada:
```python
n = 15
```

Salida:
```python
[
  "1", "2", "Fizz", "4", "Buzz",
  "Fizz", "7", "8", "Fizz", "Buzz",
  "11", "Fizz", "13", "14", "FizzBuzz"
]
```

---

## Implementaciones

### 1. Función `solution` (Condicionales explícitos)

Usa la clásica estructura `if/elif/else` comprobando primero la divisibilidad compuesta (`num % 15 == 0`), seguido de las divisibilidades individuales.
- **Complejidad temporal:** $O(n)$.
- **Complejidad espacial:** $O(n)$.
- **Ideal para:** Aprender la importancia del orden en estructuras condicionales.

### 2. Función `solution_pythonic` (Reglas mapeadas extensibles)

Utiliza una tupla o diccionario de reglas `[(3, "Fizz"), (5, "Buzz")]`. Concatena dinámicamente las palabras si el residuo es cero, permitiendo agregar nuevas reglas (ej. `(7, "Bazz")`) sin modificar la lógica interna (principio Open/Closed).
- **Complejidad temporal:** $O(n)$.
- **Complejidad espacial:** $O(n)$.
- **Ideal para:** Buenas prácticas de diseño de software y código modular.

---

## Cómo Ejecutar el Código

1. Asegúrate de tener Python 3.8 o superior.
2. Ejecuta el script `fizz-buzz.py`:
   ```bash
   python fizz-buzz.py
   ```
3. O abre el notebook interactivo `fizz-buzz.ipynb` para ver la comparativa de rendimiento con `timeit`.

### Casos de Prueba

**Ejemplo 1:**
```python
# Entrada:
n = 5
# Salida Esperada:
["1", "2", "Fizz", "4", "Buzz"]
```

**Ejemplo 2:**
```python
# Entrada:
n = 15
# Salida Esperada:
["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
```
