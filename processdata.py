# Importing the pandas package.
import pandas as pd


class clean:

    def processdata(filename):
        # Loading and reading the CSV file.
        tweet = pd.read_csv(filename)
        a_list = tweet[['category', 'lat', 'long']].values.tolist()
        return a_list
