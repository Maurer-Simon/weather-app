from django.shortcuts import render



def home(request):
    import json
    import requests
    from django.conf import settings

    api_key = settings.WEATHER_API_KEY
    weather_data = {}
    location = request.GET.get('location', 'Passau')  # Default location is Passau

    try:
        response = requests.get(f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}&aqi=no")
        response.raise_for_status()
        data = response.json()
        weather_data = {
            'location_name': data['location']['name'],
            'country': data['location']['country'],
            'time_zone': data['location']['tz_id'],
            'local_time': data['location']['localtime'],
            'temp_c': data['current']['temp_c'],
            'condition_text': data['current']['condition']['text'],
            'feels_like_c': data['current']['feelslike_c']
        }
    except (requests.RequestException, KeyError):
        weather_data = "Error..."

    return render(request, 'home.html', {'weather_data': weather_data, 'location': location})


def about(request):
    return render(request, 'about.html', {})
