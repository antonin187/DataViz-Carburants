import pandas as pd
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

csv = pd.read_csv('../cleaned_Prix_carburants_France_instantane.csv', delimiter=';', on_bad_lines='skip', dtype = {'longitude': float, 'latitude': float})

X_geom = []
y_geom = []

for row in csv['geom']:
    coordonnees = row.split(", ")

    X_geom.append(float(coordonnees[1]))
    y_geom.append(float(coordonnees[0]))

m = Basemap(projection='merc', resolution='l', llcrnrlat=41.0, urcrnrlat=51.0,
            llcrnrlon=-5.0, urcrnrlon=10.0)

X, y = m(X_geom, y_geom)

m.scatter(X, y, marker='D',color='m', zorder=5)

m.fillcontinents(color='coral',lake_color='aqua')
m.drawmapboundary(fill_color='aqua')

plt.title("Polyconic Projection")
plt.show()