"""
Solución para Aplanar Listas Anidadas (Flatten Nested List).
"""

def solution(nested_list: list) -> list:
    """
    Aplana una lista anidada con cualquier nivel de profundidad usando recursión clásica.
    
    :param nested_list: Lista que puede contener sublistas anidadas.
    :return: Lista unidimensional plana.
    """
    flat = []
    
    # Paso 1: Recorremos cada elemento de la lista recibida.
    for item in nested_list:
        # Paso 2: Si el elemento es otra lista, llamamos recursivamente a la función.
        if isinstance(item, list):
            flat.extend(solution(item))
        else:
            # Paso 3: Si es un elemento básico, lo agregamos directamente al resultado.
            flat.append(item)
            
    return flat


def solution_pythonic(nested_list: list) -> list:
    """
    Aplana una lista anidada utilizando un generador con 'yield from'.
    
    :param nested_list: Lista con sublistas anidadas.
    :return: Lista unidimensional plana.
    """
    def _flatten_gen(items):
        for item in items:
            if isinstance(item, list):
                # 'yield from' delega la generación al sub-generador recursivo.
                yield from _flatten_gen(item)
            else:
                yield item

    return list(_flatten_gen(nested_list))


if __name__ == "__main__":
    assert solution([1, [2, [3, 4], 5], 6, [7, 8]]) == [1, 2, 3, 4, 5, 6, 7, 8]
    assert solution_pythonic([1, [2, [3, 4], 5], 6, [7, 8]]) == [1, 2, 3, 4, 5, 6, 7, 8]

    assert solution([[[[1]]], 2, [3]]) == [1, 2, 3]
    assert solution_pythonic([[[[1]]], 2, [3]]) == [1, 2, 3]

    assert solution([]) == []
    assert solution_pythonic([]) == []

    assert solution([1, 2, 3]) == [1, 2, 3]
    assert solution_pythonic([1, 2, 3]) == [1, 2, 3]

    print("[OK] Todas las pruebas de flatten-list pasaron exitosamente.")
