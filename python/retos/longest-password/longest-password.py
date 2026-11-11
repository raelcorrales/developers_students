"""
Solución para Encontrar la Contraseña Válida Más Larga (Longest Password).
"""

import re

def solution(S: str) -> int:
    """
    Encuentra la longitud de la contraseña válida más larga usando validación iterativa.
    
    :param S: Cadena con palabras separadas por espacios.
    :return: Longitud de la contraseña válida más larga o -1 si no hay ninguna.
    """
    words = S.split()
    longest = -1

    for word in words:
        if not re.fullmatch(r'[a-zA-Z0-9]+', word):
            continue
        letters = sum(1 for c in word if c.isalpha())
        digits = sum(1 for c in word if c.isdigit())
        if letters % 2 == 0 and digits % 2 == 1:
            if len(word) > longest:
                longest = len(word)

    return longest

def solution_pythonic(S: str) -> int:
    """
    Versión compacta con comprensión generadora y max().
    
    :param S: Cadena de palabras.
    :return: Longitud máxima o -1.
    """
    valid_lengths = [
        len(w) for w in S.split()
        if w.isalnum()
        and sum(1 for c in w if c.isalpha()) % 2 == 0
        and sum(1 for c in w if c.isdigit()) % 2 == 1
    ]
    return max(valid_lengths, default=-1)

if __name__ == "__main__":
    assert solution("test 5 a0A pass007 ?xy1") == 7
    assert solution_pythonic("test 5 a0A pass007 ?xy1") == 7

    assert solution("???") == -1
    assert solution_pythonic("???") == -1

    print("[OK] Todas las pruebas de longest-password pasaron exitosamente.")
