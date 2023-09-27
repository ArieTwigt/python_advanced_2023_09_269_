from custom_modules.cardata import CarData

import argparse

# define a argument parser
parser = argparse.ArgumentParser()

# add arguments to the parser
parser.add_argument('--brands', 
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
    selected_brands = args.brands

    group_data = args.group_data

    # initate a CarData instance
    car_import = CarData("car import")

    # define the brands
    car_import.add_brands(selected_brands)

    # execute the api call
    car_import.execute_api_calls()

    # transform the DataFrames
    car_import.transform_df_all(group_data=group_data)

    # combine the DataFrame
    car_import.combine_dfs()

    # export the DataFrames
    car_import.export_dfs()
    pass