import requests
from django.shortcuts import render

def earthquake_list(request):
    # Fetch data from USGS
    url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson'
    response = requests.get(url)
    data = response.json()

    # Extract the first 500 earthquakes
    earthquakes = data['features'][:500]
    
    # Extract essential info
    earthquake_data = [
        {
            'place': eq['properties']['place'],
            'magnitude': eq['properties']['mag'],
            'time': eq['properties']['time'],
            'url': eq['properties']['url'],
            'coordinates': eq['geometry']['coordinates'],
        }
        for eq in earthquakes
    ]
    
    return render(request, 'tracker/earthquake_list.html', {'earthquakes': earthquake_data})
