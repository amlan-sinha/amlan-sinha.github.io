import folium
from geopy.geocoders import Nominatim

# Initialize the geocoder
geocoder = Nominatim(user_agent="amlans")

# Define your journey's locations
locations = ["Dhaka, Bangladesh", "Ithaca, New York, USA", "Princeton, New Jersey, USA"]

# Create a map object, starting at a central point
m = folium.Map(location=[40.0, -74.0], zoom_start=4)

# Loop through the locations, geocode them, and add to the map
for loc in locations:
    location = geocoder.geocode(loc)
    folium.Marker([location.latitude, location.longitude], popup=loc).add_to(m)

# Instead of showing the map, let's save it as an HTML file
m.save('./images/my-journey.html')