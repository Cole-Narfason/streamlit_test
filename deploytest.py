import streamlit as st
import leafmap.kepler as leafmap
m = leafmap.Map(center=[40, -100], zoom=2, height=600, widescreen=False)
m.to_streamlit(width=800, height=800)








