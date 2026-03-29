import pandas as pd
import geopandas as gpd
import folium

wards = gpd.read_file('data_files/NI_Wards.shp')
translink_br = gpd.read_file('data_files/translink-stations-ni.geojson')



m = wards.explore()

rail_st = translink_br['Type'] == 'R'
i_st = translink_br['Type'] == 'I'
bus_st = translink_br['Type'] == 'B'


translink_br.head()

rail_args = {
    'm': m, # add the markers to the same map we just created
    'marker_type': 'marker', # use a marker for the points, instead of a circle
    'popup': True, # show the information as a popup when we click on the marker
    'legend': False, # don't show a separate legend for the point layer
    'marker_kwds': {'icon': folium.Icon(color='red', icon='train', prefix='fa')} # make the markers red with a plane icon from FA
}

i_args = {
    'm': m, # add the markers to the same map we just created
    'marker_type': 'marker', # use a marker for the points, instead of a circle
    'popup': True, # show the information as a popup when we click on the marker
    'legend': False, # don't show a separate legend for the point layer
    'marker_kwds': {'icon': folium.Icon(color='blue', icon='i', prefix='fa')} # make the markers red with a plane icon from FA
}

bus_args = {
    'm': m, # add the markers to the same map we just created
    'marker_type': 'marker', # use a marker for the points, instead of a circle
    'popup': True, # show the information as a popup when we click on the marker
    'legend': False, # don't show a separate legend for the point layer
    'marker_kwds': {'icon': folium.Icon(color='green', icon='bus', prefix='fa')} # make the markers red with a plane icon from FA
}

#locate the data, then associate it with the previously designed markers
m = ()
    translink_br[translink_br['Type'] == 'R'].explore(**rail_args),
    translink_br[translink_br['Type'] == 'I'].explore(**i_args),
    translink_br[translink_br['Type'] == 'B'].explore(**bus_args)
)