import pandas as pd
import seaborn as sns
import numpy as np 
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from collections import Counter
# import warnings
# warnings.simplefilter("ignore")

df0 = pd.read_excel('data/Dataparcial1.xlsx')

# Definimos las constantes para las etiquetas de las columnas
EDAD = 'Edad'
CLASE_TRABAJO = 'Clase de Trabajo'
CAPITAL_FINAL = 'Capital Final'
EDUCACION = 'Educación'
EDUCACION_NUMERO = 'Educación Número'
ESTADO_CIVIL = 'Estado Civil'
OCUPACION = 'Ocupación'
RELACION = 'Relación'
RAZA = 'Raza'
SEXO = 'Sexo'
CAPITAL_GANADO = 'Capital Ganado'
CAPITAL_PERDIDO = 'Capital Perdido'
HORAS_POR_SEMANA = 'Horas por Semana'
PAIS_ORIGEN = 'País Origen'
CLASE = 'Clase'
INDICE = 'Índice'

GT_50K = 1
LTE_50K = 0

columns = [
  EDAD,
  CLASE_TRABAJO,
  CAPITAL_FINAL,
  EDUCACION,
  EDUCACION_NUMERO,
  ESTADO_CIVIL,
  OCUPACION,
  RELACION,
  RAZA,
  SEXO,
  CAPITAL_GANADO,
  CAPITAL_PERDIDO,
  HORAS_POR_SEMANA,
  PAIS_ORIGEN,
  CLASE,
]

fastCols = [
  EDAD
]

df0.columns = columns

df0[INDICE] = ['Fila' + str(item) for item in range (0, df0.shape[0])]

for column in df0.select_dtypes(include = 'object'):
  df0[column] = df0[column].astype('string')

df0.info()

# Limpiamos los datos de CLASE
df0[CLASE] = df0[CLASE].str.replace('.', '')

# Reemplazamos los valores de CLASE por '>50K' = 1, '<=50K' = 0
df0[CLASE] = df0[CLASE].apply(lambda x: GT_50K if x.strip() == ">50K" else LTE_50K)

##########
# Limpieza de datos
##########

# Funcion para reemplazar calores atipicos en variables categoricas usando la moda.
# df: Dataframe
# columnA: class column to filter
# columnB: target column
# compare: class value to filter
# value: replacement source
def replace(df, columnA, columnB, compare, value):
  subset = df.loc[df[columnA] == compare, column]
  count = Counter(subset)
  most_frequent_value = count.most_common()
  mfv = most_frequent_value[0][0]
  print(f'El valor categórico más frecuente para subgrupo {compare} de la variable {columnB} es: {mfv}')
  df[columnB] = np.where((df[columnA] == compare) & (df[columnB] == value), mfv, df[columnB])

# Function para eliminar valores NaN
def impute_nan(df, columnA):
  df[columnA] = df[columnA].dropna()

# Funcion para eliminar valores atipicos usando Winsorization(Winsorizacion).
def impute_outlier(df, columnA, columnB, compare):
  subset = df.loc[df[columnA] == compare, columnB:columnA]
  median = subset[columnB].median().astype(int)
  q1 = subset.quantile(0.25, numeric_only = True)
  q3 = subset.quantile(0.75, numeric_only = True)
  iqr = q3 - q1
  df[columnB] = np.where((df[columnA] == compare) & (df[columnB] > median + 1.5 * iqr[columnB]), median, df[columnB])
  df[columnB] = np.where((df[columnA] == compare) & (df[columnB] < median - 1.5 * iqr[columnB]), median, df[columnB])

##########################
# Limpiamos General
##########################
for column in columns:
  if df0[column].dtype == 'string':
    replace(df0, CLASE, column, GT_50K, ' ?')
    replace(df0, CLASE, column, LTE_50K, ' ?')

  if df0[column].dtype == 'int64':
    impute_nan(df0, column)

for column in columns:

  if column == CLASE:
    continue

  #######################
  # Gráficos Pre Limpieza
  #######################
  if df0[column].dtype == 'int64':
    # histo = df0[column].hist(bins=[20,30,40,50,60,70,80,90,100],rwidth=0.9)
    histo = df0[column].hist(rwidth = 0.9)
    histo.set(xlabel = column, ylabel = 'Cuenta')  
    plt.title(f'Histograma {column}')
    plt.show()

    df0.boxplot(column = [column])
    plt.title(f'Diagrama de caja para {column}')
    plt.ylabel("Cuenta")
    plt.show()

  ##########################
  # Limpiamos datos atipicos
  ##########################
  if df0[column].dtype == 'int64':
    impute_outlier(df0, CLASE, column, GT_50K)
    impute_outlier(df0, CLASE, column, LTE_50K)

  ########################
  # Gráficos Post Limpieza
  ########################
  if df0[column].dtype == 'int64':
    # histo = df0[column].hist(bins=[20,30,40,50,60,70,80,90,100],rwidth=0.9)
    histo = df0[column].hist(rwidth = 0.9)
    histo.set(xlabel = column, ylabel = 'Cuenta')  
    plt.title(f'Histograma {column}')
    plt.show()

    df0.boxplot(column = [column])
    plt.title(f'Diagrama de caja para {column}')
    plt.ylabel("Cuenta")
    plt.show()
