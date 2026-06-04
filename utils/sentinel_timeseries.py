import ee
import pandas as pd
from utils.gee_initialize import initialize_gee

initialize_gee()

def ndvi_timeseries(lat, lon):
    point = ee.Geometry.Point([lon, lat])

    collection = (
        ee.ImageCollection("COPERNICUS/S2_SR")
        .filterBounds(point)
        .map(lambda img:
             img.normalizedDifference(['B8','B4'])
             .rename('NDVI')
             .set('date', img.date().format('YYYY-MM-dd')))
    )

    def extract(img):
        val = img.reduceRegion(ee.Reducer.mean(), point.buffer(500), 10)
        return ee.Feature(None, {'date':img.get('date'),'NDVI':val.get('NDVI')})

    data = collection.map(extract).getInfo()['features']

    df = pd.DataFrame([{
        'date': f['properties']['date'],
        'NDVI': f['properties']['NDVI']
    } for f in data])

    df['date'] = pd.to_datetime(df['date'])
    return df.sort_values('date')
