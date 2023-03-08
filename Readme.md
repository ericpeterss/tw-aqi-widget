# Air Quality Widget
A widget that displays the air quality index (AQI) for a specific location in Taiwan.

## Installation
1. Clone this repository: git clone https://github.com/ericpeterss/tw-aqi-widget.git
2. Install the required Python libraries: pip install -r requirements.txt
3. Create a file named .env in the root directory of the project with the following contents:

<code>API_KEY=YOUR_API_KEY</code>

Replace YOUR_API_KEY with your API key for the Taiwanese Environmental Protection Administration air quality data API.

## Usage
1. Run the script: python air_quality_widget.py
2. A window will appear with the current site name and AQI for a location in Taiwan.
3. The window background color will change based on the AQI value.
4. The widget will automatically update every 30 minutes with the latest data.

## Configuration
You can customize the behavior of the widget by modifying the following variables in the air_quality_widget.py file:

- API_KEY: Your API key for the Taiwanese Environmental Protection Administration air quality data API.
- SITE_INDEX: The index of the location to retrieve data for. The default value is 68, which corresponds to YongHe in New Taipei City.

## License
This project is licensed under the MIT License. See the LICENSE file for details.