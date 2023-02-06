import os
import urllib.request
import zipfile
import pandas as pd
from shapely.geometry import Point
import geopandas as gpd

# Here's the list of countries in the Geonames data dump website
country_list = ["AD","AE","AF","AG","AI","AL","AM","AN","AO","AQ","AR","AS","AT","AU","AW","AX","AZ","BA","BB","BD","BE","BF","BG","BH","BI","BJ","BL","BM","BN","BO","BQ","BR","BS","BT","BV","BW","BY","BZ","CA","CC","CD","CF","CG","CH","CI","CK","CL","CM","CN","CO","CR","CS","CU","CV","CW","CX","CY","CZ","DE","DJ","DK","DM","DO","DZ","EC","EE","EG","EH","ER","ES","ET","FI","FJ","FK","FM","FO","FR","GA","GB","GD","GE","GF","GG","GH","GI","GL","GM","GN","GP","GQ","GR","GS","GT","GU","GW","GY","HK","HM","HN","HR","HT","HU","ID","IE","IL","IM","IN","IO","IQ","IR","IS","IT","JE","JM","JO","JP","KE","KG","KH","KI","KM","KN","KP","KR","KW","KY","KZ","LA","LB","LC","LI","LK","LR","LS","LT","LU","LV","LY","MA","MC","MD","ME","MF","MG","MH","MK","ML","MM","MN","MO","MP","MQ","MR","MS","MT","MU","MV","MW","MX","MY","MZ","NA","NC","NE","NF","NG","NI","NL","NO","NP","NR","NU","NZ","OM","PA","PE","PF","PG","PH","PK","PL","PM","PN","PR","PS","PT","PW","PY","QA","RE","RO","RS","RU","RW","SA","SB","SC","SD","SE","SG","SH","SI","SJ","SK","SL","SM","SN","SO","SR","SS","ST","SV","SX","SY","SZ","TC","TD","TF","TG","TH","TJ","TK","TL","TM","TN","TO","TR","TT","TV","TW","TZ","UA","UG","UM","US","UY","UZ","VA","VC","VE","VG","VI","VN","VU","WF","WS","XK","YE","YT","YU","ZA","ZM","ZW"]

# This code runs the run_download_tsv_to_shapefile
run_download_tsv_to_shapefile(country_list)


def run_download_tsv_to_shapefile(string_list):
    for string in string_list:
        download_tsv_to_shapefile(string)


def download_tsv_to_shapefile(country_code):
    # Download the zip file
    url = f"http://download.geonames.org/export/dump/{country_code}.zip"
    urllib.request.urlretrieve(url, f"{country_code}.zip")
    
    # Uncompress the zip file
    with zipfile.ZipFile(f"{country_code}.zip", "r") as zip_ref:
        zip_ref.extractall(".")
    
    # Load the txt file into a pandas dataframe
    column_names = ["geonameid","name","asciiname","alternatenames","latitude","longitude","feature_class","feature_code","country_code","cc2","admin1_code","admin2_code","admin3_code","admin4_code","population","elevation","dem","timezone","modification_date"]
    df = pd.read_csv(f"{country_code}.txt", sep="\t", header=None, names=column_names)
    
    # Create a Shapely Point object for each row in the dataframe
    df["geometry"] = [Point(x, y) for x, y in zip(df["longitude"], df["latitude"])]
    
    # Convert the pandas dataframe to a GeoDataFrame
    gdf = gpd.GeoDataFrame(df, geometry="geometry")
    
    # Make a new folder for the shapefile files
    os.makedirs(country_code, exist_ok=True)
    
    # Save the GeoDataFrame as a shapefile in the new folder
    gdf.to_file(f"{country_code}/{country_code}.shp", driver="ESRI Shapefile")
    
    # Clean up the txt file and the zip file
    os.remove(f"{country_code}.txt")
    os.remove(f"{country_code}.zip")
    os.remove(f"readme.txt")
