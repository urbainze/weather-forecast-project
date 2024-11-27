import os
import psycopg2
import pandas as pd

def load_data_to_postgres(**kwargs):
    # Retrieve cleaned data from XCom
    clean_data = kwargs['ti'].xcom_pull(key='clean_data')
    if not clean_data:
        raise ValueError("No clean data found in XCom.")

    # Convert the cleaned data (list of dictionaries) to a DataFrame
    df = pd.DataFrame(clean_data)

    # Convert the 'timestamp' column from string to datetime
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # Retrieve PostgreSQL connection details from environment variables
    db_name = os.getenv("DATA_DB")
    db_user = os.getenv("POSTGRES_USER")
    db_password = os.getenv("POSTGRES_PASSWORD")
    db_host = os.getenv("POSTGRES_HOST", "data-db")
    db_port = os.getenv("POSTGRES_PORT", "5432")

    if not all([db_name, db_user, db_password]):
        raise ValueError("Missing required database environment variables.")

    # Connect to PostgreSQL
    try:
        # Connect to PostgreSQL
        conn = psycopg2.connect(
            dbname=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )
        cursor = conn.cursor()

        
        # Insert the data
        for _, row in df.iterrows():
            cursor.execute(
                "INSERT INTO weatherdata (timestamp, temperature) VALUES (%s, %s)",
                (row['timestamp'], row['temperature'])
            )

        conn.commit()
        cursor.close()
        conn.close()
        print("Data loaded successfully to PostgreSQL!")

    except Exception as e:
        print(f"An error occurred: {e}")