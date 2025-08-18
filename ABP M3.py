#Lección 1: La librería NumPy
#Objetivo: Crear datos ficticios de clientes y transacciones
import numpy as np

# 1. Generar datos ficticios
np.random.seed(42)
clientes = np.array(["C001", "C002", "C003", "C004", "C005"])
montos = np.random.randint(1000, 5000, size=5)
fechas = np.array(["2025-01-10", "2025-01-12", "2025-01-15", "2025-01-18", "2025-01-20"])

# 2. Operaciones básicas
print("Suma:", np.sum(montos))
print("Media:", np.mean(montos))
print("Conteo:", len(montos))

# 3. Guardar como .npy
np.save("datos_numpy.npy", montos)

# 4. Convertir a lista para Pandas
datos_numpy = list(zip(clientes, fechas, montos))
#Explica que NumPy es eficiente por su uso de arrays homogéneos, 
# operaciones vectorizadas y bajo consumo de memoria

#lección 2: La librería Pandas
#Objetivo: Convertir y explorar los datos de NumPy
import pandas as pd

# 1. Convertir a DataFrame
df = pd.DataFrame(datos_numpy, columns=["ID_Cliente", "Fecha", "Monto"])

# 2. Exploración
print(df.head())
print(df.tail())
print(df.describe())
print(df[df["Monto"] > 3000])

# 3. Guardar CSV
df.to_csv("datos_clientes.csv", index=False)
#Describe cómo Pandas facilita la manipulación tabular, 
# filtrado condicional y exportación

#Lección 3: Obtención desde archivos
#Objetivo: Integrar CSV, Excel y tabla web
# 1. Cargar CSV
df_csv = pd.read_csv("datos_clientes.csv")

# 2. Cargar Excel
df_excel = pd.read_excel("datos_complementarios.xlsx")

# 3. Cargar tabla web
url = "https://cosmocode.io/automation-practice-webtable/"
df_web = pd.read_html(url)[0]

# 4. Unificar
df_total = pd.concat([df_csv, df_excel], ignore_index=True)
#Explica diferencias en formatos, encoding, 
# estructura y cómo se resolvieron

#Lección 4: Manejo de nulos y outliers
#Objetivo: Limpiar el DataFrame consolidado
# 1. Identificar nulos
print(df_total.isnull().sum())

# 2. Imputación
df_total["Monto"].fillna(df_total["Monto"].mean(), inplace=True)

# 3. Outliers con IQR
Q1 = df_total["Monto"].quantile(0.25)
Q3 = df_total["Monto"].quantile(0.75)
IQR = Q3 - Q1
lim_inf = Q1 - 1.5 * IQR
lim_sup = Q3 + 1.5 * IQR
df_total["Monto"] = np.where(df_total["Monto"] < lim_inf, lim_inf,
                      np.where(df_total["Monto"] > lim_sup, lim_sup, df_total["Monto"]))
#Justifica imputación y tratamiento de outliers para mejorar 
# calidad analítica

#Lección 5: Data Wrangling
#Objetivo: Transformar y enriquecer los datos

# 1. Eliminar duplicados
df_total.drop_duplicates(inplace=True)

# 2. Transformar tipos
df_total["Fecha"] = pd.to_datetime(df_total["Fecha"])

# 3. Nuevas columnas
df_total["Mes"] = df_total["Fecha"].dt.month
df_total["Monto_USD"] = df_total["Monto"] * 0.0011

# 4. Funciones personalizadas
df_total["Segmento"] = df_total["Monto"].apply(lambda x: "Alto" if x > 4000 else "Medio" if x > 2500 else "Bajo")

#Explica cómo estas transformaciones enriquecen el análisis 
# y preparan el dataset para modelos
# 1. Agrupamiento
agrupado = df_total.groupby("Segmento").agg({
    "Monto": ["mean", "sum", "count"]
})

# 2. Pivot
pivot = pd.pivot_table(df_total, values="Monto", index="Mes", columns="Segmento", aggfunc="mean")

# 3. Melt
melted = pd.melt(df_total, id_vars=["ID_Cliente"], value_vars=["Monto", "Monto_USD"])

# 4. Merge con otra fuente
df_bonos = pd.DataFrame({"ID_Cliente": ["C001", "C003"], "Bono": [500, 700]})
df_final = pd.merge(df_total, df_bonos, on="ID_Cliente", how="left")

# 5. Exportar
df_final.to_csv("dataset_final.csv", index=False)
df_final.to_excel("dataset_final.xlsx", index=False)
#Describe todo el flujo, decisiones tomadas, problemas resueltos y cómo el dataset final 
# está listo para análisis predictivo o visualización



