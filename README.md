# Weather API App

## Project Overview

The Weather API App is a Django-based web application that fetches and displays current weather information for a specified location. This project demonstrates how to connect a Django application to a third-party API to retrieve and present data dynamically.

## Features

- **Weather Data Fetching**: Utilizes the WeatherAPI to get real-time weather data for any specified location.
- **Dynamic Search**: Users can enter a location into a search form to retrieve current weather information for that area.
- **Error Handling**: Displays an appropriate error message if there is an issue with the API request or if the location data is invalid.
- **Responsive Design**: The application is styled using Bootstrap to ensure it is responsive and user-friendly.

## Technologies Used

- **Django**: The web framework used to develop the application.
- **WeatherAPI**: The external API used to fetch current weather data.
- **Bootstrap**: Used for styling and creating a responsive design.
- **HTML/CSS**: Markup and styling of the web pages.

## How to Run the Project

1. Clone the repository:
    ```bash
    git clone https://github.com/maurer-simon/weather-api-app.git
    ```

2. Navigate to the project directory:
    ```bash
    cd weather-api-app
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up the Django settings by adding your WeatherAPI key:
    - Create a `.env` file in the project root and add:
        ```
        WEATHER_API_KEY=your_api_key_here
        ```

5. Run the Django development server:
    ```bash
    python manage.py runserver
    ```

6. Open your browser and go to `http://127.0.0.1:8000/` to view the application.

## Usage

- On the homepage, you can enter the name of any location to get the current weather data for that location.
- The weather information includes details such as temperature, weather conditions, and more.
- The 'About' page provides an overview of the project and its purpose.
