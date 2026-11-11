"""
Solución para el Problema de FizzBuzz Extensible.
"""

def solution(n: int) -> list:
    """
    Genera la secuencia FizzBuzz de 1 a n usando condicionales if/elif/else.
    
    :param n: Límite superior entero positivo.
    :return: Lista de strings con la secuencia.
    """
    result = []
    for num in range(1, n + 1):
        # Paso 1: Evaluamos primero la condición combinada (múltiplo de 3 y 5 = 15).
        if num % 15 == 0:
            result.append("FizzBuzz")
        elif num % 3 == 0:
            result.append("Fizz")
        elif num % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(num))
    return result


def solution_pythonic(n: int) -> list:
    """
    Genera la secuencia FizzBuzz utilizando un mapeo de reglas extensible.
    
    :param n: Límite superior entero positivo.
    :return: Lista de strings con la secuencia.
    """
    # Paso 1: Reglas definidas como pares (divisor, palabra).
    # Se pueden agregar más reglas sin tocar la lógica de abajo.
    rules = ((3, "Fizz"), (5, "Buzz"))
    result = []
    
    # Paso 2: Iteramos sobre el rango.
    for num in range(1, n + 1):
        output = "".join(word for divisor, word in rules if num % divisor == 0)
        result.append(output or str(num))
        
    return result


if __name__ == "__main__":
    assert solution(5) == ["1", "2", "Fizz", "4", "Buzz"]
    assert solution_pythonic(5) == ["1", "2", "Fizz", "4", "Buzz"]

    expected_15 = [
        "1", "2", "Fizz", "4", "Buzz",
        "Fizz", "7", "8", "Fizz", "Buzz",
        "11", "Fizz", "13", "14", "FizzBuzz"
    ]
    assert solution(15) == expected_15
    assert solution_pythonic(15) == expected_15

    assert solution(1) == ["1"]
    assert solution_pythonic(1) == ["1"]

    print("[OK] Todas las pruebas de fizz-buzz pasaron exitosamente.")
