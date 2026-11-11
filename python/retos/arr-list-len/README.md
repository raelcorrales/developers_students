# Solución para Longitud de Lista Enlazada Representada en un Arreglo (ArrListLen)

Se generaron dos implementaciones para calcular la longitud de una lista enlazada simulada dentro de un arreglo. Ejercicio de Codility.

## Descripción del Problema

Un arreglo no vacío `A` de $N$ enteros representa una lista enlazada:
- La cabeza está en el índice `0`.
- El valor `A[K]` indica el índice del siguiente nodo.
- Si `A[K] == -1`, ese nodo es la cola (fin de la lista).

Devuelve la cantidad de nodos visitados desde la cabeza hasta el nodo final.

### Ejemplo

Entrada: `A = [1, 4, -1, 3, 2]`
Recorrido: índice `0` (val 1) -> índice `1` (val 4) -> índice `4` (val 2) -> índice `2` (val -1, fin).
Total nodos: `4`.
Salida: `4`
