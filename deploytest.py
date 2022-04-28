# import module
import streamlit as st
import pandas as pd
import numpy as np
from streamlit_keplergl import keplergl_static
#import keplergl
from keplergl import KeplerGl

 
# Title
st.title("Streamlit Deploy Test")

st.header('Choose Area of Interest')

Lat = st.number_input("Please enter AOI Latitude")
Long = st.number_input("Please enter AOI Longitude")









