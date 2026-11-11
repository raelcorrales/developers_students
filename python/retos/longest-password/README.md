# Solución para Encontrar la Contraseña Válida Más Larga (Longest Password)

Se generaron dos implementaciones para encontrar la longitud de la contraseña válida más larga a partir de una cadena de palabras separadas por espacios. Ejercicio de Codility.

## Descripción del Problema

Dada una cadena `S` que contiene palabras separadas por espacios, una palabra es una contraseña válida si:
1. Contiene únicamente caracteres alfanuméricos (`a-z`, `A-Z`, `0-9`).
2. Contiene una cantidad **par** de letras.
3. Contiene una cantidad **impar** de dígitos.

Devuelve la longitud de la contraseña válida más larga, o `-1` si no existe ninguna.

### Ejemplo

Entrada: `S = "test 5 a0A pass007 ?xy1"`
- `test`: 4 letras (par), 0 dígitos (par -> no es impar). Inválida.
- `5`: 0 letras (par), 1 dígito (impar). Longitud 1. Válida.
- `a0A`: 2 letras (par), 1 dígito (impar). Longitud 3. Válida.
- `pass007`: 4 letras (par), 3 dígitos (impar). Longitud 7. Válida.
- `?xy1`: contiene `?`. Inválida.

Salida: `7` (correspondiente a `pass007`)
