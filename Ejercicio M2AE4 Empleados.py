#Crear un diccionario con al menos 5 empleados
empleados = {
    'emp1': {'nombre': 'Ana', 'edad': 28},
    'emp2': {'nombre': 'Luis', 'edad': 35},
    'emp3': {'nombre': 'María', 'edad': 42},
    'emp4': {'nombre': 'Carlos', 'edad': 25},
    'emp5': {'nombre': 'Sofía', 'edad': 31}
}

# Inicializamos lista y contador
menores_30 = []
total_empleados = 0

# Usar for con .items() para recorrer el diccionario
for clave, datos in empleados.items():
    nombre = datos['nombre']
    edad = datos['edad']
    total_empleados += 1  # Contamos cada empleado

    # Imprimir empleados mayores de 30 años
    if edad > 30:
        print(f"{nombre} tiene {edad} años (mayor de 30).")
    
    # Guardar nombres con edad < 30 en lista
    if edad < 30:
        menores_30.append(nombre)

# Mostrar resultados finales
print("\nNombres de empleados con menos de 30 años:", menores_30)
print("Cantidad total de empleados:", total_empleados)
