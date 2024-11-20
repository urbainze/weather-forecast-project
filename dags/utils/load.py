import pandas as pd
import psycopg2

def load_data_to_postgres(**kwargs):
    clean_data = kwargs['ti'].xcom_pull(key='clean_data')
    df = pd.DataFrame(clean_data)

    # Connexion à PostgreSQL
    conn = psycopg2.connect(
        dbname="weather_data",
        user="postgres",
        password="your_password",
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()

    # Création de la table si elle n'existe pas
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS hourly_temperature (
        timestamp TIMESTAMP PRIMARY KEY,
        temperature FLOAT
    );
    """)

    # Insertion des données
    for _, row in df.iterrows():
        cursor.execute("""
        INSERT INTO hourly_temperature (timestamp, temperature)
        VALUES (%s, %s)
        ON CONFLICT (timestamp) DO NOTHING;
        """, (row['timestamp'], row['temperature']))

    conn.commit()
    cursor.close()
    conn.close()
