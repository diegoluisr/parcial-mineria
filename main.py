import pandas as pd
import seaborn as sns
import numpy as np 
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

df0 = pd.read_excel('data/Dataparcial1.xlsx')

df0.columns = [
  'Edad',
  'Clase de Trabajo',
  'Capital Final',
  'Educacion',
  'Educacion numero',
  'Estado civil',
  'Ocupacion',
  'Relacion',
  'Raza',
  'Sexo',
  'Capital ganado',
  'Capital perdido',
  'Horas por Semana',
  'Pais origen',
  'Clase',
]

out = ['Fila' + str(item) for item in range (0, df0.shape[0])]
df0['index'] = out

# df1=df0.copy()
df0.info()

summary = df0.describe()
print(summary)

histo = df0['Edad'].hist(bins=[20,30,40,50,60,70,80,90,100],rwidth=0.9)
histo.set(xlabel = 'Edad', ylabel = 'Count')  
plt.title('Histograma Edad')
plt.show()

histo = df0['Capital Final'].plot(kind = 'hist')
histo.set(xlabel = 'Capital Final', ylabel = 'Count')  
plt.title('Histograma Capital Final')
plt.show()

histo = df0['Educacion numero'].hist(bins=[2,4,6,8,10,12,14,16],rwidth=0.9)
histo.set(xlabel = 'Educacion numero', ylabel = 'Count')  
plt.title('Histograma Educacion numero')
plt.show()

histo = df0['Capital ganado'].plot(kind = 'hist')
histo.set(xlabel = 'Capital ganado', ylabel = 'Count')
plt.title('Histograma Capital ganado')
plt.show()

histo = df0['Capital perdido'].plot(kind = 'hist')
histo.set(xlabel = 'Capital perdido', ylabel = 'Count')
plt.title('Histograma Capital perdido')
plt.show()

histo = df0['Horas por Semana'].hist(bins = [20,30,40,50,60,70,80,90,100], rwidth = 0.9)
histo.set(xlabel = 'Horas por Semana', ylabel = 'Count')
plt.title('Histograma Horas por Semana')
plt.show()

ax = df0.groupby('Clase de Trabajo')['Edad'].nunique().plot(kind = 'barh')
plt.xlabel('Edad')
plt.ylabel('Clase de Trabajo')
plt.show()

df0.boxplot(column = ['Edad'])
plt.title("Diagrama de caja")
plt.ylabel("Count")
plt.show()

plot0 = px.box(df0,x = 'Edad', title = 'Boxplot variable edad')
plot0.show()

df0.boxplot(column = ['Capital Final'])
plt.title("Diagrama de caja")
plt.ylabel("Count")
plt.show()

plot0 = px.box(df0,x = 'Capital Final', title = 'Boxplot variable Capital Final')
plot0.show()

df0.boxplot(column = ['Educacion numero'])
plt.title("Diagrama de caja")
plt.ylabel("Count")
plt.show()

plot0 = px.box(df0, x = 'Educacion numero', title = 'Boxplot variable educacion numero')
plot0.show()

df0.boxplot(column = ['Capital ganado'])
plt.title("Diagrama de caja")
plt.ylabel("Count")
plt.show()

plot0 = px.box(df0, x = 'Capital ganado', title = 'Boxplot variable capital ganado')
plot0.show()

df0.boxplot(column = ['Capital perdido'])
plt.title("Diagrama de caja")
plt.ylabel("Count")
plt.show()

plot0 = px.box(df0, x = 'Capital perdido', title = 'Boxplot variable capital perdido')
plot0.show()

df0.boxplot(column = ['Horas por semana'])
plt.title("Diagrama de caja")
plt.ylabel("Count")
plt.show()

plot0 = px.box(df0, x = 'Horas por semana', title = 'Boxplot variable horas por semana')
plot0.show()

plot0 = px.strip(df0, x = "Edad", y = "Clase de trabajo")
plot0.show()