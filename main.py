from custom_modules.api_functions import import_cars_by_brand
from custom_modules.conversion_functions import convert_list_to_df
from custom_modules.export_functions import export_df_to_csv

if __name__ == "__main__":
    selected_brand = input("Type in a brand:\n")
    cars_list = import_cars_by_brand(selected_brand, more_data=False)
    cars_df = convert_list_to_df(cars_list, group_data=True)
    export_df_to_csv(cars_df, selected_brand)