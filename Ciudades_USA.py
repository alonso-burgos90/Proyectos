# Importamos las librerias que vamos a ocupar en este proyecto
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data_ciudades = pd.read_csv('Population of all US Cities 2024.csv')

# Vemos informacion
print(data_ciudades.head(20))

# Para ver las ultimas filas
print(data_ciudades.tail(10))
# con esto verficamos si hay valores NaN
data_ciudades.info()
data_ciudades.describe()

# Analisis descriptivo Graficos
# Estilo de graficos
sns.set_style(style="whitegrid")


# Histograma poblacion 2024
plt.figure(figsize=(10, 6))
sns.histplot(data_ciudades['Population 2024'],
             bins=30, kde=True)
plt.title('Distribucion Poblacion 2024')
plt.xlabel('Poblacion')
plt.ylabel('Frecuencia')
plt.show


# Historiagrama densidad de poblacion
plt.figure(figsize=(10, 6))
sns.histplot(data_ciudades['Density (/mile2)'], bins=30, kde=True)
plt.title('Distribucion de la densidad de poblacion')
plt.xlabel('Densidad')
plt.ylabel('Frecuencia')
plt.show()

# Grafico de dipersion comparando 2020 con 2024
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Population 2020',
                y='Population 2024', data=data_ciudades)
plt.title('Comparando poblacion en 2020 y 2024')
plt.xlabel('Poblacion 2020')
plt.ylabel('Poblacion 2024')
plt.show()


# Incrementos en la poblacion en las ciudades mas grandes,Aqui hicimos un analisis mas profundo
Top_Crecimientos_cd = data_ciudades.nlargest(10, 'Annual Change')
print(Top_Crecimientos_cd)

# Predicciones Futuras para la poblacion con machine learning
X = data_ciudades[['Population 2020']]
y = data_ciudades['Population 2024']
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.2, random_state=42)


print(X_train.shape)
print(y_train.shape)


model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
print(predictions)
