import requests
import tkinter as tk
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

API_KEY = os.getenv('API_KEY')

def get_air_quality():
    url = f'https://data.epa.gov.tw/api/v2/aqx_p_432?api_key={API_KEY}'
    response = requests.get(url)
    data = response.json()
    site_name = data['records'][68]["sitename"]
    aqi = data['records'][68]["aqi"]
    return site_name, aqi

def update_widget():
    site_name, aqi = get_air_quality()
    label.config(text='Site Name: {}\nAQI: {}'.format(site_name, aqi))
    # Change the background color based on the AQI value
    if int(aqi) <= 50:
        window.configure(background='green')
    elif int(aqi) < 100:
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
window.geometry('200x50')

# Create a label to display the air quality index
label = tk.Label(window, text='Site Name: \nAQI: ')
label.pack()

# Call the update_widget function to update the label with the air quality index
update_widget()

# Start the Tkinter event loop
window.mainloop()
