"""
Solución para el Algoritmo de Búsqueda Binaria (Binary Search).
"""

import bisect

def solution(nums: list, target: int) -> int:
    """
    Busca `target` en una lista ordenada `nums` usando búsqueda binaria iterativa.
    
    :param nums: Lista de enteros ordenados ascendentemente.
    :param target: Valor que se desea encontrar.
    :return: Índice de target en nums, o -1 si no está presente.
    """
    # Paso 1: Definimos los límites izquierdo y derecho de búsqueda.
    left = 0
    right = len(nums) - 1

    # Paso 2: Continuamos mientras el puntero izquierdo no supere al derecho.
    while left <= right:
        # Paso 3: Calculamos el índice medio.
        mid = (left + right) // 2

        # Paso 4: Si encontramos el target en la posición media, devolvemos su índice.
        if nums[mid] == target:
            return mid
        # Paso 5: Si el elemento medio es menor que target, buscamos en la mitad derecha.
        elif nums[mid] < target:
            left = mid + 1
        # Paso 6: Si el elemento medio es mayor que target, buscamos en la mitad izquierda.
        else:
            right = mid - 1

    # Paso 7: Si salimos del ciclo sin encontrarlo, devolvemos -1.
    return -1


def solution_pythonic(nums: list, target: int) -> int:
    """
    Busca `target` en una lista ordenada `nums` utilizando el módulo estándar bisect.
    
    :param nums: Lista de enteros ordenados ascendentemente.
    :param target: Valor que se desea encontrar.
    :return: Índice de target en nums, o -1 si no está presente.
    """
    # Paso 1: Usamos bisect_left para encontrar la posición de inserción de target.
    index = bisect.bisect_left(nums, target)
    
    # Paso 2: Verificamos si el índice está dentro del rango y el valor coincide.
    if index < len(nums) and nums[index] == target:
        return index
        
    return -1


if __name__ == "__main__":
    nums1 = [-1, 0, 3, 5, 9, 12]
    assert solution(nums1, 9) == 4
    assert solution_pythonic(nums1, 9) == 4

    assert solution(nums1, 2) == -1
    assert solution_pythonic(nums1, 2) == -1

    assert solution([], 5) == -1
    assert solution_pythonic([], 5) == -1

    assert solution([5], 5) == 0
    assert solution_pythonic([5], 5) == 0

    assert solution([5], 10) == -1
    assert solution_pythonic([5], 10) == -1

    print("[OK] Todas las pruebas de binary-search pasaron exitosamente.")
