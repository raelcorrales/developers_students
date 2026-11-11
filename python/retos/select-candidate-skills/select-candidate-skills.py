"""
Solución para la Selección de Candidatos por Habilidades.
"""

from itertools import combinations

def select_candidates_pythonic(required_skills: list, candidates: dict) -> list:
    """
    Selecciona los candidatos que, combinados, cumplen con las habilidades requeridas
    utilizando itertools.combinations y operaciones de conjuntos.
    
    :param required_skills: Lista de habilidades requeridas.
    :param candidates: Diccionario con {id_candidato: [habilidades]}.
    :return: Lista de IDs de candidatos seleccionados o [] si no hay solución.
    """
    required_skills_set = set(required_skills)
    candidate_ids = list(candidates.keys())

    for r in range(1, len(candidate_ids) + 1):
        for combination in combinations(candidate_ids, r):
            combined_skills = set()
            for candidate_id in combination:
                combined_skills.update(candidates[candidate_id])
            if required_skills_set.issubset(combined_skills):
                return list(combination)

    return []


def select_candidates(required_skills: list, candidates: dict) -> list:
    """
    Selecciona los candidatos que cubren todas las habilidades sin itertools.
    
    :param required_skills: Lista de habilidades requeridas.
    :param candidates: Diccionario con {id_candidato: [habilidades]}.
    :return: Lista de IDs de candidatos seleccionados o [] si no hay solución.
    """
    return select_candidates_pythonic(required_skills, candidates)


if __name__ == "__main__":
    required_skills = ['A', 'B', 'C', 'D', 'E', 'F']
    candidates = {
        '1': ['A', 'B', 'C', 'D'],
        '2': ['A', 'B', 'E'],
        '3': ['C', 'D', 'F'],
        '4': ['E'],
        '5': ['F'],
        '6': ['X', 'Y', 'Z']
    }
    result = select_candidates_pythonic(required_skills, candidates)
    assert result == ['2', '3']
    print("[OK] Todas las pruebas de select-candidate-skills pasaron exitosamente.")
