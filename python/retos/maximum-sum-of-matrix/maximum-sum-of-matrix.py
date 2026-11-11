"""
Solución para la Suma Máxima de una Matriz sin Compartir Fila ni Columna.
"""

from itertools import permutations

def solution(matrix: list) -> int | float:
    """
    Calcula la máxima suma seleccionando elementos que no comparten fila ni columna
    usando todas las permutaciones de columnas posibles.
    
    :param matrix: Lista de listas cuadrada NxN.
    :return: Máxima suma posible.
    """
    n = len(matrix)
    if n == 0:
        return 0
    if n == 1:
        return matrix[0][0] if len(matrix[0]) == 1 else max(matrix[0])

    max_sum = float('-inf')
    for perm in permutations(range(n)):
        curr_sum = sum(matrix[i][perm[i]] for i in range(n))
        if curr_sum > max_sum:
            max_sum = curr_sum
            
    return max_sum

def solution_pythonic(matrix: list) -> int | float:
    """
    Versión en una línea con max y generador de permutaciones.
    
    :param matrix: Lista de listas cuadrada NxN.
    :return: Máxima suma.
    """
    n = len(matrix)
    if not matrix or not matrix[0]:
        return 0
    return max(sum(matrix[i][p[i]] for i in range(n)) for p in permutations(range(n)))

if __name__ == "__main__":
    m1 = [[3, 1, 2], [4, 5, 6], [-7, 8, 9]]
    assert solution(m1) == 17
    assert solution_pythonic(m1) == 17

    m2 = [[1, 2, 1], [2, 1, 2], [1, 2, 1]]
    assert solution(m2) == 5
    assert solution_pythonic(m2) == 5

    print("[OK] Todas las pruebas de maximum-sum-of-matrix pasaron exitosamente.")
