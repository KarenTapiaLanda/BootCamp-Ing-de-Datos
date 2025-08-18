import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#CARGA Y EXPLORACION DEL DATASET
# Cargar dataset
df = pd.read_csv("datos_originales.csv")

# Primeras 5 filas
print(df.head())

# Descripción general
print(df.describe(include="all"))

# Tipos de datos y valores nulos
print(df.dtypes)
print(df.isnull().sum())
#MANEJO DE VALORES PERDIDOS
# Imputación numérica
for col in df.select_dtypes(include=np.number).columns:
    df[col + "_media"] = df[col].fillna(df[col].mean())
    df[col + "_mediana"] = df[col].fillna(df[col].median())
    df[col + "_moda"] = df[col].fillna(df[col].mode()[0])

# Imputación categórica
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].fillna(df[col].mode()[0])

# Evaluar eliminación de filas con nulos
df_sin_nulos = df.dropna()
print(f"Filas originales: {len(df)}, sin nulos: {len(df_sin_nulos)}")
#DETECCION Y TRATAMIENTO DE OUTLIERS
def detectar_outliers_iqr(columna):
    Q1 = df[columna].quantile(0.25)
    Q3 = df[columna].quantile(0.75)
    IQR = Q3 - Q1
    outliers = df[(df[columna] < Q1 - 1.5 * IQR) | (df[columna] > Q3 + 1.5 * IQR)]
    return outliers

# Ejemplo con una columna
outliers_goles = detectar_outliers_iqr("Goles")
print(outliers_goles)
#VISUALIZACION CON BOXPLOT
sns.boxplot(x=df["Goles"])
plt.title("Boxplot de Goles")
plt.show()
#ESTRATEGIA DE TRATAMIENTO
# 1. Eliminación
df_filtrado = df[~df.index.isin(outliers_goles.index)]

# 2. Sustitución con límites
Q1 = df["Goles"].quantile(0.25)
Q3 = df["Goles"].quantile(0.75)
IQR = Q3 - Q1
lim_inf = Q1 - 1.5 * IQR
lim_sup = Q3 + 1.5 * IQR
df["Goles_limpios"] = np.where(df["Goles"] < lim_inf, lim_inf,
                        np.where(df["Goles"] > lim_sup, lim_sup, df["Goles"]))

# 3. Transformación logarítmica
df["Goles_log"] = np.log1p(df["Goles"])
#VALIDACION DATOS LIMPIOS
# Verificar nulos
print(df.isnull().sum())

# Distribución post-limpieza
sns.histplot(df["Goles_limpios"], kde=True)
plt.title("Distribución de Goles Limpios")
plt.show()
#EXPORTACION DATASET LIMPIO
df.to_csv("datos_limpios.csv", index=False)
