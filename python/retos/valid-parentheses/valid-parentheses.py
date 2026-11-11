"""
Solución para Validar Paréntesis y Signos de Agrupación Balanceados.
"""

def solution(s: str) -> bool:
    """
    Verifica si una cadena de corchetes, paréntesis y llaves está balanceada
    utilizando una lista como pila (stack) y condicionales explícitos.
    
    :param s: Cadena de texto con caracteres (), [], {}.
    :return: True si la cadena está balanceada, False en caso contrario.
    """
    # Paso 1: Si la longitud es impar, es imposible que todos los símbolos tengan pareja.
    if len(s) % 2 != 0:
        return False
        
    # Paso 2: Creamos una lista vacía que funcionará como pila (LIFO).
    stack = []
    
    # Paso 3: Recorremos cada carácter de la cadena.
    for char in s:
        # Si es un carácter de apertura, lo añadimos a la pila.
        if char in ('(', '[', '{'):
            stack.append(char)
        # Si es de cierre, verificamos si la pila no está vacía y si coincide con el tope.
        elif char == ')':
            if not stack or stack.pop() != '(':
                return False
        elif char == ']':
            if not stack or stack.pop() != '[':
                return False
        elif char == '}':
            if not stack or stack.pop() != '{':
                return False
                
    # Paso 4: Si al finalizar la pila quedó completamente vacía, la cadena es válida.
    return len(stack) == 0


def solution_pythonic(s: str) -> bool:
    """
    Verifica si una cadena de corchetes y paréntesis está balanceada
    utilizando un diccionario de mapeo y una pila compacta.
    
    :param s: Cadena de texto con caracteres (), [], {}.
    :return: True si la cadena está balanceada, False en caso contrario.
    """
    # Paso 1: Mapeamos cada símbolo de cierre con su apertura correspondiente.
    mapping = {')': '(', ']': '[', '}': '{'}
    stack = []
    
    # Paso 2: Recorremos cada carácter en la cadena.
    for char in s:
        # Si el carácter es una llave de cierre (clave del diccionario):
        if char in mapping:
            # Extraemos el elemento superior de la pila si existe, de lo contrario usamos un valor ficticio.
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            # Si es un símbolo de apertura, lo apilamos.
            stack.append(char)
            
    # Paso 3: La cadena es válida si y solo si la pila está vacía al terminar.
    return not stack


if __name__ == "__main__":
    assert solution("()") is True
    assert solution_pythonic("()") is True

    assert solution("()[]{}") is True
    assert solution_pythonic("()[]{}") is True

    assert solution("(]") is False
    assert solution_pythonic("(]") is False

    assert solution("([{}])") is True
    assert solution_pythonic("([{}])") is True

    assert solution("([)]") is False
    assert solution_pythonic("([)]") is False

    assert solution("{[]}") is True
    assert solution_pythonic("{[]}") is True

    assert solution("") is True
    assert solution_pythonic("") is True

    assert solution("(((") is False
    assert solution_pythonic("(((") is False

    print("[OK] Todas las pruebas de valid-parentheses pasaron exitosamente.")
