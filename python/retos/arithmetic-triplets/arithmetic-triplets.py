"""
Solución para Contar Tripletes Aritméticos.
"""

def solution(nums: list, diff: int) -> int:
    """
    Cuenta tripletes aritméticos usando búsqueda exhaustiva de tres bucles.
    
    :param nums: Lista ordenada de enteros.
    :param diff: Diferencia requerida entre elementos consecutivos del triplete.
    :return: Total de tripletes encontrados.
    """
    count = 0
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[j] - nums[i] == diff:
                for k in range(j + 1, n):
                    if nums[k] - nums[j] == diff:
                        count += 1
    return count

def solution_pythonic(nums: list, diff: int) -> int:
    """
    Cuenta tripletes aritméticos en O(n) utilizando un conjunto para búsqueda O(1).
    
    :param nums: Lista ordenada de enteros.
    :param diff: Diferencia requerida.
    :return: Total de tripletes.
    """
    num_set = set(nums)
    return sum(1 for a in nums if (a + diff in num_set and a + 2 * diff in num_set))

if __name__ == "__main__":
    assert solution([1, 2, 4, 6, 7, 11, 12], 5) == 2
    assert solution_pythonic([1, 2, 4, 6, 7, 11, 12], 5) == 2

    assert solution([4, 5, 6, 7, 8, 9], 2) == 2
    assert solution_pythonic([4, 5, 6, 7, 8, 9], 2) == 2

    print("[OK] Todas las pruebas de arithmetic-triplets pasaron exitosamente.")
