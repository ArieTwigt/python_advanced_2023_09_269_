import requests


# function to import data from the rdw
def import_cars_by_brand(brand: str, more_data: bool=False) -> list:

    # uppercase the brand
    brand_upper = brand.upper()

    # define the endpoint
    endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?merk={brand_upper}"

    # modify if we want more data
    if more_data:
        print("⬇️ Getting more data")
        endpoint = endpoint + "&$limit=10000"
    
    # execute the request
    print("🕒Getting data from API")
    response = requests.get(endpoint)
    print("✅ Got data from API")

    # get the data from the response
    data = response.json()
    
    # check if the data is not empty
    if len(data) == 0:
        raise ValueError(f"Did not find any cars for {brand}")

    return data