import os
import psycopg2
import pandas as pd






def load_data_to_postgres(**kwargs):
    # Retrieve cleaned data from XCom
    clean_data = kwargs['ti'].xcom_pull(key='clean_data')
    df = pd.DataFrame(clean_data)

    # Retrieve PostgreSQL connection details from environment variables
    db_name = os.getenv("POSTGRES_DB")
    if not db_name:
        raise ValueError("Environment variable POSTGRES_DB is not set.")
    db_user = os.getenv("POSTGRES_USER")
    if not db_user:
        raise ValueError("Environment variable POSTGRES_USER is not set.")
    db_password = os.getenv("POSTGRES_PASSWORD")
    if not db_password:
        raise ValueError("Environment variable POSTGRES_PASSWORD is not set.")
    db_host = os.getenv("POSTGRES_HOST", "localhost")
    db_port = os.getenv("POSTGRES_PORT","5432")
    # Connection to PostgreSQL
    try:
        conn = psycopg2.connect(
            dbname=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )
        cursor = conn.cursor()

        # Example operation (Insert DataFrame rows into a PostgreSQL table)
        for index, row in df.iterrows():
            cursor.execute(
                "INSERT INTO weather (timestamp, temperature) VALUES (%s, %s)",
                (row['timestamp'], row['temperature'])
            )

        # Commit and close
        conn.commit()
        cursor.close()
        conn.close()

        print("Data loaded successfully to PostgreSQL!")

    except Exception as e:
        print(f"An error occurred: {e}")
