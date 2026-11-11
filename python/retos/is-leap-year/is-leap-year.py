"""
Solución para Determinar si un Año es Bisiesto.
"""

import calendar

def solution(year: int) -> bool:
    """
    Determina si un año es bisiesto usando condicionales explícitos.
    
    :param year: Año entero.
    :return: True si es bisiesto, False en caso contrario.
    """
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    return False

def solution_pythonic(year: int) -> bool:
    """
    Determina si un año es bisiesto usando expresión lógica directa o calendar.isleap.
    
    :param year: Año entero.
    :return: True si es bisiesto, False en caso contrario.
    """
    return calendar.isleap(year)

if __name__ == "__main__":
    assert solution(2000) is True
    assert solution_pythonic(2000) is True

    assert solution(1900) is False
    assert solution_pythonic(1900) is False

    assert solution(2024) is True
    assert solution_pythonic(2024) is True

    assert solution(2023) is False
    assert solution_pythonic(2023) is False

    print("[OK] Todas las pruebas de is-leap-year pasaron exitosamente.")
