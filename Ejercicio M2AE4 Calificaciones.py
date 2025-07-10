# Definir una lista con al menos 8 calificaciones
calificaciones = [85, 72, 90, 58, 63, 45, 100, 77]

# Variables para acumular total y contar aprobados
total = 0
aprobados = 0
notas_aprobadas = []

# Recorrer calificaciones, sumar total y contar aprobados
for nota in calificaciones:
    total += nota  # acumulamos la nota
    if nota >= 60:  # condición de aprobado
        aprobados += 1
        notas_aprobadas.append(nota)  # guardamos nota aprobada

# Calcular promedio y mostrar resultados
promedio = total / len(calificaciones)

# Mostrar resultados
print("Promedio general:", promedio)
print("Cantidad de estudiantes aprobados:", aprobados)
print("Lista de notas aprobadas:", notas_aprobadas)
