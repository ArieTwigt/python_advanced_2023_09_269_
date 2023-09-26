from custom_modules.api_functions import import_cars_by_brand
from custom_modules.conversion_functions import convert_list_to_df
from custom_modules.export_functions import export_df_to_csv

import argparse

# define a argument parser
parser = argparse.ArgumentParser()

# add arguments to the parser
parser.add_argument('--brand', 
                    '-b',
                    type=str,
                    required=True,
                    help="A brand name (required)")

parser.add_argument('--more_data',
                    '-m',
                    type=bool,
                    required=False,
                    default=False,
                    help="Should the API return 10000 rows instead of 1000?")

parser.add_argument('--group_data', 
                    '-g',
                    type=bool,
                    required=False,
                    default=False,
                    help="Should the data by grouped?")

parser.add_argument('--show_type', 
                    '-s',
                    type=str, 
                    required=False,
                    choices=['csv', 'print'],
                    default='print',
                    help="How to return the results")

# parse the arguments
args = parser.parse_args()

# execute the code
if __name__ == "__main__":
    selected_brand = args.brand
    cars_list = import_cars_by_brand(selected_brand, args.more_data)
    cars_df = convert_list_to_df(cars_list, args.group_data)

    show_type = args.show_type

    if show_type == "csv":
        export_df_to_csv(cars_df, selected_brand)
    elif show_type == "print":
        print(cars_df)
    else:
        pass