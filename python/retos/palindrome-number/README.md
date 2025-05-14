# Solución para Verificar si una Cadena es un Palíndromo

Se generaron tres implementaciones para resolver el problema de verificar si una cadena de texto es un **palíndromo**. Un palíndromo es una palabra, frase o secuencia que se lee igual de izquierda a derecha que de derecha a izquierda, ignorando espacios, símbolos y diferencias entre mayúsculas y minúsculas. Cada implementación está diseñada para ser clara y eficiente.

## Descripción del Problema

Dada una cadena de texto, el objetivo es determinar si es un **palíndromo**.

### Ejemplo

Entrada:
```python
s = "A man, a plan, a canal: Panama"
```

Salida:
```python
True
```

---

Entrada:
```python
s = "race a car"
```

Salida:
```python
False
```

---

## Implementaciones

### 1. Función `solution`

Esta es una implementación clara y detallada que utiliza un bucle para comparar los caracteres de la cadena desde los extremos hacia el centro. Es ideal para estudiantes que comienzan a programar, ya que explica cada paso del proceso.

### 2. Función `solution_pythonic`

Esta es una implementación compacta y expresiva que utiliza el operador `:=` (walrus operator) para limpiar y comparar la cadena con su versión invertida. Es adecuada para programadores familiarizados con las características modernas de Python.

### 3. Función `solution_pythonic_2`

Esta es una implementación igualmente compacta pero más tradicional que limpia la cadena y la compara con su versión invertida, sin utilizar el operador `:=`. Es ideal para quienes prefieren escribir código más directo.

---

## Cómo Ejecutar el Código

1. Asegúrate de tener Python instalado en tu sistema (versión 3.11 o superior).
2. Copia cualquiera de las funciones (`solution`, `solution_pythonic` o `solution_pythonic_2`) en un archivo Python (por ejemplo, `main.py`).
3. Ejecuta el archivo desde la terminal o tu entorno de desarrollo preferido.
4. Prueba cada función utilizando los casos de prueba proporcionados para validar el comportamiento del código.

### Casos de Prueba

**Ejemplo 1:**
```python
# Entrada:
s = "A man, a plan, a canal: Panama"
# Salida Esperada:
True
```

**Ejemplo 2:**
```python
# Entrada:
s = "race a car"
# Salida Esperada:
False
```

**Ejemplo 3:**
```python
# Entrada:
s = " "
# Salida Esperada:
True
```


Este desafío es ideal para practicar conceptos básicos como manejo de cadenas, expresiones regulares y comparaciones, así como para explorar diferentes estilos de programación en Python.