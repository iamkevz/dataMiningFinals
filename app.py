import io

import pandas as pd
from flask import Flask
from flask import render_template
import folium
import pandas as pd


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


if __name__ == '__main__':
    app.run(debug=True)
