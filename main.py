from datasets import load_dataset

# cargando dataset
dataset = load_dataset("mstz/heart_failure")
# Accediendo a los datos
data = dataset["train"]
#print(data)

#Convertir la lista de edades a un arreglo de NumPy y calcular el promedio
import numpy as np
#capturando edades
edades = np.array(data['age'])
#tomamos el promedio
edad_promedio = np.mean(edades)
#redondeamos el promedio
promedio_redondeado = round(edad_promedio,1)
#imprimimos resultado
#print("Promedio de edad:",promedio_redondeado)

import pandas as pd
#Convertir la estructura Dataset en un DataFrame de Pandas usando pd.DataFrame.
df = pd.DataFrame(data)
#Separar el dataframe en dos diferentes, uno conteniendo las filas con personas que perecieron (is_dead=1) y otro con el complemento.
fallecidos_df = df[df['is_dead'] == 1]
sobrevivientes_df = df[df['is_dead'] == 0]
#Calcular los promedios de las edades de cada dataset e imprimir.
promedio_edad_fallecidos = fallecidos_df['age'].mean()
promedio_edad_sobrevivientes = sobrevivientes_df['age'].mean()

#redondeo el resultado
edad_p_round_fallecidos = round(promedio_edad_fallecidos,1)
edad_p_round_sobrevivientes =round(promedio_edad_sobrevivientes,1)

#imprimimos resultados
#print("Promedio de edad de los fallecidos:", edad_p_round_fallecidos)
#print("Promedio de edad de los sobrevivientes:", edad_p_round_sobrevivientes)

#parte 3
#Verificar que los tipos de datos son correctos en cada colúmna (por ejemplo que no existan colúmnas numéricas en formato de cadena).
tipos_datos_correctos = df.dtypes
#print("Tipos de datos en cada columna:\n", tipos_datos_correctos)

#Calcular la cantidad de hombres fumadores vs mujeres fumadoras (usando agregaciones en Pandas).
cantidad_hombres_fumadores = df[(df['is_male'] == 1) & (df['is_smoker'] == 1)].shape[0]
cantidad_mujeres_fumadoras = df[(df['is_male'] == 0) & (df['is_smoker'] == 1)].shape[0]

print("Cantidad de hombres fumadores:", cantidad_hombres_fumadores)
print("Cantidad de mujeres fumadoras:", cantidad_mujeres_fumadoras)
