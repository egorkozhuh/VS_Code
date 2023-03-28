# Parsing parking meters data from gis.arlingtonva.us API
import requests

url = 'https://gis.arlingtonva.us/arlgis/rest/services/public/Parking/MapServer/2/query'

params = {
    'where': '1=1',
    'outFields': '*',
    'returnGeometry': 'true',
    'f': 'geojson'
}

response = requests.get(url, params)
assert response.status_code==200
data = response.json()