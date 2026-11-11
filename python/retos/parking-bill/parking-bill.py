"""
Solución para el Cálculo de Tarifa de Estacionamiento (Parking Bill).
"""

def solution(E: str, L: str) -> int:
    """
    Calcula el costo del estacionamiento a partir de las horas HH:MM.
    
    :param E: Hora de entrada ("HH:MM").
    :param L: Hora de salida ("HH:MM").
    :return: Costo total entero.
    """
    e_h, e_m = map(int, E.split(':'))
    l_h, l_m = map(int, L.split(':'))

    total_minutes = (l_h * 60 + l_m) - (e_h * 60 + e_m)
    # Redondeo hacia arriba: cualquier fracción de hora cuenta como hora completa
    total_hours = (total_minutes + 59) // 60

    if total_hours <= 0:
        return 2
    return 2 + 3 + (total_hours - 1) * 4

def solution_pythonic(E: str, L: str) -> int:
    """
    Versión alternativa usando aritmética directa de minutos.
    
    :param E: Hora de entrada.
    :param L: Hora de salida.
    :return: Costo total.
    """
    t_in = int(E[:2]) * 60 + int(E[3:])
    t_out = int(L[:2]) * 60 + int(L[3:])
    hours = -(-(t_out - t_in) // 60) # ceil division entera
    return 2 + 3 + max(0, hours - 1) * 4

if __name__ == "__main__":
    assert solution("10:00", "13:21") == 17
    assert solution_pythonic("10:00", "13:21") == 17

    assert solution("09:42", "11:42") == 9
    assert solution_pythonic("09:42", "11:42") == 9

    assert solution("10:00", "10:05") == 5
    assert solution_pythonic("10:00", "10:05") == 5

    print("[OK] Todas las pruebas de parking-bill pasaron exitosamente.")
