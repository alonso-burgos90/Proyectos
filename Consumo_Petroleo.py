# Importamos las librerias que vamos a ocupar en este proyecto
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data_consumo = pd.read_csv('Oil Consumption by Country 1965 to 2023.csv')

# Visualizamos informacion
print(data_consumo.head(20))

# Para ver las ultimas filas
data_consumo.tail(15)

data_consumo.info()

# con esto podemos ver la media, moda etc
data_consumo.describe()

# Despues de verificar la informacion, tambien verficamos si hay campos o filas NaN
data_consumo.isnull().sum()

# Los quitamos
data_consumo.dropna(inplace=True)

# Analisis descriptivo Graficos
# Estilo de graficos
sns.set_style("darkgrid")

# Vamos a hacer un historiagrama de consuño 2023 comparando  con 2000 Año 2023

# Año 2023
plt.figure(figsize=(10, 6))
sns.histplot(data_consumo['2023'].dropna(), kde=True)
plt.title('Consumo petroleo 2023')
plt.xlabel('Consumo de Petroleo por (Barriles por dia)')
plt.ylabel('Frecuencia')
plt.show()

# Año 2020
plt.figure(figsize=(10, 6))
sns.histplot(data_consumo['2000'].dropna(), kde=True)
plt.title('Consumo petroleo 2000')
plt.xlabel('Consumo de Petroleo por (Barriles por dia)')
plt.ylabel('Frecuencia')
plt.show()



