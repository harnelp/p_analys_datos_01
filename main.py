import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, f1_score, accuracy_score
from sklearn.model_selection import train_test_split

# Cargamos el DataFrame
df_limpio = pd.read_csv('p_analys_datos_05/datos_limpios.csv')

# Eliminar la columna 'categoria_edad' para crear la matriz X y y
X = df_limpio.drop(columns=['DEATH_EVENT', 'categoria_edad'])
y = df_limpio['DEATH_EVENT']

# Partición estratificada del dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

# Ajustar un Random Forest
rf_classifier = RandomForestClassifier(random_state=42)  # Puedes variar los parámetros aquí
rf_classifier.fit(X_train, y_train)

# Predecir sobre el conjunto de test
y_pred = rf_classifier.predict(X_test)

# Calcular la matriz de confusión
conf_matrix = confusion_matrix(y_test, y_pred)
print("Matriz de confusión:")
print(conf_matrix)

# Calcular F1-Score y comparar con el accuracy
f1 = f1_score(y_test, y_pred)
accuracy = accuracy_score(y_test, y_pred)
print(f"F1-Score: {f1:.2f}")
print(f"Accuracy: {accuracy:.2f}")
