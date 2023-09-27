import os
import pandas as pd
import requests


class CarData:
    


    # define the init
    def __init__(self, name: str) -> None:
        self.name = name
        self.brands_list = []

    
    # collect the brand names
    def add_brands(self, *args) -> None:

        # iterate for the brands
        for brand in args:
            self.brands_list.append(brand)

        print("Succesfully added brands")


    # function to import data from the rdw
    def import_cars_by_brand(brand: str, more_data: bool=False) -> pd.DataFrame:

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

        # create a DataFrame from the list
        df = pd.DataFrame(data)
        return df
    

    # method for executing the API requests and saving the results to a list
    def execute_api_calls(self) -> None:
        self.df_list = []
        # execute the api call for every brand in the list
        car_brands_list = self.brands_list

        for car_brand in car_brands_list:
            df = self.import_cars_by_brand(car_brand)   
            self.df_list.append(df)

    
    def transform_df(df: pd.DataFrame, group_data=False) -> pd.DataFrame:
        '''
        Accepts a list and converts it to a pandas DataFrame
        
        '''

    
        # create list of columns
        selected_columns = ['kenteken', 'merk', 'handelsbenaming', 'catalogusprijs', 'datum_tenaamstelling']
        
        df_sub_cols = df[selected_columns].copy() # add .copy() to get rid of the warnings and ceveat messsages
        # convert catalogusprijs to numeric
        df_sub_cols['catalogusprijs'] = df_sub_cols['catalogusprijs'].astype(float)

        # convert datum_tenaamstelling to a date timme data type
        df_sub_cols['datum_tenaamstelling'] = pd.to_datetime(df_sub_cols['datum_tenaamstelling'], 
                                                            format = "%Y%m%d")
        
        # get the month from the date
        df_sub_cols['maand_tenaamstelling'] = df_sub_cols['datum_tenaamstelling'].dt.month
        df_sub_cols['week_tenaamstelling'] = df_sub_cols['datum_tenaamstelling'].dt.isocalendar()['week']

        # replace NaN for 0
        df_sub_cols['catalogusprijs'] = df_sub_cols['catalogusprijs'].fillna(0)

        # filter, remove cars with a catalogusprijs of 0
        df_sub_cols_filtered = df_sub_cols.query("catalogusprijs > 0")

        # if we want to group the data
        if group_data:

            # grouping and summarizing data --> Data Pipeline
            group_columns = ['handelsbenaming', 'catalogusprijs']

            df_sub_cols_filtered_grouped = (
                df_sub_cols_filtered[group_columns]
                .groupby('handelsbenaming')
                .mean('catalogusprijs')
                .rename(columns={'catalogusprijs': 'gemiddelde_catalogusprijs'})
                .sort_values(by='gemiddelde_catalogusprijs', ascending=False)
                .reset_index()
            )
            
            # return the grouped DataFrame
            return df_sub_cols_filtered_grouped

        # return the un-grouped DataFram
        return df_sub_cols_filtered
    

    # method for converting all the DataFrames in the list
    def transform_df_all(self):

        # iterate over every DataFrame for the conversion
        df_list = self.df_list

        for idx, df in enumerate(df_list):
            df_converted = self.transform_df(df)
            self.df_list[idx] = df_converted

        print(f"✅ Done with converting {len(self.df_list)} DataFrames")

    
    # method for combining the DataFrame list to a single DataFrame
    def combine_dfs(self) -> None:
        df_list = self.df_list


        # combine the DataFrames to a single DataFrame
        df_combined = pd.concat(df_list)

        # df list is now the combined DataFrame
        self.combined_df = df_combined

    
    def export_df_to_csv(df: pd.DataFrame, brand_name="car_export") -> None:
        '''
        Export the data frame to a csv file
        '''
        
        # specify the file name
        file_path = f"data/{brand_name}/{brand_name}.csv"

        # list the files and folders in the current directory
        files_folders = os.listdir("data")

        # check if the new directory already exists
        brand_folder = brand_name

        if brand_folder not in files_folders:
            os.mkdir(brand_folder)
        
        # export the pandas DataFrame
        print("🕒 Export data")
        df.to_csv(file_path, sep=";", index=False)
        print("✅ Successfully exported data")


    # method for exporting the DataFrames
    def export_dfs(self, export_type: str = "all") -> None:

        if export_type == "all":
            print("Exporting the seperate DataFrames")
            df_list = self.df_list

            for df in df_list:
                self.export_df_to_csv(df)
        else:
            print("Exporting the combined DataFrame")
            self.export_df_to_csv(self.combined_df)


