"""
Solución para Conversión de Números Romanos a Enteros.
"""

def solution(s: str) -> int:
    """
    Convierte un número romano en entero usando lectura hacia adelante con verificación de pares.
    
    :param s: Cadena con número romano válido.
    :return: Entero equivalente.
    """
    rom = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    i = 0
    n = len(s)

    while i < n:
        if i + 1 < n and rom[s[i + 1]] > rom[s[i]]:
            total += rom[s[i + 1]] - rom[s[i]]
            i += 2
        else:
            total += rom[s[i]]
            i += 1

    return total

def solution_pythonic(s: str) -> int:
    """
    Convierte un número romano en entero mediante recorrido inverso.
    
    :param s: Cadena con número romano válido.
    :return: Entero equivalente.
    """
    rom = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    prev_val = 0

    for char in reversed(s):
        curr_val = rom[char]
        if curr_val < prev_val:
            total -= curr_val
        else:
            total += curr_val
        prev_val = curr_val

    return total

if __name__ == "__main__":
    assert solution("III") == 3
    assert solution_pythonic("III") == 3

    assert solution("LVIII") == 58
    assert solution_pythonic("LVIII") == 58

    assert solution("MCMXCIV") == 1994
    assert solution_pythonic("MCMXCIV") == 1994

    assert solution("LXIX") == 69
    assert solution_pythonic("LXIX") == 69

    print("[OK] Todas las pruebas de roman-to-integer pasaron exitosamente.")
