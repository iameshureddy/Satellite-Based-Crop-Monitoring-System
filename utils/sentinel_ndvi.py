import ee
from utils.gee_initialize import initialize_gee

initialize_gee()

def get_ndvi(lat, lon):
    point = ee.Geometry.Point([lon, lat])

    img = (
        ee.ImageCollection("COPERNICUS/S2_SR")
        .filterBounds(point)
        .sort("CLOUDY_PIXEL_PERCENTAGE")
        .first()
    )

    ndvi = img.normalizedDifference(['B8','B4'])

    stats = ndvi.reduceRegion(
        reducer=ee.Reducer.mean(),
        geometry=point.buffer(500),
        scale=10
    )

    return stats.get('nd').getInfo()
