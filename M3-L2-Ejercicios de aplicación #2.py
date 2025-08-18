#1. Carga y Exportacion de Datos
import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv("mundial_2022_resultados.csv")

# Primeras y últimas 5 filas
print(df.head())
print(df.tail())

# Información general
print(df.info())

# Estadísticas descriptivas
print(df.describe(include='all'))
'''
Estas funciones permiten entender la estructura del dataset, 
detectar tipos de datos y posibles problemas como valores nulos o inconsistencias
'''
#2. Manejo de valores nulos y duplicados
# Identificar valores nulos
print(df.isnull().sum())

# Imputación de valores faltantes
for col in df.select_dtypes(include='number'):
    df[col].fillna(df[col].mean(), inplace=True)

for col in df.select_dtypes(include='object'):
    df[col].fillna(df[col].mode()[0], inplace=True)

# Eliminar duplicados
df.drop_duplicates(inplace=True)
'''
La imputación con media y moda mantiene la coherencia estadística. 
Eliminar duplicados evita sesgos en el análisis
'''
#3. Filtrado y Seleccion de datos
# Filtrar partidos con más de 3 goles
filtro = df[df["Goles_Totales"] > 3]

# Selección de columnas relevantes
df_relevante = df[["Equipo_Local", "Equipo_Visitante", "Goles_Local", "Goles_Visitante", "Fecha"]]

# Ordenar por goles del equipo local
df_ordenado = df.sort_values(by="Goles_Local", ascending=False)
'''
Filtrar y seleccionar permite enfocar el análisis en variables clave. 
Ordenar ayuda a detectar patrones o outliers
'''
#4:Agrupamiento y estadisticas
# Agrupar por equipo local y calcular promedio de goles
promedio_goles = df.groupby("Equipo_Local")["Goles_Local"].mean()

# Estadísticas agregadas por equipo visitante
estadisticas = df.groupby("Equipo_Visitante").agg({
    "Goles_Visitante": ["mean", "max", "min"],
    "Goles_Local": "sum"
})

# Función de agregación personalizada
def rango(goles):
    return goles.max() - goles.min()

rango_goles = df.groupby("Equipo_Local")["Goles_Local"].agg(rango)
'''
Agrupar permite comparar rendimiento entre equipos. 
Las funciones personalizadas enriquecen el análisis
'''
#5.Transformacion y Exportacion
# Nueva columna: diferencia de goles
df["Diferencia_Goles"] = df["Goles_Local"] - df["Goles_Visitante"]

# Conversión de tipo de datos
df["Fecha"] = pd.to_datetime(df["Fecha"])

# Renombrar columnas
df.rename(columns={"Equipo_Local": "Local", "Equipo_Visitante": "Visitante"}, inplace=True)

# Exportar a Excel y JSON
df.to_excel("Resultados_Liga_Espanola.xlsx", index=False)
df.to_json("Resultados_Liga_Espanola.json", orient="records")
'''
Transformar columnas permite crear nuevas métricas. Exportar facilita compartir 
resultados con otros equipos
'''
#6.Automatizacion con funciones
def limpiar_dataframe(df):
    df.drop_duplicates(inplace=True)
    for col in df.select_dtypes(include='number'):
        df[col].fillna(df[col].mean(), inplace=True)
    for col in df.select_dtypes(include='object'):
        df[col].fillna(df[col].mode()[0], inplace=True)
    return df

def agregar_diferencia_goles(df):
    df["Diferencia_Goles"] = df["Goles_Local"] - df["Goles_Visitante"]
    return df
'''
Automatizar tareas comunes mejora la eficiencia y 
reduce errores en flujos de trabajo repetitivos
'''