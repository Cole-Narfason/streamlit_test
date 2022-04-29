import streamlit as st
import pydeck as pdk

DATA = 'usa.geojson'

layer = pdk.Layer(
    'GeoJsonLayer',  # `type` positional argument is here
    DATA,
)

# Set the viewport location
view_state = pdk.ViewState(
    longitude=-1.415,
    latitude=52.2323,
    zoom=6,
    min_zoom=5,
    max_zoom=15,
    pitch=40.5,
    bearing=-27.36)

# Combined all of it and render a viewport
st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state))
#r.to_html('hexagon-example.html')
#st.pydeck_chart(r)







