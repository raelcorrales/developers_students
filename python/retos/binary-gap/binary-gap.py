"""
Solución para el Espacio Binario (Binary Gap).
"""

def solution(N: int) -> int:
    """
    Encuentra la longitud máxima de ceros rodeados por unos usando recorrido iterativo.
    
    :param N: Entero positivo.
    :return: Longitud del mayor binary gap.
    """
    binary_rep = bin(N)[2:]
    max_gap = 0
    current_gap = 0
    counting = False

    for bit in binary_rep:
        if bit == '1':
            if counting:
                if current_gap > max_gap:
                    max_gap = current_gap
            counting = True
            current_gap = 0
        elif counting:
            current_gap += 1

    return max_gap

def solution_pythonic(N: int) -> int:
    """
    Encuentra el mayor binary gap recortando ceros iniciales/finales y dividiendo por '1'.
    
    :param N: Entero positivo.
    :return: Longitud del mayor binary gap.
    """
    gaps = bin(N)[2:].strip('0').split('1')
    return max((len(gap) for gap in gaps), default=0)

if __name__ == "__main__":
    assert solution(9) == 2
    assert solution_pythonic(9) == 2

    assert solution(529) == 4
    assert solution_pythonic(529) == 4

    assert solution(20) == 1
    assert solution_pythonic(20) == 1

    assert solution(15) == 0
    assert solution_pythonic(15) == 0

    assert solution(1041) == 5
    assert solution_pythonic(1041) == 5

    print("[OK] Todas las pruebas de binary-gap pasaron exitosamente.")
