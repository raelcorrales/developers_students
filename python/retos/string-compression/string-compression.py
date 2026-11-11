"""
Solución para Compresión de Cadenas (Run-Length Encoding).
"""

from itertools import groupby

def solution(s: str) -> str:
    """
    Comprime una cadena contando repeticiones consecutivas.
    Si la versión comprimida no es estrictamente más corta, devuelve la original.
    
    :param s: Cadena de texto de entrada.
    :return: Cadena comprimida o la original si no se reduce la longitud.
    """
    # Paso 1: Si la cadena está vacía o tiene un solo carácter, no se puede comprimir más.
    if len(s) <= 1:
        return s

    compressed_parts = []
    count = 1

    # Paso 2: Recorremos desde el segundo carácter hasta el final.
    for i in range(1, len(s)):
        # Si el carácter actual es igual al anterior, incrementamos el contador.
        if s[i] == s[i - 1]:
            count += 1
        else:
            # Si cambia de carácter, guardamos el anterior y su frecuencia.
            compressed_parts.append(f"{s[i - 1]}{count}")
            count = 1

    # Paso 3: Agregamos el último bloque acumulado.
    compressed_parts.append(f"{s[-1]}{count}")

    # Paso 4: Unimos las partes.
    compressed = "".join(compressed_parts)

    # Paso 5: Devolvemos la comprimida solo si es estrictamente más corta que la original.
    return compressed if len(compressed) < len(s) else s


def solution_pythonic(s: str) -> str:
    """
    Comprime una cadena utilizando itertools.groupby.
    
    :param s: Cadena de texto de entrada.
    :return: Cadena comprimida o la original si no se reduce la longitud.
    """
    if len(s) <= 1:
        return s

    # Paso 1: groupby agrupa caracteres consecutivos idénticos.
    compressed = "".join(f"{char}{len(list(group))}" for char, group in groupby(s))

    # Paso 2: Comparamos las longitudes.
    return compressed if len(compressed) < len(s) else s


if __name__ == "__main__":
    assert solution("aabcccccaaa") == "a2b1c5a3"
    assert solution_pythonic("aabcccccaaa") == "a2b1c5a3"

    assert solution("abcd") == "abcd"
    assert solution_pythonic("abcd") == "abcd"

    assert solution("") == ""
    assert solution_pythonic("") == ""

    assert solution("a") == "a"
    assert solution_pythonic("a") == "a"

    assert solution("wwwwaaadexxxxxx") == "w4a3d1e1x6"
    assert solution_pythonic("wwwwaaadexxxxxx") == "w4a3d1e1x6"

    print("[OK] Todas las pruebas de string-compression pasaron exitosamente.")
