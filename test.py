import requests
import tkinter as tk
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

API_KEY = os.getenv('API_KEY')

url = f'https://data.epa.gov.tw/api/v2/aqx_p_432?api_key={API_KEY}'
response = requests.get(url)
# print(response.text)
data = response.json()
site_name = data['records'][68]["sitename"]
air_quality_index = data['records'][68]["aqi"]
print(site_name)
print(air_quality_index)


