"""
Solución para Encontrar el Primer Número Único en una Lista.
"""

from collections import Counter

def solution(list_numbers: list) -> int:
    """
    Dada una lista `list_numbers` de N enteros, encuentra el primer entero único en ella.
    Un número único es aquel que aparece exactamente una vez en la lista.
    
    :param list_numbers: Lista de enteros.
    :return: El primer entero único en la lista o -1 si no hay ninguno.
    """
    # Paso 1: Verificamos si la lista está vacía.
    if not list_numbers:
        return -1

    # Paso 2: Creamos un diccionario para contar las ocurrencias de cada número.
    unique_numbers = {}
    for num in list_numbers:
        unique_numbers[num] = unique_numbers.get(num, 0) + 1

    # Paso 3: Recorremos la lista original nuevamente para preservar el orden de aparición.
    for num in list_numbers:
        if unique_numbers[num] == 1:
            return num

    # Paso 4: Si no encontramos ningún número único, devolvemos -1.
    return -1


def solution_pythonic(list_numbers: list) -> int:
    """
    Dada una lista list_numbers de N enteros, encuentra el primer entero único en ella
    utilizando collections.Counter.
    
    :param list_numbers: Lista de enteros.
    :return: El primer entero único en la lista o -1 si no hay ninguno.
    """
    # Paso 1: Verificamos si la lista está vacía.
    if not list_numbers:
        return -1

    # Paso 2: Usamos Counter para contar cuántas veces aparece cada número en la lista.
    unique_numbers = Counter(list_numbers)
    
    # Paso 3: Recorremos la lista original en el mismo orden.
    for number in list_numbers:
        if unique_numbers[number] == 1:
            return number
            
    # Paso 4: Si no hay números únicos, devolvemos -1.
    return -1


if __name__ == "__main__":
    assert solution([1, 1, 2, 2, 3, 4, 5]) == 3
    assert solution_pythonic([1, 1, 2, 2, 3, 4, 5]) == 3

    assert solution([1, 1, 2, 3, 3, 4]) == 2
    assert solution_pythonic([1, 1, 2, 3, 3, 4]) == 2

    assert solution([]) == -1
    assert solution_pythonic([]) == -1

    assert solution([10, 20, 30]) == 10
    assert solution_pythonic([10, 20, 30]) == 10

    print("[OK] Todas las pruebas de first-unique pasaron exitosamente.")
