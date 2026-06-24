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
    df = df.dropna()

    puntuacion = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

    df["sexo"] = df["sexo"].str.strip().str.lower()

    df["tipo_de_emprendimiento"] = df["tipo_de_emprendimiento"].str.strip().str.lower()
    df["tipo_de_emprendimiento"] = df["tipo_de_emprendimiento"].str.translate(
        str.maketrans(puntuacion, " " * len(puntuacion))
    )
    df["tipo_de_emprendimiento"] = (
        df["tipo_de_emprendimiento"].str.replace(r"\s+", " ", regex=True).str.strip()
    )

    df["idea_negocio"] = df["idea_negocio"].str.strip().str.lower()
    df["idea_negocio"] = df["idea_negocio"].str.translate(
        str.maketrans(puntuacion, " " * len(puntuacion))
    )
    df["idea_negocio"] = (
        df["idea_negocio"].str.replace(r"\s+", " ", regex=True).str.strip()
    )

    df["barrio"] = df["barrio"].str.strip().str.lower()
    df["barrio"] = df["barrio"].str.translate(
        str.maketrans(puntuacion, " " * len(puntuacion))
    )
    df["barrio"] = df["barrio"].str.replace(r"\s+", " ", regex=True).str.strip()

    df["línea_credito"] = df["línea_credito"].str.strip().str.lower()
    df["línea_credito"] = df["línea_credito"].str.replace(" ", "_", regex=False)
    df["línea_credito"] = df["línea_credito"].str.replace("-", "_", regex=False)
    df["línea_credito"] = df["línea_credito"].str.replace(".", "_", regex=False)
    df["línea_credito"] = df["línea_credito"].str.replace(r"_+", "_", regex=True)

    df["monto_del_credito"] = df["monto_del_credito"].str.replace("$", "", regex=False)
    df["monto_del_credito"] = df["monto_del_credito"].str.replace(",", "", regex=False)
    df["monto_del_credito"] = df["monto_del_credito"].str.strip()
    df["monto_del_credito"] = df["monto_del_credito"].astype(float).astype(int)

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
    df.to_csv(output_file, sep=";", index=False)


def pregunta_01():

    archivo_entrada = "files/input/solicitudes_de_credito.csv"
    archivo_salida = "files/output/solicitudes_de_credito.csv"

    df = load_data(archivo_entrada)
    df = clean_data(df)

    os.makedirs("files/output", exist_ok=True)
    save_data(df, archivo_salida)

    return df

if __name__ == "__main__":
    pregunta_01()