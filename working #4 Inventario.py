import csv

# Diccionario inicial de inventario
inventario = {}

# 1. Función para agregar productos al inventario
def agregar_producto(nombre, cantidad, precio, categoria):
    inventario[nombre] = {'cantidad': cantidad, 'precio': precio, 'categoria': categoria}

# 2. Función para eliminar productos del inventario
def eliminar_producto(nombre):
    if nombre in inventario:
        del inventario[nombre]
    else:
        print("El producto no existe en el inventario.")

# 3. Función para actualizar cantidad y/o precio de productos
def actualizar_producto(nombre, cantidad=None, precio=None):
    if nombre in inventario:
        if cantidad is not None:
            inventario[nombre]['cantidad'] = cantidad
        if precio is not None:
            inventario[nombre]['precio'] = precio
    else:
        print("El producto no existe en el inventario.")

# 4. Función para listar productos de una categoría específica
def listar_por_categoria(categoria):
    print(f"Productos en la categoría '{categoria}':")
    encontrados = False
    for nombre, detalles in inventario.items():
        if detalles['categoria'] == categoria:
            print(f"  Producto: {nombre}, Cantidad: {detalles['cantidad']}, Precio: {detalles['precio']}")
            encontrados = True
    if not encontrados:
        print("  No se encontraron productos en esta categoría.")

# 5. Función para calcular el valor total del inventario
def calcular_valor_total():
    valor_total = sum(detalles['cantidad'] * detalles['precio'] for detalles in inventario.values())
    return valor_total

# 6. Función para exportar el inventario a un archivo CSV
def exportar_inventario_csv(nombre_archivo):
    with open(nombre_archivo, 'w', newline='') as archivo_csv:
        campos = ['Producto', 'Cantidad', 'Precio', 'Categoría']
        writer = csv.writer(archivo_csv)
        writer.writerow(campos)
        for nombre, detalles in inventario.items():
            writer.writerow([nombre, detalles['cantidad'], detalles['precio'], detalles['categoria']])
    print(f"Inventario exportado a {nombre_archivo}")

# === EJEMPLO DE USO ===

# Agregar productos
agregar_producto("Laptop", 10, 700, "Electrónica")
agregar_producto("Manzana", 50, 0.5, "Alimentos")
agregar_producto("Auriculares", 30, 25, "Electrónica")

# Eliminar un producto (descomenta si deseas probar)
# eliminar_producto("Auriculares")

# Actualizar un producto
actualizar_producto("Laptop", cantidad=8, precio=680)

# Listar por categoría
listar_por_categoria("Electrónica")

# Calcular valor total
print("\nValor total del inventario:", calcular_valor_total())

# Exportar a CSV
exportar_inventario_csv("inventario.csv")
