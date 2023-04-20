"""Load, clean and save data"""
import pathlib
import pandas as pd


def clean_data(data_toclean: pd.DataFrame) -> pd.DataFrame:
    '''
    Function to clean_data.
    :param data_toclean: DataFrame data loaded to clean.
    :return: DataFrame cleaned data.
    '''
    # rename column region
    data_toclean = data_toclean.rename(columns={data_toclean.columns[3]:"region"})

    # unpivot
    data_toclean = data_toclean.melt(
                ['unit', 'sex', 'age', 'region'],
                var_name = 'year',
                value_name = 'value'
    )

    # year as int
    data_toclean['year'] = data_toclean['year'].astype(int)

    # region PT
    data_toclean = data_toclean[data_toclean.region == 'PT']

    # value as float and remove NaNs
    data_toclean['value'] = data_toclean['value'].str.split(' ', n=1).str.get(0)
    data_toclean = data_toclean[data_toclean.value != ':']
    data_toclean['value'] = data_toclean['value'].astype(float)

    return data_toclean

def save_data(data_tosave: pd.DataFrame) -> None:
    '''
    Function to save data.
    :param data_tosave: DataFrame with data to save.
    '''
    # write to csv
    write_path = pathlib.Path(__file__).parent / 'data/pt_life_expectancy.csv'
    data_tosave.to_csv(write_path, index=False)
