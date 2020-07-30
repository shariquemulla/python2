import folium, pandas

def color_producer(elevation):
    if el<=1500:
        return "green"
    elif el<=3000:
        return "orange"
    else:
        return "darkred"

df = pandas.read_csv("Volcanoes.txt")
lat = list(df['LAT'])
lon = list(df['LON'])
name = list(df['NAME'])
elev = list(df['ELEV'])

map = folium.Map(location=[48.7767982,-121.8109970], zoom_start=5, tiles="Stamen Terrain")

fg1 = folium.FeatureGroup(name="Volcanoes")
for lat,lon,nam,el in zip(lat,lon,name,elev):
    fg1.add_child(folium.CircleMarker(location=[lat, lon], color='gray', radius=5,
        popup=nam, fill_color=color_producer(el), fill_opacity=7, fill=True))

fg2 = folium.FeatureGroup(name="Population")
fg2.add_child(folium.GeoJson(open("world.json", "r", encoding='utf-8-sig').read(), 
style_function=lambda features: { 
    'fillColor':'green' if features['properties']['POP2005'] <= 10000000
    else 'blue' if features['properties']['POP2005'] <= 30000000
    else 'red'
}))

map.add_child(fg1)
map.add_child(fg2)
map.add_child(folium.LayerControl())
map.save("map.html")

