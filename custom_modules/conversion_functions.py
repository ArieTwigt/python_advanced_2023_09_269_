import pandas as pd


def convert_list_to_df(list_to_convert: list, group_data=False) -> pd.DataFrame:
    '''
    Accepts a list and converts it to a pandas DataFrame
    
    '''

    # convert the list to a pandas DataFrame
    df = pd.DataFrame(list_to_convert)

    # analyse methoden
    # eerste 5 regels laten zien
    #df.head()

    # overzicht van kolommen en data types
    #df.info()

    # overzicht van kolommen
    #df.columns

    # selecting a column 
    #df['merk']

    # create list of columns
    selected_columns = ['kenteken', 'merk', 'handelsbenaming', 'catalogusprijs', 'datum_tenaamstelling']
    
    df_sub_cols = df[selected_columns].copy() # add .copy() to get rid of the warnings and ceveat messsages

    # convert columns to the right types
    # check the types
    #df_sub_cols.dtypes

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



    #df_sub_cols = df_sub_cols.copy()

    # is numeric now, can apply calculation or statistical functions
    # df_sub_cols['catalogusprijs'].mean()
    # df_sub_cols['catalogusprijs'].max()
    # df_sub_cols['catalogusprijs'].sum()


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

    # return from the function
