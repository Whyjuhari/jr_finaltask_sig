import streamlit as st
import geopandas as gpd
import folium
from streamlit_folium import st_folium

# # mengubah file shp ke dalam geojson
# gdf = gpd.read_file('Banggae\KecamatanBanggae.shp')
# gdf.to_file('KecBanggae.geojson', driver='GeoJSON')
    
    

# memberikan warna berdasarkan jumlah penduduk
def color_function(feature):
    jumlah_penduduk = feature['properties']['JUMLAH_PEN']
    
    # berdasarkan yang di ambil dari file .geoJson
    if jumlah_penduduk <= 840:
        return '#E6E6FA'  
    elif 840 < jumlah_penduduk <= 1564:
        return '#D8BFD8' 
    elif 1564 < jumlah_penduduk <= 1687:
        return '#B0C4DE'  
    elif 1687 < jumlah_penduduk <= 1966:
        return '#87CEEB'  
    elif 1966 < jumlah_penduduk <= 2194:
        return '#6495ED'  
    elif 2194 < jumlah_penduduk <= 5655:
        return '#4169E1'  
    else:
        return '#191970'  
    
def create_map():
    # mengambil file geosjon
    gdf = gpd.read_file('KecBanggae.geojson')

    # mendapatkan koordinat tengah untuk pemetaan
    center = [gdf.geometry.centroid.y.mean(), gdf.geometry.centroid.x.mean()]
    
    # membuat peta folium
    m = folium.Map(location=center, zoom_start=13)
    
    # menambahkan layer GeoJSON 
    folium.GeoJson(
        gdf,
        style_function=lambda feature: {
            'fillColor': color_function(feature),
            'color': 'black',
            'weight': 2,
            'fillOpacity': 0.7
        },
        tooltip=folium.GeoJsonTooltip(
            fields=["DESA"],
            aliases=["Nama Desa: "],
            localize=True
        ),
    ).add_to(m)
    
    # menampilkan label berdasarkan desa
    for _, row in gdf.iterrows():
        folium.Marker(
            location=[row.geometry.centroid.y, row.geometry.centroid.x],
            popup=row['DESA'],
            icon=folium.DivIcon(
                html=f"""<div style="font-weight:bold; font-size:12px;">{row['DESA']}</div>""",
                icon_size=(150, 36),
                icon_anchor=(75, 18)
            )
        ).add_to(m)
    



    folium.GeoJson(gdf).add_to(m)
    return m

st.title("Penerapan streamlit map dengan map")
map = create_map()
st_folium(map, width=700, height=500)
