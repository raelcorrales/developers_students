"""
Solución para la Suma de Múltiplos de FizzBuzz.
"""

def solution(target: int) -> int:
    """
    Calcula la suma de múltiplos de 3 o 5 menores a target usando un bucle acumulativo.
    
    :param target: Límite superior estricto.
    :return: Suma de múltiplos.
    """
    total = 0
    for i in range(1, target):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total

def solution_pythonic(target: int) -> int:
    """
    Calcula la suma de múltiplos utilizando una comprensión de generador.
    
    :param target: Límite superior estricto.
    :return: Suma de múltiplos.
    """
    return sum(i for i in range(1, target) if i % 3 == 0 or i % 5 == 0)

if __name__ == "__main__":
    assert solution(10) == 23
    assert solution_pythonic(10) == 23

    assert solution(16) == 60
    assert solution_pythonic(16) == 60

    assert solution(100) == 2318
    assert solution_pythonic(100) == 2318

    print("[OK] Todas las pruebas de fizz-buzz-sum pasaron exitosamente.")
