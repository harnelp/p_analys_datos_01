import pandas as pd
from sklearn.manifold import TSNE
import plotly.express as px

# Cargar el DataFrame
df_limpio = pd.read_csv('p_analys_datos_05/datos_limpios.csv')

# Preparar los datos, eliminar la columna objetivo y otras no deseadas
X = df_limpio.drop(columns=['DEATH_EVENT', 'categoria_edad']).values
y = df_limpio['DEATH_EVENT'].values

# Ejecutar t-SNE
X_embedded = TSNE(n_components=3, learning_rate='auto', init='random', perplexity=3).fit_transform(X)

# Crear un DataFrame con los datos transformados y la columna objetivo
tsne_df = pd.DataFrame(X_embedded, columns=['x', 'y', 'z'])
tsne_df['DEATH_EVENT'] = y

# Crear un gráfico de dispersión 3D usando Plotly
fig = px.scatter_3d(tsne_df, x='x', y='y', z='z',
                    color='DEATH_EVENT', 
                    labels={'0': 'Vivo', '1': 'Muerto'},
                    title='Visualización 3D t-SNE de los datos de insuficiencia cardíaca')

# Mostrar el gráfico
fig.show()

