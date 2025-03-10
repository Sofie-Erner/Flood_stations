import folium
import requests
import json

""" Initial Map of England """
my_map = folium.Map(location=[52.561928, -1.464854], zoom_start = 7) # map of England from centre

""" Request of stations from Environmental Agency """
response = requests.get("https://environment.data.gov.uk/flood-monitoring/id/stations?status=Active")
y = response.json()

radius = 5

for i in range(0,len(y["items"])):
    st = y["items"][i]

    try:
        folium.CircleMarker(
            location=[st["lat"], st["long"]],
            radius=radius,
            color="black",
            weight=1,
            fill = True,
            fill_opacity=0.6,
            opacity=1
            #popup="{} meters".format(radius),
            #tooltip="I am in meters",
        ).add_to(my_map)

    except Exception as err:
        print("number: ",i)
        print(err)


my_map.save('map.html')