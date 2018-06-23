import folium
import pandas

mappings = pandas.read_excel('vol_locations.xlsx')
lat = list(mappings['Latitude'])
lon = list(mappings['Longitude'])
elev = list(mappings['Elevation (m)'])
name = list(mappings['Name'])

map_obj = folium.Map(location=[41.034069, -112.234989],zoom_start=5)

fg = folium.FeatureGroup(name='Volcano Map')

for lt, lg, el, na in zip(lat,lon,elev,name):
    fg.add_child(folium.Marker(location=[lt,lg], popup=folium.Popup(str(na) + '\n' + str(el) + ' m',parse_html=True), icon=folium.Icon(color='red')))

map_obj.add_child(fg)

map_obj.save('map1.html')