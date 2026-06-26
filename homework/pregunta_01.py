"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""
import os

import pandas as pd


def load_data(input_file):

    df = pd.read_csv(input_file, sep=";", index_col=0)
    return df


def clean_data(df):

    df = df.copy()

    df = df.dropna()

    for col in ["sexo", "tipo_de_emprendimiento", "idea_negocio", "línea_credito"]:
        df[col] = df[col].str.lower().str.strip()

    for col in ["idea_negocio", "línea_credito"]:
        df[col] = (
            df[col]
            .str.replace("-", " ", regex=False)
            .str.replace("_", " ", regex=False)
            .str.replace(r"\s+", " ", regex=True)
            .str.strip()
        )

    df["barrio"] = (
        df["barrio"]
        .str.lower()
        .str.replace("-", " ", regex=False)
        .str.replace("_", " ", regex=False)
    )

    df["monto_del_credito"] = (
        df["monto_del_credito"]
        .str.replace(r"[\$,\s]", "", regex=True)
        .str.replace(r"\.00$", "", regex=True)
        .str.replace(".", "", regex=False)
        .astype(float)
        .astype(int)
    )

    f1 = pd.to_datetime(df["fecha_de_beneficio"], format="%d/%m/%Y", errors="coerce")
    f2 = pd.to_datetime(df["fecha_de_beneficio"], format="%Y/%m/%d", errors="coerce")
    df["fecha_de_beneficio"] = f1.fillna(f2)

    df["comuna_ciudadano"] = df["comuna_ciudadano"].astype(int)

    df = df.drop_duplicates()

    return df


def save_data(df, output_file):

    df = df.copy()
    df.to_csv(output_file, sep=";", index=False)


def pregunta_01():

    archivo_entrada = "files/input/solicitudes_de_credito.csv"
    archivo_salida = "files/output/solicitudes_de_credito.csv"

    df = load_data(archivo_entrada)
    df = clean_data(df)

    os.makedirs("files/output", exist_ok=True)
    save_data(df, archivo_salida)

    return df
