import io

import pandas as pd
from flask import Flask
from flask import render_template
import folium
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64

from folium.plugins import FastMarkerCluster


app = Flask(__name__)


@app.route("/")
def base():
    # base map
    map = folium.Map(
        location=[14.164862797000069, 120.8616300000001],
        zoom_start=6
    )
    a_list = convertToList('reversed_geocode.csv')
    fg = folium.FeatureGroup(name='tweet_map')
    for i in a_list:
        if i[0].find("Medical") != -1:
            fg.add_child(folium.Marker(location=[i[2], i[1]], popup='<b>Need: </b>' + i[0] + " " + "<b>Location: </b>" + i[3], icon=folium.Icon(color='red')))
        elif i[0].find("Food") != -1:
            fg.add_child(folium.Marker(location=[i[2], i[1]], popup='<b>Need: </b>' + i[0] + " " + "<b>Location: </b>" + i[3], icon=folium.Icon(color='green')))
        else:
            fg.add_child(folium.Marker(location=[i[2], i[1]], popup='<b>Need: </b>' + i[0] + " " + "<b>Location: </b>" + i[3], icon=folium.Icon(color='blue')))
    map.add_child(fg)
    #showPlot()
    #map.save("templates/index.html")
    return render_template('index.html')


def convertToList(file):
    tweet = pd.read_csv(file)
    list = tweet[['category', 'lat', 'long', 'address']].values.tolist()
    return list

def showPlot():
    df = pd.read_csv("Jupyter/Jupyter/Datasets/dataset_with_goods.csv")

    cities = ['abuyog leyte', 'capiz', 'dumarao capiz', 'iloilo', 'ajuy iloilo',
              'leyte leyte', 'pilar leyte', 'tanauan leyte', 'samar', 'guiuan samar']

    location = df[df["loc_name"].isin(cities)]
    df_loc = location
    df_loc["loc_name"].unique()

    s = df_loc.groupby(['loc_name', 'people_needs']).size().unstack()
    s.plot(kind='bar', stacked=True, figsize=(9, 7))

    plt.title("10 Cities and what are the People Needs in that City")
    plt.xlabel("Cities")
    plt.savefig('templates/plot.png')


if __name__ == '__main__':
    app.run(debug=True)
