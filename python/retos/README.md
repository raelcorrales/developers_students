# 🎯 Retos de Programación en Python

Este directorio contiene una colección de **ejercicios y desafíos** de programación, clasificados por niveles de dificultad.

Cada reto está documentado con su respectivo enunciado, ejemplos y (cuando aplique) una solución. Puedes:

- Leer el enunciado en formato Markdown.
- Probar tu propia solución.
- Comparar tu solución con la de otros en los Pull Requests.

---

## 📂 Estructura de cada reto

Cada reto cuenta con su propia carpeta con documentación y código ejecutable:

```text
retos/
└── <nombre-del-reto>/
    ├── README.md               → Explicación teórica, análisis y casos de prueba
    ├── <nombre-del-reto>.py    → Implementación en script ejecutable con pruebas (asserts)
    └── <nombre-del-reto>.ipynb → Notebook interactivo con análisis de tiempo (timeit)
```

---

## 📋 Catálogo de Retos Disponibles

### 🟢 Nivel Básico
| Reto | Temas Clave | Origen / Enfoque | Archivos |
| :--- | :--- | :--- | :---: |
| [**fizz-buzz**](./fizz-buzz/) | Condicionales, Reglas extensibles con tuplas | Lógica inicial vs OCP | `README.md`, `.py`, `.ipynb` |
| [**fizz-buzz-sum**](./fizz-buzz-sum/) | Múltiplos, Acumuladores, Divisibilidad | Google Interview | `README.md`, `.py`, `.ipynb` |
| [**is-leap-year**](./is-leap-year/) | Operadores lógicos, Aritmética modular | Lógica de calendario | `README.md`, `.py`, `.ipynb` |
| [**factorial-formula**](./factorial-formula/) | Bucles iterativos, Recursión, `math.factorial` | Microsoft Interview | `README.md`, `.py`, `.ipynb` |
| [**contains-duplicate**](./contains-duplicate/) | Detección de duplicados, `set()` vs búsqueda lineal | Apple Interview | `README.md`, `.py`, `.ipynb` |
| [**two-sum**](./two-sum/) | Listas, Tablas Hash, Bucle doble vs Diccionario | LeetCode / Clásico | `README.md`, `.py`, `.ipynb` |
| [**palindrome-number**](./palindrome-number/) | Cadenas, Punteros, Expresiones Regulares, Slicing | Clásico | `README.md`, `.py`, `.ipynb` |
| [**valid-parentheses**](./valid-parentheses/) | Pilas (Stack LIFO), Diccionarios de mapeo | Estructuras de datos | `README.md`, `.py`, `.ipynb` |
| [**anagram-checker**](./anagram-checker/) | Cadenas, `Counter`, `sorted()`, Frecuencias | Clásico | `README.md`, `.py`, `.ipynb` |
| [**string-compression**](./string-compression/) | Recorrido de strings, RLE, `itertools.groupby` | Algoritmos de compresión | `README.md`, `.py`, `.ipynb` |
| [**merge-sorted-lists**](./merge-sorted-lists/) | Dos Punteros (*Two Pointers*), `heapq.merge` | Algoritmos / MergeSort | `README.md`, `.py`, `.ipynb` |
| [**intersection-of-two-lists**](./intersection-of-two-lists/) | Operaciones de conjuntos (`&`), Intersección | Apple Interview | `README.md`, `.py`, `.ipynb` |
| [**arr-list-len**](./arr-list-len/) | Simulación de listas enlazadas en arreglos | Codility | `README.md`, `.py`, `.ipynb` |
| [**parking-bill**](./parking-bill/) | Parsing de strings `"HH:MM"`, Tarifas por tramos | Codility | `README.md`, `.py`, `.ipynb` |

### 🟡 Nivel Intermedio
| Reto | Temas Clave | Origen / Enfoque | Archivos |
| :--- | :--- | :--- | :---: |
| [**binary-search**](./binary-search/) | Divide y vencerás, $O(\log n)$, módulo `bisect` | Algoritmos de búsqueda | `README.md`, `.py`, `.ipynb` |
| [**binary-gap**](./binary-gap/) | Representación binaria, Conteo de secuencias | Codility | `README.md`, `.py`, `.ipynb` |
| [**collatz-sequence-steps**](./collatz-sequence-steps/) | Conjetura $3n+1$, Bucles, Generadores | Bloomberg Interview | `README.md`, `.py`, `.ipynb` |
| [**flatten-list**](./flatten-list/) | Recursividad, Generadores (`yield from`), Listas | Manipulación anidada | `README.md`, `.py`, `.ipynb` |
| [**first-unique**](./first-unique/) | Listas, Frecuencias, Diccionarios vs `Counter` | Codility | `README.md`, `.py`, `.ipynb` |
| [**roman-to-integer**](./roman-to-integer/) | Cadenas, Pares de resta, Lectura inversa | Palantir Interview | `README.md`, `.py`, `.ipynb` |
| [**longest-password**](./longest-password/) | RegEx, Conteo condicional de paridad | Codility | `README.md`, `.py`, `.ipynb` |

### 🔴 Nivel Avanzado
| Reto | Temas Clave | Origen / Enfoque | Archivos |
| :--- | :--- | :--- | :---: |
| [**arithmetic-triplets**](./arithmetic-triplets/) | Búsqueda exhaustiva $O(n^3)$ vs Hashing $O(n)$ | Oracle Interview | `README.md`, `.py`, `.ipynb` |
| [**maximum-sum-of-matrix**](./maximum-sum-of-matrix/) | Matrices $N \times N$, Permutaciones sin colisión | Stripe Interview | `README.md`, `.py`, `.ipynb` |
| [**select-candidate-skills**](./select-candidate-skills/) | Cobertura de conjuntos (Set Cover), Combinatoria | Optimización | `README.md`, `.py`, `.ipynb` |

---

## 🎓 ¿Cómo funciona este repositorio?

1. Se propone un ejercicio mediante un **Issue**.
2. Se toma un ejercicio del **Issue**, se resuelve y se sube en un **Pull Request**.
3. Una vez revisado y aprobado, se integra al repositorio como contenido educativo con sus diferentes implementaciones (didáctica vs *pythonic*) y medición de rendimiento (`timeit`).

> Este repositorio **no es solo un banco de ejercicios para resolver**, sino una colección de **ejemplos explicados paso a paso para aprender**.