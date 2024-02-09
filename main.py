import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Cargar el DataFrame
df_limpio = pd.read_csv('p_analys_datos_05/datos_limpios.csv')

# Eliminar las columnas 'DEATH_EVENT', 'age' y 'categoria_edad' para crear la matriz X
X = df_limpio.drop(columns=['DEATH_EVENT', 'age', 'categoria_edad'])

# Usar la columna 'age' como vector y
y = df_limpio['age']

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Ajustar una regresión lineal
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predecir las edades en el conjunto de prueba
y_pred = regressor.predict(X_test)

# Comparar las edades reales y predichas
comparacion = pd.DataFrame({'Edad Real': y_test, 'Edad Predicha': y_pred})
print(comparacion.head())  # Mostrar las primeras filas para comparar

# Calcular el error cuadrático medio
mse = mean_squared_error(y_test, y_pred)
print("")
print(f"El error cuadrático medio (MSE) es: {mse}")
print("")
