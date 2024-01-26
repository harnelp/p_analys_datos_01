import requests
import pandas as pd
import sys

def datos_url(url, archivo_aguardar='datos.csv', timeout=10):
    try:
        respuesta = requests.get(url, timeout=timeout)
        if respuesta.status_code == 200:
            with open(archivo_aguardar, 'w', encoding='utf-8') as archivo:
                archivo.write(respuesta.text)
                print(f"Datos guardados con éxito en {archivo_aguardar}")
        else:
            print(f"Error al descargar los datos: {respuesta.status_code}")
        
    except requests.Timeout:
        print("La solicitud ha excedido el tiempo de espera.")
    except requests.RequestException as e:
        print(f"Error al realizar la solicitud: {e}")

def clear_data(archivo_csv):
    # para leer los datos
    df = pd.read_csv(archivo_csv)
    # para verificar y manejar valores faltantes
    df.dropna(inplace=True)
    # para eliminar filas duplicadas
    df.drop_duplicates(inplace=True)
    # sobre valores outliers(atipicos), en estudio
    # para crear una columna y categorizar edades
    bins = [0, 13, 20, 40, 60, float('inf')]
    labels = ['Niño', 'Adolescente', 'Jóvenes adulto', 'Adulto', 'Adulto mayor']
    df['categoria_edad'] = pd.cut(df['age'], bins=bins, labels=labels, right=False)
    
    # Para guardar el df limpio, como un nuevo archivo CSV
    df.to_csv('datos_limpios.csv', index=False)
    return df

if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
        datos_url(url)
        clear_data('datos.csv')
        print("Proceso completado: los datos han sido descargados, limpiados y guardados en 'datos_limpios.csv'")
    else:
        print("Por favor, proporciona la URL como argumento al ejecutar el script.")
        