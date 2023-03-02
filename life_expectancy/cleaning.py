'''
Cleaning data script.
'''
import argparse
import pathlib
import pandas as pd

def load_data() -> pd.DataFrame:
    '''
    Function to load data.
    :return: DataFrame with loaded data from path.
    '''
    # define path
    read_path = pathlib.Path(__file__).parent / 'data/eu_life_expectancy_raw.tsv'

    # load data
    df_data = pd.read_csv(read_path, sep='[,\t]', engine='python')

    return df_data

def clean_data(data_toclean: pd.DataFrame, region) -> pd.DataFrame:
    '''
    Function to clean_data.
    :param data_toclean: DataFrame data loaded to clean.
    :param region: String of region we want to filter. By default is 'PT'.
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

    # value as float and remove NaNs
    data_toclean['value'] = data_toclean['value'].str.split(' ', n=1).str.get(0)
    data_toclean = data_toclean[data_toclean.value != ':']
    data_toclean['value'] = data_toclean['value'].astype(float)

    # filter only PT region
    data_toclean = data_toclean[data_toclean['region'] == region]

    return data_toclean

def save_data(data_tosave: pd.DataFrame) -> None:
    '''
    Function to save data.
    :param data_tosave: DataFrame with data to save.
    '''
    # write to csv
    write_path = pathlib.Path(__file__).parent / 'data/pt_life_expectancy.csv'
    data_tosave.to_csv(write_path, index=False)

def main(region: str = 'PT') -> None:
    '''
    Main function.
    :param region: String with the region to filter data. By default 'PT'.
    '''
    # load data
    data = load_data()

    # clean data
    data_cleaned = clean_data(data, region)

    # save data
    save_data(data_cleaned)

if __name__ == "__main__":  # pragma: no cover

    # create parser
    parser = argparse.ArgumentParser()
    # add the argument region
    parser.add_argument('--r', type=str, help='Region', default='PT')
    # parse args
    args = parser.parse_args()
    # call main with optional arg
    main(args.r)
