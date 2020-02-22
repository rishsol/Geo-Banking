import requests
import json
from pprint import pprint
import geopandas
import csv

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

#stuff = json_datab['geocode'][1]
for i in range(len(json_datab)):
   geo_tag_listb.append(json_datab[i]['geocode'])

for i in range(len(json_datam)):
    try:
        if json_datam[i]['geocode']['lng'] != 0:
            geo_tag_listm.append(json_datam[i]['geocode'])
    except:
        pass

with open("Merchants_Data.csv", 'w', newline = "") as fout:
    dict_writer = csv.DictWriter(fout, fieldnames=geo_tag_listm[0].keys())
    dict_writer.writeheader()
    dict_writer.writerows(geo_tag_listm)

with open("Banks_Data.csv", 'w', newline = "") as fout:
    dict_writer = csv.DictWriter(fout, fieldnames=geo_tag_listb[0].keys())
    dict_writer.writeheader()
    dict_writer.writerows(geo_tag_listb)