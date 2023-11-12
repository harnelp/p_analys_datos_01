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
promedio_redondeado = round(edad_promedio,2)
#imprimimos resultado
print("Promedio de edad:",promedio_redondeado)