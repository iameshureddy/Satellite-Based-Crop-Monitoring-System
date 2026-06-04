import folium
from folium.plugins import Draw
from streamlit_folium import st_folium

def draw_polygon():
    m = folium.Map(location=[20.5,78.9], zoom_start=5)
    Draw(export=True).add_to(m)
    return st_folium(m)
