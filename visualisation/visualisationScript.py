import pandas as pd
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

csv = pd.read_csv('../Prix carburants France instantane.csv', delimiter=';', on_bad_lines='skip')

