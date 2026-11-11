# Solución para Contar Tripletes Aritméticos

Se generaron dos implementaciones para contar los tripletes aritméticos con una diferencia fija en una lista de enteros estrictamente creciente. Pregunta de Oracle.

## Descripción del Problema

Dada una lista `nums` ordenada estrictamente creciente y un entero positivo `diff`, un triplete `(i, j, k)` es aritmético si:
- `i < j < k`
- `nums[j] - nums[i] == diff`
- `nums[k] - nums[j] == diff`

Devuelve la cantidad total de tripletes válidos.

### Ejemplo

Entrada: `nums = [1, 2, 4, 6, 7, 11, 12], diff = 5`
Tripletes: `(1, 6, 11)` y `(2, 7, 12)`
Salida: `2`
