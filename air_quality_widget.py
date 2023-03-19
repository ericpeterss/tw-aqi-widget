"""
air_quality_widget.py

This script creates a simple air quality widget using Tkinter. It fetches air quality index (AQI) data from the EPA API and displays the AQI values for two specific sites. The background color of the widget changes based on the AQI values.

Functions:
    - get_air_quality(): Fetches AQI data from the EPA API and returns the site names and AQI values for two specific sites.
    - update_widget(): Updates the widget's label with the latest AQI data and changes the background color based on the AQI values.
"""

import os
import time
import tkinter as tk
import requests
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

API_KEY = os.getenv('API_KEY')

def get_air_quality():
    url = f'https://data.epa.gov.tw/api/v2/aqx_p_432?api_key={API_KEY}'
    while True:
        try:
            response = requests.get(url)
            data = response.json()
            site_name1 = data['records'][68]["sitename"]
            aqi1 = data['records'][68]["aqi"]
            site_name2 = data['records'][14]["sitename"]
            aqi2 = data['records'][14]["aqi"]
            return site_name1, aqi1, site_name2, aqi2
        except requests.exceptions.JSONDecodeError:
            print('Failed to decode JSON data. Retrying in 30 seconds...')
            time.sleep(30)

def update_widget():
    site_name1, aqi1, site_name2, aqi2 = get_air_quality()
    label.config(text='Site Name: {}\nAQI: {}\nSite Name: {}\nAQI: {}'.format(site_name1, aqi1, site_name2, aqi2))
    # Change the background color based on the AQI value
    if int(aqi1) and int(aqi2) <= 50:
        window.configure(background='green')
    elif int(aqi1) and int(aqi2) < 100:
        window.configure(background='yellow')
    else:
        window.configure(background='red')
    # Update the widget every 30 minutes
    label.after(1800000, update_widget)

# Create a Tkinter window
window = tk.Tk()

# Set the title of the window
window.title('Air Quality Widget')

# Set the width and height of the window
window.geometry('200x70')

# Create a label to display the air quality index
label = tk.Label(window, text='Site Name: \nAQI: \nSite Name: \nAQI: ')
label.pack()

# Call the update_widget function to update the label with the air quality index
update_widget()

# Start the Tkinter event loop
window.mainloop()
