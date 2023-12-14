# This file is aiming to convert the drought data provided by EEA and convert them to a CSV with each measurement in a row
#
#
#

import io
from urllib.request import urlopen
from zipfile import ZipFile
import pandas as pd


def read_zip(zip_url):
    resp = urlopen(zip_url)
    zf = ZipFile(io.BytesIO(resp.read()))
    print(zf.namelist()[1])
    return zf.read(zf.namelist()[1])

df = pd.read_excel(io.BytesIO(read_zip("https://sdi.eea.europa.eu/datashare/s/Knxtr2akXfizFHa/download")),'Data_km2')

df_drough_cols = ['country','year', 'drought_impact']
drought_data = []
for i,r in df.iterrows():
    if (i==8):
        columns = r
        print(columns[0])
    if (i > 10):
        for year in range(3,26):
            print(str(r[1])+" "+ str(columns[year]) +" "+ str(r[year]))
            drought_data.append([r[1], columns[year] , r[year]])

drough_df = pd.DataFrame(drought_data, columns= df_drough_cols )

drough_df.to_csv("drought.csv", index=False)