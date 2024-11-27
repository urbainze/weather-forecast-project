
# Nous importons les données
import pandas as pd

# Fonction servant à transformer les données
def transform_data(**kwargs):
    raw_data = kwargs['ti'].xcom_pull(key='raw_data')
    # Convertir les données horaires en DataFrame
    df = pd.DataFrame({
        'timestamp': raw_data['hourly']['time'],
        'temperature': raw_data['hourly']['temperature_2m']
    })
    # Convertir les timestamps en format datetime
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    # Convertir les timestamps en chaîne de caractères (ISO format)
    df['timestamp'] = df['timestamp'].dt.strftime('%Y-%m-%dT%H:%M:%S')
    # Pousser les données nettoyées dans XCom
    kwargs['ti'].xcom_push(key='clean_data', value=df.to_dict(orient='records'))
