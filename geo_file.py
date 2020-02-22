import requests
import json
from pprint import pprint
import geopandas as gpd
import descartes
from shapely.geometry import Point, Polygon


addressList = []
addressStringList = []

urlc = 'http://api.reimaginebanking.com/customers?key=3bb6dcc2cfc7ec704cfd2678b2816209'
urlb = 'http://api.reimaginebanking.com/branches?key=3bb6dcc2cfc7ec704cfd2678b2816209'
urlm = 'http://api.reimaginebanking.com/merchants?key=3bb6dcc2cfc7ec704cfd2678b2816209'

json_datac = requests.get(urlc).json()
datab_data = requests.get(urlb)
json_datab = datab_data.json()
json_datam = requests.get(urlm).json()

geo_tag_listb = []
geo_tag_listm = []

# stuff = json_datab['geocode'][1]
for i in range(len(json_datab)):
    geo_tag_listb.append(json_datab[i]['geocode'])

for i in range(len(json_datam)):
    try:
        if json_datam[i]['geocode']['lng'] != 0:
            geo_tag_listm.append(json_datam[i]['geocode'])
    except:
        pass

world_map = gpd.read_file("TM_WORLD_BORDERS-0.3.shp")
fig, ax = plt.subplots(figsize=(15, 15))
# geometry = [Point(xy) for xy in zip(geo_tag_listm['lng'],geo_tag_listm['lat'])]
newList = []
for i in range(len(geo_tag_listm)):
    a_tup = (geo_tag_listm[i]['lng'], geo_tag_listm[i]['lat'])
    newList.append(Point(a_tup))

