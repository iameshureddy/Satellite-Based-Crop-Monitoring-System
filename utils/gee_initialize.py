import ee

def initialize_gee():
    try:
        ee.Initialize()
    except:
        ee.Authenticate()
        ee.Initialize()
