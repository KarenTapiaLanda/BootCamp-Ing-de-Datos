import numpy as np
#1. Creación y Manipulación de Arrays
# Array unidimensional de 20 enteros aleatorios entre 1 y 100
array = np.random.randint(1, 101, size=20)

# Operaciones básicas
suma = np.sum(array)
promedio = np.mean(array)
maximo = np.max(array)
minimo = np.min(array)

# Ordenamiento
ascendente = np.sort(array)
descendente = np.sort(array)[::-1]

# Valores pares
pares = array[array % 2 == 0]

# Reemplazo de impares por -1
array_modificado = np.where(array % 2 != 0, -1, array)
'''
Se refleja como NumPy simplifica el procesamiento de datos
con funciones vectorizadas y filtros logicos.
'''
#2.Operaciones con Matrices
# Dos matrices 4x4 con enteros aleatorios entre 1 y 50
matriz1 = np.random.randint(1, 51, size=(4, 4))
matriz2 = np.random.randint(1, 51, size=(4, 4))

# Suma, resta y multiplicación matricial
suma_matrices = matriz1 + matriz2
resta_matrices = matriz1 - matriz2
multiplicacion_matrices = np.matmul(matriz1, matriz2)

# Transpuesta de la primera matriz
transpuesta = matriz1.T

# Determinante e inversa de la segunda matriz
determinante = np.linalg.det(matriz2)
inversa = np.linalg.inv(matriz2) if np.linalg.det(matriz2) != 0 else "No invertible"
'''
NumPy Permite realizar algebra lineal con precision y eficiencia.
La verificacion del determinante evita errores al calcular la inversa
'''
#3. Aplicacion de funciones NumPy
# Array de 100 valores uniformemente distribuidos entre 0 y 10
valores = np.linspace(0, 10, 100)

# Funciones trigonométricas
seno = np.sin(valores)
coseno = np.cos(valores)

# Exponencial
exponencial = np.exp(valores)

# Raíz cuadrada de elementos > 5
raices = np.sqrt(valores[valores > 5])
'''
Estas funciones son utiles en modelado matematico, simulaciones
y analisis de señales. NumPy las aplica de forma vectorizada
'''
#4. Modularizacion de Operaciones
def operaciones_basicas(arr):
    return np.sum(arr), np.mean(arr), np.max(arr), np.min(arr)

def filtrar_pares(arr):
    return arr[arr % 2 == 0]

def reemplazar_impares(arr):
    return np.where(arr % 2 != 0, -1, arr)

def operaciones_matriciales(m1, m2):
    suma = m1 + m2
    resta = m1 - m2
    producto = np.matmul(m1, m2)
    return suma, resta, producto

def analisis_matriz(m):
    transpuesta = m.T
    determinante = np.linalg.det(m)
    inversa = np.linalg.inv(m) if determinante != 0 else None
    return transpuesta, determinante, inversa
'''
Modularizar permite reutilizar codigo, probar con diferentes tamaños
y escalar el analisis facilmente.
'''
'''
Análisis y Experimentación
Probar con matrices 10x10 o 100x100 revela cómo NumPy mantiene eficiencia incluso con grandes volúmenes.
Aplicar estas funciones a datasets reales (por ejemplo, precios de acciones, sensores, etc.) permite extraer métricas clave rápidamente.
Comparado con listas y bucles, NumPy reduce el tiempo de ejecución y mejora la legibilidad del código.
'''