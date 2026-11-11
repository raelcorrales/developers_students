# Solución para el Espacio Binario (Binary Gap)

Se generaron dos implementaciones para encontrar la longitud del mayor espacio binario (*binary gap*): la secuencia contigua más larga de ceros rodeada por unos en la representación binaria de un número entero positivo. Ejercicio clásico de Codility.

## Descripción del Problema

Dado un entero positivo `N`, devuelve la longitud de su mayor secuencia de ceros consecutivos rodeados por `1` a ambos lados en su forma binaria. Si no contiene espacios binarios, devuelve `0`.

### Ejemplo

- `N = 9` (binario: `1001`): longitud 2.
- `N = 529` (binario: `1000010001`): contiene espacios de 4 y 3 ceros; el mayor es 4.
- `N = 20` (binario: `10100`): el espacio es 1 (los ceros finales no están rodeados por 1).
- `N = 15` (binario: `1111`): devuelve 0.
