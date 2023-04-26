"""Save data"""
import pathlib
import pandas as pd

def save_data(data_tosave: pd.DataFrame) -> None:
    '''
    Function to save data.
    :param data_tosave: DataFrame with data to save.
    '''
    # write to csv
    write_path = pathlib.Path(__file__).parent / 'data/pt_life_expectancy.csv'
    data_tosave.to_csv(write_path, index=False)
