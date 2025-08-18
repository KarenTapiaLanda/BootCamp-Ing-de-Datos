import pandas as pd
#CARGA Y EXPLORACION DE DATOS
# Cargar el dataset
df = pd.read_csv("datos_empresa.csv")

# Inspección inicial
print(df.head())
print(df.info())
print(df.describe(include="all"))

# Identificación de nulos y duplicados
print("Valores nulos por columna:")
print(df.isnull().sum())

print("Duplicados encontrados:", df.duplicated().sum())
#Este paso permite entender la estructura del dataset, 
# detectar problemas de calidad y preparar estrategias de limpieza

#LIMPIEZA Y TRANSFORMACION DE DATOS
# Imputación de valores numéricos
for col in df.select_dtypes(include="number"):
    df[col].fillna(df[col].mean(), inplace=True)

# Imputación de valores categóricos
for col in df.select_dtypes(include="object"):
    df[col].fillna(df[col].mode()[0], inplace=True)

# Eliminación de duplicados
df.drop_duplicates(inplace=True)

# Conversión de columnas categóricas a numéricas (ejemplo: género)
df["Genero_Num"] = df["Genero"].map({"Masculino": 1, "Femenino": 0})
#La imputación evita pérdida de información. 
# La codificación numérica permite usar variables categóricas en modelos analíticos

#OPTIMIZACION Y ESTRUCTURACION
# Agrupamiento por departamento y cálculo de métricas
resumen = df.groupby("Departamento").agg({
    "Salario": ["mean", "max", "min"],
    "Edad": "median"
})

# Filtrado: empleados con salario mayor a 1.5 veces el promedio
salario_promedio = df["Salario"].mean()
df_filtrado = df[df["Salario"] > 1.5 * salario_promedio]

# Renombrar columnas para claridad
df.rename(columns={
    "Nombre": "Empleado",
    "Salario": "Salario_Mensual",
    "Edad": "Edad_Años"
}, inplace=True)
#Agrupar y filtrar permite generar reportes estratégicos. 
# Renombrar mejora la legibilidad para usuarios no técnicos

#EXPORTACION DE DATOS
# Exportar CSV sin índice
df.to_csv("datos_empresa_limpios.csv", index=False)

# Exportar a Excel
df.to_excel("datos_empresa_limpios.xlsx", index=False)
#Exportar en formatos estándar permite 
# compartir resultados con otros equipos o integrarlos en dashboards