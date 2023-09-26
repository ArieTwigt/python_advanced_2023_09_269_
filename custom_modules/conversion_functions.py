import pandas as pd


def convert_list_to_df(list_to_convert: list) -> pd.DataFrame:
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
    df_sub_cols = df[selected_columns]
    pass