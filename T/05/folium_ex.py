import json
import folium
import os

map_osm = folium.Map(location=[36.320231, 127.859134], zoom_start=8)

rfile = open('skorea-municipalities-2018-geo.json', 'r', encoding='utf-8').read()
jsonData = json.loads(rfile)

folium.GeoJson(jsonData, name='json_data').add_to(map_osm)

if os.path.isfile('/Users/kadragon/Dev/Python_T/T/05/map.html'):
    os.system('rm -rf /Users/kadragon/Dev/Python_T/T/05/map.html')

map_osm.save('/Users/kadragon/Dev/Python_T/T/05/map.html')