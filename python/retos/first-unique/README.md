# Solución para Encontrar el Primer Número Único en una Lista

Se generaron dos implementaciones para resolver el problema de encontrar el primer número único en una lista de enteros. Un número único es aquel que aparece exactamente una vez en la lista. Ambas implementaciones están diseñadas para manejar listas de diferentes tamaños y escenarios.

## Descripción del Problema

Dada una lista de enteros, el objetivo es encontrar el **primer número único** en la lista. Si no hay números únicos, la función debe devolver `-1`.

### Ejemplo

Entrada:
```python
[1, 1, 2, 2, 3, 4, 5]
```

Salida:
```python
3
```

## Implementaciones

### 1. Función `solution`

Esta es una implementación básica y clara que utiliza un diccionario para contar las ocurrencias de cada número en la lista. Luego, recorre la lista original para encontrar el primer número único.

### 2. Función `solution_pythonic`

Esta es una implementación intermedia y usando los paquetes y modulos que tenemos a nuestra disposicion, que utiliza un collections.Counter para contar las ocurrencias de cada número en la lista. Luego, recorre la lista original para encontrar el primer número único.

---

## Cómo Ejecutar el Código

1. Asegúrate de tener Python instalado en tu sistema (versión 3.6 o superior).
2. Copia cualquiera de las funciones (`solution` o `solution_pythonic`) en un archivo Python (por ejemplo, `main.py`).
3. Ejecuta el archivo desde la terminal o tu entorno de desarrollo preferido.
4. Puedes modificar o añadir más casos de prueba para validar el comportamiento del código.

