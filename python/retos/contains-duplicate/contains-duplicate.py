"""
Solución para Determinar si una Lista Contiene Duplicados.
"""

def solution(nums: list) -> bool:
    """
    Determina si la lista contiene duplicados usando un conjunto de visitados.
    
    :param nums: Lista de números enteros.
    :return: True si hay duplicados, False si todos son únicos.
    """
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

def solution_pythonic(nums: list) -> bool:
    """
    Determina si hay duplicados comparando la longitud de la lista con su conjunto.
    
    :param nums: Lista de números enteros.
    :return: True si hay duplicados, False si todos son únicos.
    """
    return len(set(nums)) < len(nums)

if __name__ == "__main__":
    assert solution([1, 2, 3, 1]) is True
    assert solution_pythonic([1, 2, 3, 1]) is True

    assert solution([1, 2, 3, 4]) is False
    assert solution_pythonic([1, 2, 3, 4]) is False

    assert solution([]) is False
    assert solution_pythonic([]) is False

    print("[OK] Todas las pruebas de contains-duplicate pasaron exitosamente.")
