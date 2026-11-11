"""
Solución para Intersección de Dos Listas.
"""

def solution(a: list, b: list) -> list:
    """
    Encuentra la intersección de dos listas usando conjuntos para búsqueda eficiente O(1).
    
    :param a: Primera lista.
    :param b: Segunda lista.
    :return: Lista con elementos comunes sin duplicados.
    """
    set_b = set(b)
    result = []
    seen = set()
    for item in a:
        if item in set_b and item not in seen:
            result.append(item)
            seen.add(item)
    return result

def solution_pythonic(a: list, b: list) -> list:
    """
    Encuentra la intersección de dos listas utilizando el operador de intersección de conjuntos (&).
    
    :param a: Primera lista.
    :param b: Segunda lista.
    :return: Lista con elementos comunes.
    """
    return list(set(a) & set(b))

if __name__ == "__main__":
    res1 = solution([1, 2, 3, 4, 5], [0, 1, 3, 7])
    assert sorted(res1) == [1, 3]
    res1_py = solution_pythonic([1, 2, 3, 4, 5], [0, 1, 3, 7])
    assert sorted(res1_py) == [1, 3]

    assert solution([1, 2, 3], [4, 5, 6]) == []
    assert solution_pythonic([1, 2, 3], [4, 5, 6]) == []

    print("[OK] Todas las pruebas de intersection-of-two-lists pasaron exitosamente.")
