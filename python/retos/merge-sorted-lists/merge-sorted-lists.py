"""
Solución para Fusión de Dos Listas Ordenadas (Merge Two Sorted Lists).
"""

import heapq

def solution(list1: list, list2: list) -> list:
    """
    Fusiona dos listas ordenadas en una nueva lista ordenada usando el patrón de dos punteros.
    
    :param list1: Primera lista ordenada ascendentemente.
    :param list2: Segunda lista ordenada ascendentemente.
    :return: Lista fusionada y ordenada.
    """
    merged = []
    i = 0
    j = 0
    len1 = len(list1)
    len2 = len(list2)

    # Paso 1: Recorremos ambas listas comparando los elementos actuales.
    while i < len1 and j < len2:
        if list1[i] <= list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1

    # Paso 2: Si quedaron elementos sobrantes en alguna lista, los concatenamos.
    if i < len1:
        merged.extend(list1[i:])
    if j < len2:
        merged.extend(list2[j:])

    return merged


def solution_pythonic(list1: list, list2: list) -> list:
    """
    Fusiona dos listas ordenadas utilizando heapq.merge de la biblioteca estándar.
    
    :param list1: Primera lista ordenada.
    :param list2: Segunda lista ordenada.
    :return: Lista fusionada y ordenada.
    """
    # heapq.merge intercala iterables ya ordenados de forma eficiente.
    return list(heapq.merge(list1, list2))


if __name__ == "__main__":
    assert solution([1, 2, 4], [1, 3, 4]) == [1, 1, 2, 3, 4, 4]
    assert solution_pythonic([1, 2, 4], [1, 3, 4]) == [1, 1, 2, 3, 4, 4]

    assert solution([], [0]) == [0]
    assert solution_pythonic([], [0]) == [0]

    assert solution([], []) == []
    assert solution_pythonic([], []) == []

    assert solution([2, 5, 8], [1, 3, 9, 11]) == [1, 2, 3, 5, 8, 9, 11]
    assert solution_pythonic([2, 5, 8], [1, 3, 9, 11]) == [1, 2, 3, 5, 8, 9, 11]

    print("[OK] Todas las pruebas de merge-sorted-lists pasaron exitosamente.")
