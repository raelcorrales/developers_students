# Code Challenge: Selección de Candidatos por Habilidades

Este repositorio contiene un desafío para resolver el problema de seleccionar el menor número de candidatos que cubran todas las habilidades necesarias para un proyecto, a partir de un conjunto de candidatos con diferentes habilidades.

## Descripción del Problema

Dado:
1. Un diccionario donde las claves representan los nombres de los candidatos y los valores son listas de habilidades que posee cada candidato.
2. Una lista de habilidades requeridas para un proyecto.

El objetivo es seleccionar el **menor número de candidatos** que cubran todas las habilidades necesarias.

### Ejemplo

**Entrada:**
```python
required_skills = ['A', 'B', 'C', 'D', 'E', 'F']
candidates = {
    '1': ['A', 'B', 'C', 'D'],
    '2': ['A', 'B', 'E'],
    '3': ['C', 'D', 'F'],
    '4': ['E'],
    '5': ['F'],
    '6': ['X', 'Y', 'Z']  # Candidato con habilidades irrelevantes
}
```

**Salida Esperada:**
```python
['2', '3']
```

---

## Implementación

La solución debe implementarse como una función que reciba dos parámetros:
1. `candidates`: Un diccionario donde las claves son los nombres de los candidatos y los valores son listas de habilidades.
2. `required_skills`: Una lista de habilidades necesarias para el proyecto.

La función debe devolver una lista con los nombres de los candidatos seleccionados que cubran todas las habilidades requeridas.

## Cómo Ejecutar el Código

1. Asegúrate de tener Python instalado en tu sistema (versión 3.6 o superior).
2. Copia la implementación de la función `select_candidates` en un archivo Python (por ejemplo, `main.py`).
3. Utiliza los casos de prueba proporcionados para validar la funcionalidad.
