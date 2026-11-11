"""
Solución para el Cálculo del Factorial.
"""

import math

def solution(n: int) -> int:
    """
    Calcula el factorial de n mediante un bucle iterativo.
    
    :param n: Entero no negativo.
    :return: n!
    """
    if n < 0:
        raise ValueError("n debe ser no negativo")
    ans = 1
    for i in range(2, n + 1):
        ans *= i
    return ans

def solution_pythonic(n: int) -> int:
    """
    Calcula el factorial utilizando la función optimizada math.factorial.
    
    :param n: Entero no negativo.
    :return: n!
    """
    return math.factorial(n)

if __name__ == "__main__":
    assert solution(0) == 1
    assert solution_pythonic(0) == 1

    assert solution(5) == 120
    assert solution_pythonic(5) == 120

    assert solution(10) == 3628800
    assert solution_pythonic(10) == 3628800

    print("[OK] Todas las pruebas de factorial-formula pasaron exitosamente.")
