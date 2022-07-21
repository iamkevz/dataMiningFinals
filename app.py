import pandas as pd
from flask import Flask
from flask import render_template
import folium
app = Flask(__name__)


@app.route("/")
def base():
    #base map
    map = folium.Map(
        location=[14.164862797000069, 120.8616300000001],
        zoom_start=6
    )
    tweet = pd.read_csv('Cleaned.csv')
    a_list = tweet[['category', 'lat', 'long']].values.tolist()
    fg = folium.FeatureGroup(name='tweet_map')
    for i in a_list:
        if i[0].find("Medical")!=-1:
            fg.add_child(folium.Marker(location=[i[2],i[1]],popup=i[0],icon=folium.Icon(color='red')))
        elif i[0].find("Food")!=-1:
            fg.add_child(folium.Marker(location=[i[2], i[1]], popup=i[0], icon=folium.Icon(color='green')))
        else:
            fg.add_child(folium.Marker(location=[i[2], i[1]], popup=i[0], icon=folium.Icon(color='blue')))
    map.add_child(fg)
    #map.save("templates/index.html")
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, port=5000)
