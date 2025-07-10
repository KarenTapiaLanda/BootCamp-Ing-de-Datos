class AnalizadorFinanciero:
# Calcula el total de ingresos en una lista de transacciones
    def calcular_total_ingresos(self, transacciones):
        total = 0
        for ingreso in transacciones:
            total += ingreso
        return total
# Filtra y retorna solo los ingresos mayores a un umbral dado
def filtrar_ingresos_altos(self, transacciones, umbral):
    ingresos_altos = []
    for ingreso in transacciones:
        if ingreso > umbral:
            ingresos_altos.append(ingreso)
    return ingresos_altos
# Agrupa ingresos en un diccionario por categorías
def agrupar_por_categoria(self, transacciones, categorias):
    agrupado = {}
    for categoria, ingreso in zip(categorias, transacciones):
        if categoria in agrupado:
            agrupado[categoria].append(ingreso)
        else:
            agrupado[categoria] = [ingreso]
    return agrupado
transacciones = [1000, 500, 1200, 700, 300]
categorias = ['sueldo', 'freelance', 'sueldo', 'inversiones', 'freelance']
af = AnalizadorFinanciero()

assert af.calcular_total_ingresos(transacciones) == 3700
assert af.filtrar_ingresos_altos(transacciones, 800) == [1000, 1200]
assert af.agrupar_por_categoria(transacciones, categorias) == {
    'sueldo': [1000, 1200],
    'freelance': [500, 300],
    'inversiones': [700]
}
