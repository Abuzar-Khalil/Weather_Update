# from django.shortcuts import render

# import requests

# # def weather_view(request):
# #     # Static weather data
# #     weather_data = {
# #         'location': 'New York City',
# #         'temperature': '22°C',
# #         'humidity': '60%',
# #         'description': 'Partly Cloudy',
# #     }
# #     return render(request, 'weather/index.html', {'weather': weather_data})

# # def weather_view(request):
# #     api_key = 'cc81efd8be20986081109b8d8bdb0d07'
# #     city = 'New York'
# #     url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

# #     response = requests.get(url)
# #     data = response.json()

# #     weather_data = {
# #         'location': data['name'],
# #         'temperature': f"{data['main']['temp']}°C",
# #         'humidity': f"{data['main']['humidity']}%",
# #         'description': data['weather'][0]['description'].title(),
# #     }
# #     return render(request, 'weather/index.html', {'weather': weather_data})

# from .forms import CityForm

# def weather_view(request):
#     form = CityForm(request.POST or None)
#     city = 'New York'
#     weather_data = {}

#     if form.is_valid():
#         city = form.cleaned_data['city']
        
#     # Fetch weather data as before using the `city` variable.
#     api_key = 'cc81efd8be20986081109b8d8bdb0d07'
#     url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
#     response = requests.get(url)
#     data = response.json()

#     weather_data = {
#         'location': data['name'],
#         'temperature': f"{data['main']['temp']}°C",
#         'humidity': f"{data['main']['humidity']}%",
#         'description': data['weather'][0]['description'].title(),
#     }

#     return render(request, 'weather/index.html', {'weather': weather_data, 'form': form})

from django.shortcuts import render
from .forms import CityForm
import requests

def weather_view(request):
    form = CityForm(request.POST or None)
    weather_data = None  # Initialize without data

    if request.method == 'POST' and form.is_valid():
        city = form.cleaned_data['city']
        
        # Fetch weather data using the city from the form
        api_key = 'cc81efd8be20986081109b8d8bdb0d07'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)
        data = response.json()

        if data.get('main'):  # Ensure the response contains weather data
            weather_data = {
                'location': data['name'],
                'temperature': f"{data['main']['temp']}°C",
                'humidity': f"{data['main']['humidity']}%",
                'description': data['weather'][0]['description'].title(),
            }

    # Only display weather if data is available after form submission
    return render(request, 'weather/index.html', {'weather': weather_data, 'form': form})
