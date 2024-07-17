# Importamos las librerias que vamos a ocupar en este proyecto
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


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

# Agregamos un modelo para predecir el consumo 2023 basandose en 2022
X = data_consumo[['2022']].dropna()
y = data_consumo['2023'].dropna()
common_index = X.index.intersection(y.index)
X = X.loc[common_index]
y = y.loc[common_index]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=2)
model = LinearRegression()
model.fit(X_train, y_train)

Predicciones = model.predict(X_test)
print(Predicciones)

# Verificamos el modelo
r2_score = model.score(X_test, y_test)
f'R² Score: {r2_score:.2f}'


# Predicciones vs Valores reales
plt.figure(figsize=(10, 6))
plt.scatter(y_test, Predicciones, alpha=0.7)
plt.plot([y_test.min(), y_test.max()], [
         y_test.min(), y_test.max()], 'r--', linewidth=2)
plt.title('Predicciones vs Valores reales ')
plt.xlabel('Valores reales')
plt.ylabel('Predicciones')
plt.show()
