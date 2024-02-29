import pandas as pd
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

csv = pd.read_csv('../cleaned_Prix_carburants_France_instantane.csv', delimiter=';', on_bad_lines='skip')

print(csv['geom'])

X = csv['longitude']
y = csv['latitude']

m = Basemap(llcrnrlon=-35.,llcrnrlat=-30,urcrnrlon=80.,urcrnrlat=50.,\
            resolution='l',area_thresh=1000.,projection='poly',\
            lat_0=0.,lon_0=20.)

x, Y = m(0, 0)

m.scatter(X, y, marker='D',color='m')
m.scatter(x, Y, marker='.', color='g')

m.fillcontinents(color='coral',lake_color='aqua')
m.drawmapboundary(fill_color='aqua') 

plt.title("Polyconic Projection")
plt.show()