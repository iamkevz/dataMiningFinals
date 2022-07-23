import pandas as pd
import matplotlib.pyplot as plt


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