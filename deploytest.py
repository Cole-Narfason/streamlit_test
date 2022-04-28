# import module
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import plotly.graph_objects as go
import plotly.express as px
from streamlit_keplergl import keplergl_static
from keplergl import KeplerGl

 
# Title
st.title("Streamlit Deploy Test")

st.header('Choose Area of Interest')

Lat = st.number_input("Please enter AOI Latitude")
Long = st.number_input("Please enter AOI Longitude")

#Maps
map_1 = KeplerGl(height = 800)
map_2 = KeplerGl(height = 800)




#Config
if Lat and Long != 0:

    config = {
    'version': 'v1',
    'config': {
        'mapState': {
            'latitude': Lat,
            'longitude': Long,
            'zoom': 7
        }}}

else:
    config = {
    'version': 'v1',
    'config': {
        'mapState': {
            'latitude': 39.367545,
            'longitude': -99.423799,
            'zoom': 3.2
        }}}

map_1.config = config
#map_2.config = config

st.header("Ambient Temperature")
# GeoJSON as string
with open('TestSurfaceTemp.geojson', 'r') as f:
    geojson = f.read()

map_1.add_data(data=geojson, name='AVG Annual Temperature')

keplergl_static(map_1)



