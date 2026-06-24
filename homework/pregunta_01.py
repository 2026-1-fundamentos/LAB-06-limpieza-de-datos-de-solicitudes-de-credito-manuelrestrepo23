"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""
import os
import pandas as pd

def load_data(input_file):
    df = pd.read_csv(input_file, sep=";")
    return df


def clean_data(df):
    df = df.copy()
    df = df.drop(columns=["Unnamed: 0"])
    df = df.drop_duplicates()
    df = df.dropna()

    df["sexo"] = df["sexo"].str.strip().str.lower()

    df["tipo_de_emprendimiento"] = df["tipo_de_emprendimiento"].str.strip().str.lower()

    df["idea_negocio"] = df["idea_negocio"].str.strip().str.lower()

    df["barrio"] = df["barrio"].str.strip().str.lower()

    df["línea_credito"] = df["línea_credito"].str.strip().str.lower()
    df["línea_credito"] = df["línea_credito"].str.replace(" ", "_", regex=False)
    df["línea_credito"] = df["línea_credito"].str.replace("-", "_", regex=False)
    df["línea_credito"] = df["línea_credito"].str.replace(".", "_", regex=False)
    df["línea_credito"] = df["línea_credito"].str.replace(r"_+$", "", regex=True)
    df["línea_credito"] = df["línea_credito"].str.replace(r"_+", "_", regex=True)

    df["monto_del_credito"] = df["monto_del_credito"].str.replace("$", "", regex=False)
    df["monto_del_credito"] = df["monto_del_credito"].str.replace(",", "", regex=False)
    df["monto_del_credito"] = df["monto_del_credito"].str.replace(".", "", regex=False)
    df["monto_del_credito"] = df["monto_del_credito"].str.strip()
    df["monto_del_credito"] = df["monto_del_credito"].astype(int)

    df["fecha_de_beneficio"] = pd.to_datetime(
        df["fecha_de_beneficio"],
        format="mixed",
        dayfirst=True,
    )
    df["fecha_de_beneficio"] = df["fecha_de_beneficio"].dt.strftime("%Y-%m-%d")

    df["comuna_ciudadano"] = df["comuna_ciudadano"].astype(int)

    df = df.drop_duplicates()

    return df


def save_data(df, output_file):

    df = df.copy()
    df.to_csv(output_file, index=False)
def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """
    archivo_entrada = "files/input/solicitudes_de_credito.csv"
    archivo_salida = "files/output/solicitudes_de_credito.csv"

    df = load_data(archivo_entrada)
    df = clean_data(df)

    os.makedirs("files/output", exist_ok=True)
    save_data(df, archivo_salida)

    return df
