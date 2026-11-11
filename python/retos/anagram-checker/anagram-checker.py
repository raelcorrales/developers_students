"""
Solución para Verificar si Dos Cadenas son Anagramas.
"""

import re
from collections import Counter

def solution(s1: str, s2: str) -> bool:
    """
    Verifica si dos cadenas son anagramas utilizando diccionarios de frecuencias manuales.
    
    :param s1: Primera cadena de texto.
    :param s2: Segunda cadena de texto.
    :return: True si son anagramas, False en caso contrario.
    """
    # Paso 1: Limpiamos ambas cadenas conservando solo caracteres alfanuméricos en minúsculas.
    clean_s1 = re.sub(r'[^a-zA-Z0-9]', '', s1).lower()
    clean_s2 = re.sub(r'[^a-zA-Z0-9]', '', s2).lower()
    
    # Paso 2: Si tienen longitudes distintas, no pueden ser anagramas.
    if len(clean_s1) != len(clean_s2):
        return False
        
    # Paso 3: Contamos la frecuencia de cada carácter en la primera cadena.
    count = {}
    for char in clean_s1:
        count[char] = count.get(char, 0) + 1
        
    # Paso 4: Restamos la frecuencia con cada carácter de la segunda cadena.
    for char in clean_s2:
        if char not in count or count[char] == 0:
            return False
        count[char] -= 1
        
    return True


def solution_pythonic(s1: str, s2: str) -> bool:
    """
    Verifica si dos cadenas son anagramas utilizando Counter de collections.
    
    :param s1: Primera cadena de texto.
    :param s2: Segunda cadena de texto.
    :return: True si son anagramas, False en caso contrario.
    """
    # Paso 1: Limpiamos ambas cadenas conservando únicamente caracteres alfanuméricos.
    clean1 = re.sub(r'\W+', '', s1).lower()
    clean2 = re.sub(r'\W+', '', s2).lower()
    
    # Paso 2: Comparamos directamente los conteos de caracteres generados por Counter.
    return Counter(clean1) == Counter(clean2)


def solution_sorted(s1: str, s2: str) -> bool:
    """
    Verifica si dos cadenas son anagramas ordenando sus caracteres alfabéticamente.
    
    :param s1: Primera cadena de texto.
    :param s2: Segunda cadena de texto.
    :return: True si son anagramas, False en caso contrario.
    """
    # Paso 1: Limpiamos y ordenamos los caracteres alfabéticamente.
    clean1 = sorted(re.sub(r'\W+', '', s1).lower())
    clean2 = sorted(re.sub(r'\W+', '', s2).lower())
    
    # Paso 2: Verificamos si ambas listas ordenadas son exactamente iguales.
    return clean1 == clean2


if __name__ == "__main__":
    assert solution("listen", "silent") is True
    assert solution_pythonic("listen", "silent") is True
    assert solution_sorted("listen", "silent") is True

    assert solution("Amor", "Roma") is True
    assert solution_pythonic("Amor", "Roma") is True
    assert solution_sorted("Amor", "Roma") is True

    assert solution("A gentleman", "Elegant man") is True
    assert solution_pythonic("A gentleman", "Elegant man") is True
    assert solution_sorted("A gentleman", "Elegant man") is True

    assert solution("rat", "car") is False
    assert solution_pythonic("rat", "car") is False
    assert solution_sorted("rat", "car") is False

    assert solution("hello", "world") is False
    assert solution_pythonic("hello", "world") is False
    assert solution_sorted("hello", "world") is False

    print("[OK] Todas las pruebas de anagram-checker pasaron exitosamente.")
