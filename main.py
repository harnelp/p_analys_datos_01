import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Cargamos el DataFrame
df_limpio = pd.read_csv('p_analys_datos_05/datos_limpios.csv')

# Eliminar la columna 'categoria_edad' para crear la matriz X y y
X = df_limpio.drop(columns=['DEATH_EVENT', 'categoria_edad'])
y = df_limpio['DEATH_EVENT']

# Graficar la distribución de clases
plt.figure(figsize=(8, 5))
df_limpio['DEATH_EVENT'].value_counts().plot(kind='bar', color=['blue', 'orange'])
plt.title('Distribución de Clases')
plt.xlabel('Clase')
plt.ylabel('Frecuencia')
plt.xticks(ticks=[0, 1], labels=['Vivo', 'Muerto'], rotation=0)
plt.show()

# Partición estratificada del dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

# Ajustar un árbol de decisión
dt_classifier = DecisionTreeClassifier(random_state=42)  # Puedes variar los parámetros aquí
dt_classifier.fit(X_train, y_train)

# Predecir sobre el conjunto de test
y_pred = dt_classifier.predict(X_test)

# Calcular el accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy del modelo: {accuracy:.2f}")

# Experimentar con diferentes valores de parámetros para el árbol de decisión
# Por ejemplo, cambiar la profundidad máxima (max_depth), criterio, min_samples_split, etc.
