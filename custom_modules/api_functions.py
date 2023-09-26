import requests


# function to import data from the rdw
def import_cars_by_brand(brand: str) -> list:

    # uppercase the brand
    brand_upper = brand.upper()

    # define the endpoint
    endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?merk={brand_upper}"
    
    # execute the request
    response = requests.get(endpoint)

    # get the data from the response
    data = response.json()
    
    # check if the data is not empty
    if len(data) == 0:
        raise ValueError(f"Did not find any cars for {brand}")

    return data