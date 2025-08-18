import pandas as pd
#CARGA Y EXPLORACION DEL DATASET
# i. Importar el dataset
df = pd.read_csv("datos_empresa.csv")

# ii. Mostrar las primeras 5 filas y descripción general
print(df.head())
print(df.describe(include='all'))

# iii. Verificar valores nulos y tipos de datos
print("\nValores nulos por columna:")
print(df.isnull().sum())

print("\nTipos de datos:")
print(df.dtypes)

#AGRUPAMIENTO DE DATOS
# i. Agrupar por 'Departamento' y calcular métricas
grupo = df.groupby("Departamento")

# ii. Promedio, suma y cantidad por grupo
print("\nPromedio por departamento:")
print(grupo["Salario"].mean())

print("\nSuma por departamento:")
print(grupo["Salario"].sum())

print("\nCantidad de empleados por departamento:")
print(grupo["ID"].count())

# iii. Función personalizada con .agg()
estadisticas = grupo.agg({
    "Salario": ["mean", "sum", "max"],
    "Antigüedad": lambda x: x.mean() if x.notnull().any() else None
})
print("\nEstadísticas personalizadas:")
print(estadisticas)

#PIVOTADO Y DESPIVOTADO
# i. Tabla dinámica: promedio de salario por departamento y género
pivot = pd.pivot_table(df, values="Salario", index="Departamento", columns="Genero", aggfunc="mean")
print("\nTabla dinámica:")
print(pivot)

# ii. Despivotar con melt()
melted = pd.melt(df, id_vars=["ID", "Nombre"], value_vars=["Edad", "Salario", "Antigüedad"])
print("\nDataFrame despivotado:")
print(melted.head())

#COMBINACION Y FUSION DE DATOS
# i. Concatenar dos DataFrames (simulamos una división por antigüedad)
df1 = df[df["Antigüedad"] <= 3]
df2 = df[df["Antigüedad"] > 3]
df_concat = pd.concat([df1, df2])
print("\nDataFrame concatenado:")
print(df_concat.shape)

# ii. Fusión con merge()
# Creamos un DataFrame auxiliar con bonificaciones
bonos = pd.DataFrame({
    "ID": [1, 2, 3, 4, 5],
    "Bono": [50000, 60000, 55000, 52000, 58000]
})

# Merge tipo inner
df_merge_inner = pd.merge(df, bonos, on="ID", how="inner")
print("\nMerge INNER:")
print(df_merge_inner.head())

# Merge tipo left
df_merge_left = pd.merge(df, bonos, on="ID", how="left")
print("\nMerge LEFT:")
print(df_merge_left.head())

#EXPORTACIN DE DATOS
# i. Guardar en CSV y Excel
df_merge_left.to_csv("datos_empresa_transformado.csv", index=False)
df_merge_left.to_excel("datos_empresa_transformado.xlsx", index=False)
print("✅ Archivos exportados con éxito.")