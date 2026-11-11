"""
Solución para el Problema de Suma de Dos Números (Two Sum).
"""

def solution(nums: list, target: int) -> list:
    """
    Encuentra dos índices en la lista `nums` cuyos valores sumen `target`.
    Utiliza el enfoque clásico de fuerza bruta comparando cada par posible.
    
    :param nums: Lista de números enteros.
    :param target: Valor objetivo que deben sumar los dos números.
    :return: Lista con los dos índices encontrados o [] si no hay solución.
    """
    n = len(nums)
    # Paso 1: Recorremos cada elemento con un bucle exterior.
    for i in range(n):
        # Paso 2: Recorremos los elementos posteriores con un bucle interior.
        for j in range(i + 1, n):
            # Paso 3: Verificamos si la suma de ambos números es igual al objetivo.
            if nums[i] + nums[j] == target:
                return [i, j]
                
    # Paso 4: Si terminamos ambos bucles sin coincidencias, devolvemos [].
    return []


def solution_pythonic(nums: list, target: int) -> list:
    """
    Encuentra dos índices en la lista `nums` cuyos valores sumen `target`.
    Utiliza un diccionario (tabla hash) para resolver el problema en una sola pasada O(n).
    
    :param nums: Lista de números enteros.
    :param target: Valor objetivo que deben sumar los dos números.
    :return: Lista con los dos índices encontrados o [] si no hay solución.
    """
    # Paso 1: Creamos un diccionario para almacenar los números visitados como claves
    # y sus índices como valores.
    seen = {}
    
    # Paso 2: Recorremos la lista obteniendo simultáneamente el índice y el valor con enumerate.
    for index, num in enumerate(nums):
        # Paso 3: Calculamos el complemento necesario para alcanzar el target.
        complement = target - num
        
        # Paso 4: Si el complemento ya está en el diccionario, encontramos el par.
        if complement in seen:
            return [seen[complement], index]
            
        # Paso 5: Si no está, guardamos el número actual y su posición.
        seen[num] = index
        
    # Paso 6: Si no hay solución, devolvemos una lista vacía.
    return []


if __name__ == "__main__":
    # Pruebas de validación
    assert solution([2, 7, 11, 15], 9) == [0, 1]
    assert solution_pythonic([2, 7, 11, 15], 9) == [0, 1]

    assert solution([3, 2, 4], 6) == [1, 2]
    assert solution_pythonic([3, 2, 4], 6) == [1, 2]

    assert solution([3, 3], 6) == [0, 1]
    assert solution_pythonic([3, 3], 6) == [0, 1]

    assert solution([1, 2, 3], 10) == []
    assert solution_pythonic([1, 2, 3], 10) == []

    print("[OK] Todas las pruebas de two-sum pasaron exitosamente.")
