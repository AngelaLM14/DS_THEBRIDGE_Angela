import numpy as np
import pandas as pd

def lista_columnas(dataframe): 
    columnas = dataframe.columns.to_list()
    return columnas


def encuentra_duplicados(dataframe):
    duplicados = dataframe[dataframe.duplicated(keep=False)] 
    cantidad_duplicados = len(duplicados)
    print("Cantidad de filas duplicadas:",cantidad_duplicados)
    return duplicados


def indices_y_categoricas(dataframe): 
    posibles_indices = []
    posibles_categóricas = []
    umbral_categorica = 10 
    for col in dataframe:
        cardinalidad = dataframe[col].nunique()/len(dataframe) * 100
        if cardinalidad == 100:
            posibles_indices.append(col)
        elif cardinalidad < umbral_categorica:
            posibles_categóricas.append(col)
    print(f"Posibles índices: {','.join(posibles_indices)}")
    print(f"Posibles categóricas: {','.join(posibles_categóricas)}")


def cardinalidad_lista_col(dataframe, lista_col):
    for col in lista_col:
        cardinalidad = dataframe[col].nunique()/len(dataframe)*100
        print(f"Cardinalidad de {col}: ",cardinalidad, "; nunique:", dataframe[col].nunique()) 


def porcentaje_sin_valor_por_columna(dataframe):
    porcentajes_por_columna = (dataframe == "(Sin valor)").sum() / len(dataframe) * 100
    return porcentajes_por_columna


def reemplazar_nulos_con_moda(dataframe, columna):
    moda = dataframe[columna].mode()[0]
    dataframe[columna].fillna(moda, inplace=True)
    return dataframe


def convertir_a_fecha(dataframe, nombre_columna):
    dataframe[nombre_columna] = pd.to_datetime(dataframe[nombre_columna], errors='coerce')
    return dataframe


def convertir_a_float(dataframe, nombre_columna):
    dataframe[nombre_columna] = pd.to_numeric(dataframe[nombre_columna], errors='coerce')
    return dataframe

def reemplazar_nulos_con_media(dataframe, columna):
    media = dataframe[columna].mean()
    dataframe[columna].fillna(media, inplace=True)
    return dataframe

def card_tipo(df,umbral_categoria = 10, umbral_continua = 30):
    # Primera parte: Preparo el dataset con cardinalidades, % variación cardinalidad, y tipos
    df_temp = pd.DataFrame([df.nunique(), df.nunique()/len(df) * 100, df.dtypes]) # Cardinaliad y porcentaje de variación de cardinalidad
    df_temp = df_temp.T # Como nos da los valores de las columnas en columnas, y quiero que estas sean filas, la traspongo
    df_temp = df_temp.rename(columns = {0: "Card", 1: "%_Card", 2: "Tipo"}) # Cambio el nombre de la transposición anterior para que tengan más sentido, y uso asignación en vez de inplace = True (esto es arbitrario para el tamaño de este dataset)

    # Corrección para cuando solo tengo un valor
    df_temp.loc[df_temp.Card == 1, "%_Card"] = 0.00

    # Creo la columna de sugerenica de tipo de variable, empiezo considerando todas categóricas pero podría haber empezado por cualquiera, siempre que adapte los filtros siguientes de forma correspondiente
    df_temp["tipo_sugerido"] = "Categorica"
    df_temp.loc[df_temp["Card"] == 2, "tipo_sugerido"] = "Binaria"
    df_temp.loc[df_temp["Card"] >= umbral_categoria, "tipo_sugerido"] = "Numerica discreta"
    df_temp.loc[df_temp["%_Card"] >= umbral_continua, "tipo_sugerido"] = "Numerica continua"
    return df_temp