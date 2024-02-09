import pandas as pd
import matplotlib.pyplot as plt

# Cargamos el DataFrame
df_limpio = pd.read_csv('p_analys_datos_05/datos_limpios.csv')

# Creamos una figura con subplots
fig, axs = plt.subplots(1, 4, figsize=(14, 5))  # Ajusta el tamaño según tus necesidades

# Lista de condiciones y sus respectivos títulos
condiciones = ['anaemia', 'diabetes', 'smoking', 'DEATH_EVENT']
titulos = ['Anémicos', 'Diabéticos', 'Fumadores', 'Muertos']

for i, condicion in enumerate(condiciones):
    # Calculamos las proporciones
    sizes = df_limpio[condicion].value_counts(normalize=True) * 100
    labels = ['No', 'Sí']
    colors = ['#ff9999','#66b3ff']  # Ajusta los colores según tus necesidades
    
    # Dibujamos la gráfica de torta
    axs[i].pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    axs[i].axis('equal')  # Esto asegura que la torta sea un círculo
    axs[i].set_title(titulos[i])

# Ajustar el layout y mostrar la gráfica
plt.tight_layout()
plt.show()
