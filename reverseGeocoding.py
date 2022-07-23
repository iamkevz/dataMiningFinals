import numpy as np
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.point import Point

geolocator = Nominatim(user_agent="test")

def reverse_geocoding(lat, lon):
    try:
        location = geolocator.reverse(Point(lat, lon))
        return location.raw['display_name']
    except:
        return None

df = pd.read_csv('Cleaned.csv')


df['address'] = np.vectorize(reverse_geocoding)(df['long'], df['lat'])

df.to_csv('reversed_geocode.csv')
