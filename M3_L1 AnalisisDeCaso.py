import numpy as np

# Datos simulados: 5 acciones (filas) y 5 días de cotización (columnas)
precios = np.array([
    [100, 102, 105, 107, 110],  # Acción A
    [50, 52, 51, 53, 55],       # Acción B
    [200, 198, 202, 205, 210],  # Acción C
    [30, 32, 31, 33, 34],       # Acción D
    [75, 77, 76, 78, 80]        # Acción E
])
'''
Matriz 5x5 permite representar precios diarios de cada accion
facilitando el analisis por filas(acciones) y Columnas(dias)
'''
promedio = np.mean(precios, axis=1)
maximo = np.max(precios, axis=1)
minimo = np.min(precios, axis=1)
'''
Calcula Metricas por fila (accion). esto permite evaluar el rendimiento
general de cada activo
'''

variacion = np.diff(precios, axis=1) / precios[:, :-1] * 100
'''
Calcula la diferencia entre dias consecutivos. Dividir por el valor
anterior y multiplicar por 100 da la variacion porcentual
'''

logaritmo = np.log(precios)
exponencial = np.exp(precios)
'''
El Logaritmo ayuda a analizar retornos compuestos. La exponencial
puede modelar crecimiento continuo.
'''

min_val = np.min(precios, axis=1, keepdims=True)
max_val = np.max(precios, axis=1, keepdims=True)
normalizado = (precios - min_val) / (max_val - min_val)
'''
Normalizar permite comparar acciones en escalas distintas
mantiene la forma para broadcasting
'''
rendimiento_C_dia3 = precios[2, 2] 
# Indexación directa permite extraer datos específicos sin recorrer la matriz.
precios_aumento = precios * 1.05
#Broadcasting aplica la operación a todo el array sin bucles, optimizando el rendimiento.

'''
NumPy mejora significativamente la eficiencia en análisis financiero.
Permite cálculos rápidos, precisos y escalables.
Su sintaxis clara y operaciones vectorizadas reducen la complejidad del código.
Ideal para entornos donde se requiere procesamiento en tiempo real.
'''