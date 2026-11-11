"""
Solución para Longitud de Lista Enlazada Representada en un Arreglo (ArrListLen).
"""

def solution(A: list) -> int:
    """
    Calcula la cantidad de nodos en la lista enlazada recorriendo los índices de A.
    
    :param A: Lista de enteros no vacía donde A[k] apunta al siguiente índice (-1 para fin).
    :return: Cantidad total de nodos.
    """
    length = 0
    curr = 0
    while curr != -1:
        length += 1
        curr = A[curr]
    return length

def solution_pythonic(A: list) -> int:
    """
    Versión generadora para iterar por los nodos de la lista enlazada.
    
    :param A: Lista de enteros.
    :return: Cantidad total de nodos.
    """
    def _nodes(arr):
        idx = 0
        while idx != -1:
            yield idx
            idx = arr[idx]
    return sum(1 for _ in _nodes(A))

if __name__ == "__main__":
    assert solution([1, 4, -1, 3, 2]) == 4
    assert solution_pythonic([1, 4, -1, 3, 2]) == 4

    assert solution([-1]) == 1
    assert solution_pythonic([-1]) == 1

    print("[OK] Todas las pruebas de arr-list-len pasaron exitosamente.")
