import ee
from utils.gee_initialize import initialize_gee

initialize_gee()

def get_ndvi_map(lat, lon):
    region = ee.Geometry.Point([lon, lat]).buffer(1000)

    img = (
        ee.ImageCollection("COPERNICUS/S2_SR")
        .filterBounds(region)
        .sort("CLOUDY_PIXEL_PERCENTAGE")
        .first()
    )

    ndvi = img.normalizedDifference(['B8','B4'])

    url = ndvi.getThumbURL({
        'min':0,
        'max':1,
        'region':region,
        'dimensions':512,
        'palette':['red','yellow','green']
    })

    return url
