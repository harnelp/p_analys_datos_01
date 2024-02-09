import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Cargar los datos limpios
df_limpio = pd.read_csv('p_analys_datos_05/datos_limpios.csv')

"""
# Verificar los nombres de las columnas
print(df_limpio.columns)
"""


# Define las categorías basadas en las columnas de tu DataFrame
categorias = ['Anémicos', 'Diabéticos', 'Fumadores', 'Muertos']
condiciones = ['anaemia', 'diabetes', 'smoking', 'DEATH_EVENT']

# Asume que la columna 'sex' usa 0 para mujeres y 1 para hombres
# Si la columna 'sex' no usa valores binarios, deberás ajustar las condiciones
hombres = [df_limpio[(df_limpio['sex'] == 1) & (df_limpio[condicion] == 1)].shape[0] for condicion in condiciones]
mujeres = [df_limpio[(df_limpio['sex'] == 0) & (df_limpio[condicion] == 1)].shape[0] for condicion in condiciones]

# Configura la ubicación de las barras en el eje x
x = np.arange(len(categorias))
width = 0.35  # Ancho de las barras

# Crear el histograma agrupado
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, hombres, width, label='Hombres', color='blue')
rects2 = ax.bar(x + width/2, mujeres, width, label='Mujeres', color='red')

# Añadir etiquetas y título
ax.set_ylabel('Cantidad')
ax.set_title('Histograma Agrupado por Sexo')
ax.set_xticks(x)
ax.set_xticklabels(categorias)
ax.legend()

# Función para añadir etiquetas a las barras
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

# Llama a la función autolabel para cada conjunto de barras
autolabel(rects1)
autolabel(rects2)

# Ajusta el layout y muestra el gráfico
fig.tight_layout()
plt.show()
