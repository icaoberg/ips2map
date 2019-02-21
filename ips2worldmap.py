import argparse

######## Argument Parsing ##########
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="name of input file (.txt)", default = "ip.txt")
parser.add_argument("-o", "--output", help="name of output file (.eps)", default = "worldmap.eps")
parser.add_argument("-t", "--title", help="title of the map", default = " ")
parser.add_argument("-c", "--color", help="color of the markers", default = "red")
parser.add_argument("-m", "--marker", help="shape of the markers", default = "o")

args = parser.parse_args()

# if args.file:
# 	file = args.file
# if args.output:
# 	output = 

import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import matplotlib.cm
import math
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib.colors import Normalize
from ipToGeo import ipToGeo


fig, ax = plt.subplots(figsize=(10,20))

print('Setting up basemap')
m = Basemap(resolution='i', # c, l, i, h, f or None
	projection='merc',
	lat_1=45.,lat_2=55,lat_0=50,lon_0=-107,
        llcrnrlon=-180, llcrnrlat=-70, urcrnrlon=180, urcrnrlat=80)

print('Drawing map boundary')
m.drawmapboundary(fill_color='#45bcec')

print('Coloring continents')
m.fillcontinents(color='#f2f2f2',lake_color='#46bcec')
#m.drawcountries()
#m.drawstates()
#m.drawcoastlines()

print('Obtaining geographic information from IPs')
locations = ipToGeo(args.file)

print('Preparing plot')
scale = 0.5
plt.title("IP Addresses Around the World")
for k, v in locations.items():
	lon = v[0]
	lat = v[1]
	markerSize = scale*v[2]

	print('Adding to (lat,lon):(' + str(lat) + ',' + str(lon) + ') with marker size ' + str(markerSize)); 
	x, y = m(lat, lon)
	plt.plot(x, y, markersize = markerSize, color = args.color, marker = args.marker)
	#plt.text(x,y, bp, fontsize=8);

plt.savefig(args.output, bbox_inches = 'tight', format = 'eps', dpi = 1200)

