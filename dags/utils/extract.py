# we import the libraries
import requests


# the function for extracting the data from oprn meteo
def extract_data(**kwargs):
    url = "https://api.open-meteo.com/v1/forecast?latitude=48.8566&longitude=2.3522&hourly=temperature_2m&timezone=Europe%2FParis"
    response = requests.get(url)
    data = response.json()
    kwargs['ti'].xcom_push(key='raw_data', value=data)




