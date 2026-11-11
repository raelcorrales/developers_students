# Solución para Contar Pasos en la Secuencia de Collatz

Se generaron dos implementaciones para calcular el número de pasos que toma a un número entero positivo `n` llegar a `1` aplicando las reglas de la conjetura de Collatz ($3n + 1$). Pregunta de Bloomberg.

## Descripción del Problema

Dado un número entero positivo `n`, aplica iterativamente:
- Si `n` es par: `n = n // 2`
- Si `n` es impar: `n = 3 * n + 1`

Devuelve la cantidad total de transformaciones necesarias hasta alcanzar el valor `1`.

### Ejemplo

Entrada:
```python
n = 3
```

Salida:
```python
7
# Secuencia: 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1 (7 pasos)
```
