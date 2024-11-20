
# nous importons les données
import pandas as pd


# fonction servant à transformer les données
def transform_data(**kwargs):
    raw_data = kwargs['ti'].xcom_pull(key='raw_data')
    # Convertir les données horaires en DataFrame
    df = pd.DataFrame({
        'timestamp': raw_data['hourly']['time'],
        'temperature': raw_data['hourly']['temperature_2m']
    })
    # Convertir les timestamps en format datetime
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    kwargs['ti'].xcom_push(key='clean_data', value=df.to_dict(orient='records'))
