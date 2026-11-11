"""
Solución para Contar Pasos en la Secuencia de Collatz.
"""

def solution(n: int) -> int:
    """
    Calcula los pasos de la secuencia de Collatz hasta llegar a 1.
    
    :param n: Entero positivo.
    :return: Número de pasos.
    """
    steps = 0
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps

def solution_pythonic(n: int) -> int:
    """
    Versión generadora para contar pasos de Collatz.
    
    :param n: Entero positivo.
    :return: Número de pasos.
    """
    def _gen(val):
        while val > 1:
            val = val // 2 if val % 2 == 0 else 3 * val + 1
            yield val
    return sum(1 for _ in _gen(n))

if __name__ == "__main__":
    assert solution(1) == 0
    assert solution_pythonic(1) == 0

    assert solution(3) == 7
    assert solution_pythonic(3) == 7

    assert solution(6) == 8
    assert solution_pythonic(6) == 8

    print("[OK] Todas las pruebas de collatz-sequence-steps pasaron exitosamente.")
