import requests


# function to import data from the rdw
def import_cars_by_brand(brand: str) -> list:

    # define the endpoint
    endpoint = "https://opendata.rdw.nl/resource/m9d7-ebf2.json"
    
    # execute the request
    response = requests.get(endpoint)

    # get the data from the response
    data = response.json()
    
    return data