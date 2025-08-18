import pandas as pd
# CARGA DE DATOS DESDE ARCHIVOS
# Cargar archivo CSV
df_csv = pd.read_csv("LigaEspanola2023-2024-Resultados.csv")

# Cargar archivo Excel
df_excel = pd.read_excel("liga_datos.xlsx")

# Mostrar primeras 5 filas
print("CSV:")
print(df_csv.head())
print("\nExcel:")
print(df_excel.head())

# Verificar tipos de datos y valores nulos
print("\nTipos de datos CSV:")
print(df_csv.dtypes)
print("\nValores nulos CSV:")
print(df_csv.isnull().sum())

print("\nTipos de datos Excel:")
print(df_excel.dtypes)
print("\nValores nulos Excel:")
print(df_excel.isnull().sum())
# MANEJO Y TRANSFORMACION DE DATOS
# Selección de columnas relevantes
df_csv = df_csv[["Fecha", "EquipoLocal", "EquipoVisitante", "GolesLocal", "GolesVisitante", "Resultado"]]
df_excel = df_excel[["Equipo", "Temporada", "Goles", "Asistencias"]]

# Eliminar filas con nulos en columnas críticas
df_csv.dropna(subset=["Fecha", "EquipoLocal", "EquipoVisitante"], inplace=True)
df_excel.dropna(subset=["Equipo", "Temporada"], inplace=True)

# Convertir tipo de datos
df_csv["Fecha"] = pd.to_datetime(df_csv["Fecha"])
df_excel["Temporada"] = df_excel["Temporada"].astype(str)
#LECTURA DE DATOS DESDE LA WEB
# Extraer tabla web
url = "https://cosmocode.io/automation-practice-webtable/"
df_web = pd.read_html(url)[0]

# Verificar estructura y seleccionar columnas
print("\nTabla Web:")
print(df_web.head())

df_web = df_web[["Country", "Capital", "Currency"]]
df_web.rename(columns={"Country": "País", "Capital": "Capital", "Currency": "Moneda"}, inplace=True)
#EXPORTACION DE DATOS
# Exportar CSV sin índice
df_csv.to_csv("LigaEspanola_Limpio.csv", index=False)

# Exportar Excel con múltiples hojas
with pd.ExcelWriter("Datos_Exportados.xlsx") as writer:
    df_csv.to_excel(writer, sheet_name="Resultados", index=False)
    df_excel.to_excel(writer, sheet_name="Estadísticas", index=False)
    df_web.to_excel(writer, sheet_name="TablaWeb", index=False)

# Exportar a JSON y Parquet
df_csv.to_json("LigaEspanola_Limpio.json", orient="records")
df_csv.to_parquet("LigaEspanola_Limpio.parquet", index=False)
#AUTOMATIZACION CON FUNCIONES
def cargar_y_limpiar_csv(ruta):
    df = pd.read_csv(ruta)
    df = df[["Fecha", "EquipoLocal", "EquipoVisitante", "GolesLocal", "GolesVisitante", "Resultado"]]
    df.dropna(subset=["Fecha", "EquipoLocal", "EquipoVisitante"], inplace=True)
    df["Fecha"] = pd.to_datetime(df["Fecha"])
    return df

def cargar_y_limpiar_excel(ruta):
    df = pd.read_excel(ruta)
    df = df[["Equipo", "Temporada", "Goles", "Asistencias"]]
    df.dropna(subset=["Equipo", "Temporada"], inplace=True)
    df["Temporada"] = df["Temporada"].astype(str)
    return df
