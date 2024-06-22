import streamlit as st
import geopandas as gpd
import folium
from streamlit_folium import st_folium

# Mengubah file shp ke dalam geojson
gdf = gpd.read_file('Banggae\KecamatanBanggae.shp')
gdf.to_file('KecBanggae.geojson', driver='GeoJSON')

def create_map():
    # Baca file GeoJSON
    gdf = gpd.read_file('KecBanggae.geojson')
    
    # Dapatkan koordinat tengah untuk pemetaan
    center = [gdf.geometry.centroid.y.mean(), gdf.geometry.centroid.x.mean()]

    # Buat peta folium
    m = folium.Map(location=center, zoom_start=13)

    folium.GeoJson(gdf).add_to(m)
    return m

st.title("Peta Kecematan Banggae")
map = create_map()
st_folium(map, width=700, height=500)
