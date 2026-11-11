"""
Solución para Verificar si una Cadena es un Palíndromo.
"""

import re

def solution(s: str) -> bool:
    """
    Verifica si una cadena de texto es un palíndromo comparando caracteres desde los extremos.
    
    :param s: Cadena de texto a evaluar.
    :return: True si es palíndromo, False en caso contrario.
    """
    # Paso 1: Conservar solo caracteres alfanuméricos.
    s = re.sub(r'[^a-zA-Z0-9]', '', s)
    
    # Paso 2: Convertir a minúsculas.
    s = s.lower()

    # Paso 3: Comparar caracteres de los extremos hacia el centro.
    for i in range(len(s) // 2):
        left = i
        right = (i + 1) * -1
        if s[left] != s[right]:
            return False

    return True


def solution_pythonic(s: str) -> bool:
    """
    Verifica si una cadena es palíndromo utilizando expresiones regulares y slicing inverso.
    
    :param s: Cadena de texto a evaluar.
    :return: True si es palíndromo, False en caso contrario.
    """
    cleaned = re.sub(r'\W+', '', s).lower()
    return cleaned == cleaned[::-1]


def solution_pythonic_2(s: str) -> bool:
    """
    Verifica si una cadena es palíndromo limpiando con filtro alfanumérico y comparando con su inverso.
    
    :param s: Cadena de texto a evaluar.
    :return: True si es palíndromo, False en caso contrario.
    """
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    assert solution("A man, a plan, a canal: Panama") is True
    assert solution_pythonic("A man, a plan, a canal: Panama") is True
    assert solution_pythonic_2("A man, a plan, a canal: Panama") is True

    assert solution("race a car") is False
    assert solution_pythonic("race a car") is False
    assert solution_pythonic_2("race a car") is False

    assert solution(" ") is True
    assert solution_pythonic(" ") is True
    assert solution_pythonic_2(" ") is True

    print("[OK] Todas las pruebas de palindrome-number pasaron exitosamente.")
