#%%


# importamos las librerías que necesitamos

# Tratamiento de datos
# -----------------------------------------------------------------------
import pandas as pd
import numpy as np

# Visualización
# ------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import seaborn as sns

# Evaluar linealidad de las relaciones entre las variables
# y la distribución de las variables
# ------------------------------------------------------------------------------
import scipy.stats as stats
from scipy.stats import ttest_ind, norm, chi2_contingency, f_oneway

# Configuración
# -----------------------------------------------------------------------
pd.set_option('display.max_columns', None) # para poder visualizar todas las columnas de los DataFrames

# Gestión de los warnings
# -----------------------------------------------------------------------
import warnings
warnings.filterwarnings("ignore")

from unidecode import unidecode

def apertura_fichero(ruta):
    csv_apertura= pd.read_csv(ruta, index_col=0)
    csv_apertura.reset_index(inplace = True)
    display(csv_apertura.head())
    return csv_apertura


def exploracion_datos(csv):
    forma = csv.shape
    print(f"La forma es {forma}")
    print("_______________")
    nulos = csv.isna().sum().reset_index()
    print(f"Los nulos son:")
    display(nulos)
    print("_______________")
    duplicados = csv.duplicated().sum()
    print(f"Hay {duplicados} duplicados")
    print("_______________")
    tipo_dato = csv.dtypes.reset_index()
    print(f"Los datos son de tipo:")
    display(tipo_dato)
    print("_______________")
    columnas = csv.columns
    print(f"Las columnas son {columnas}")
# %%
def unificar(lines):
    lista_columnas = lines[0][0:-1].split(",")
    #print(lista_columnas)
    lista_productos = []
    for line in lines[1:-1]:
        split = line.split(",")
        join = ",".join(split[5:-1])
        all = split[0:5]
        all.append(join)
        lista_productos.append(all)
    df_all = pd.DataFrame(lista_productos)
    df_all.columns = lista_columnas
    df_all = df_all.set_index("ID")
    return df_all.to_csv("../files/ETL/out/productos1.csv")

def exploracion_datos(csv):
    forma = csv.shape
    print(f"La forma es {forma}")
    print("_______________")
    nulos = csv.isna().sum().reset_index()
    print(f"Los nulos son:")
    print(nulos)
    print("_______________")
    duplicados = csv.duplicated().sum()
    print(f"Hay {duplicados} duplicados")
    print("_______________")
    tipo_dato = csv.dtypes.reset_index()
    print(f"Los datos son de tipo:")
    print(tipo_dato)
    print("_______________")
    columnas = csv.columns
    print(f"Las columnas son {columnas}")

def unificacion_columnas(df):
    df.columns = df.columns.str.lower()
    df.columns = [unidecode(columna) for columna in df.columns]
