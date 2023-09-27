import pandas as pd
import os

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