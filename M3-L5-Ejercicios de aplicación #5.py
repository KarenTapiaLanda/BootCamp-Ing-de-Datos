import pandas as pd
#CARGA Y EXPLORACION DEL DATASET
# Importar el CSV
df = pd.read_csv("datos_originales.csv")

# a.ii. Mostrar las primeras 5 filas y descripción general
print(df.head())
print(df.describe(include='all'))

# a.iii. Identificar valores nulos y tipos de datos
print(df.info())
print(df.isnull().sum())
#ORDENAMIENTO Y MANIPULACION DE DATOS
# b.i. Ordenar por Edad y Goles (descendente)
df_sorted = df.sort_values(by=["Edad", "Goles"], ascending=False)

# b.ii. Permutación aleatoria
df_shuffled = df.sample(frac=1, random_state=42)

# b.iii. Selección de columnas relevantes
df_selected = df[["Nombre", "Edad", "Goles", "Posición"]]
#DETECCION Y ELIMINACION DE DUPLICADOS
# c.i. Identificar duplicados
duplicados = df.duplicated()
print("Duplicados encontrados:", duplicados.sum())

# c.ii. Eliminar duplicados
df_sin_duplicados = df.drop_duplicates()
print("Tamaño original:", len(df))
print("Tamaño sin duplicados:", len(df_sin_duplicados))
#REEMPLAZO DE VALORES Y DISCRETIZACION
# d.i. Reemplazar valores inconsistentes en 'Posición'
df["Posición"] = df["Posición"].fillna("Sin posición")

# d.ii. Binning de Edad en rangos
df["Rango_Edad"] = pd.cut(df["Edad"], bins=[20,25,30,35], labels=["Joven","Adulto","Veterano"])
#ENRIQUECIMIENTO DE DATOS
# e.i. Nueva columna: IMC = Peso / Altura²
df["IMC"] = df["Peso"] / (df["Altura"] ** 2)

# e.ii. Función personalizada para clasificar rendimiento
def clasificar_rendimiento(goles):
    if pd.isna(goles):
        return "Desconocido"
    elif goles >= 15:
        return "Alto"
    elif goles >= 8:
        return "Medio"
    else:
        return "Bajo"

df["Rendimiento"] = df["Goles"].apply(clasificar_rendimiento)

# e.iii. Lambda para abreviar nombres de equipos
df["Equipo_Corto"] = df["Equipo"].apply(lambda x: x.split()[0])
#MANIPULACION DE ESTRUCTURA
# f.i. Agregar columna y eliminar otra
df["Altura_cm"] = df["Altura"] * 100
df.drop(columns=["Altura"], inplace=True)

# f.ii. Redimensionar: jugadores con Edad > 25 y Goles > 5
df_sub = df[(df["Edad"] > 25) & (df["Goles"] > 5)]

# f.iii. Renombrar columnas
df.rename(columns={"Peso": "Peso_kg", "Edad": "Edad_años"}, inplace=True)
#eXPORTACION DE DATOS
# g.i. Guardar en CSV y Excel
df.to_csv("datos_transformados.csv", index=False)
df.to_excel("datos_transformados.xlsx", index=False)
