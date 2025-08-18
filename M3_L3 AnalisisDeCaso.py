import pandas as pd

# Cargar archivo CSV
df_csv = pd.read_csv("liga_espanola.csv")

# Cargar archivo Excel
df_excel = pd.read_excel("liga_datos.xlsx")

# Extraer tabla web
url = "https://cosmocode.io/automation-practice-webtable/"
df_web = pd.read_html(url)[0]
# Verificar nulos
print(df_csv.isnull().sum())

# Eliminar duplicados
df_csv = df_csv.drop_duplicates()

# Ajustar tipos de datos
df_csv["Puntos"] = pd.to_numeric(df_csv["Puntos"], errors="coerce")
df_csv["Equipo"] = df_csv["Equipo"].astype("category")
# Verificar nulos
print(df_excel.isnull().sum())

# Imputar valores nulos si es necesario
df_excel.fillna(method="ffill", inplace=True)

# Ajustar tipos
df_excel["Temporada"] = df_excel["Temporada"].astype(str)
# Verificar nulos
print(df_web.isnull().sum())

# Eliminar duplicados
df_web = df_web.drop_duplicates()

# Ajustar tipos
df_web["Country"] = df_web["Country"].astype("category")
df_csv = df_csv[["Equipo", "Puntos", "Posición"]]
df_excel = df_excel[["Equipo", "Temporada", "Goles"]]
df_web = df_web[["Country", "Capital", "Currency"]]
df_csv.rename(columns={"Equipo": "Club", "Puntos": "Pts", "Posición": "Rank"}, inplace=True)
df_excel.rename(columns={"Equipo": "Club", "Temporada": "Season", "Goles": "Goals"}, inplace=True)
df_web.rename(columns={"Country": "País", "Capital": "Capital", "Currency": "Moneda"}, inplace=True)
df_csv.sort_values(by="Pts", ascending=False, inplace=True)
df_excel.sort_values(by="Goals", ascending=False, inplace=True)
df_web.sort_values(by="País", inplace=True)
# Guardar CSV sin índice
df_csv.to_csv("liga_espanola_limpio.csv", index=False)

# Exportar a Excel
with pd.ExcelWriter("datos_procesados.xlsx") as writer:
    df_csv.to_excel(writer, sheet_name="Liga", index=False)
    df_excel.to_excel(writer, sheet_name="Complemento", index=False)
    df_web.to_excel(writer, sheet_name="TablaWeb", index=False)
    