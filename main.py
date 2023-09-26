from custom_modules.api_functions import import_cars_by_brand
from custom_modules.conversion_functions import convert_list_to_df

if __name__ == "__main__":
    cars_list = import_cars_by_brand("audi", more_data=True)
    cars_df = convert_list_to_df(cars_list, group_data=True)
    pass