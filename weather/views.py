import urllib.request
import json
from django.shortcuts import render


def index(request):
    
    if request.method == 'POST':
        city = request.POST['city']
        # icon = request.POST['icon']

        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' +
                                        city + '&units=metric&appid=ecc1b951e5a9948949760949bc708c93').read()
        list_of_data = json.loads(source)

        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ', '
            + str(list_of_data['coord']['lat']),

            "temp": str(list_of_data['main']['temp']) + ' °C',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            'main': str(list_of_data['weather'][0]['main']),
            'description': str(list_of_data['weather'][0]['description']),
            'icon': list_of_data['weather'][0]['icon'],
        }
        print(data)
    else:
        data = {}

    return render(request, "weather/weather.html", data)

# def get_icon_data(request):
#         icon_id = list_of_data['weather'][0]['icon']
#         url = 'http://openweathermap.org/img/wn/{icon}.png'.format(icon=icon_id)
#         response = requests.get(url, stream=True)
#         return base64.encodebytes(response.raw.read())