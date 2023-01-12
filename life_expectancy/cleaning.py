'''
Cleaning data script.
'''
import argparse
import pathlib
import pandas as pd

def clean_data(region: str = 'PT') -> None:
    '''
    Function to clean data from raw file.
    '''

    # define path
    read_path = pathlib.Path(__file__).parent / 'data/eu_life_expectancy_raw.tsv'

    # load data
    data = pd.read_csv(read_path, sep='[,\t]', engine='python')

    # rename column region
    data = data.rename(columns={data.columns[3]:"region"})

    # unpivot
    data = data.melt(
                ['unit', 'sex', 'age', 'region'],
                var_name = 'year',
                value_name = 'value'
    )

    # year as int
    data['year'] = data['year'].astype(int)

    # value as float and remove NaNs
    data['value'] = data['value'].str.split(' ', n=1).str.get(0)
    data = data[data.value != ':']
    data['value'] = data['value'].astype(float)

    # filter only PT region
    data = data[data['region'] == region]

    # write to csv
    write_path = pathlib.Path(__file__).parent / 'data/pt_life_expectancy.csv'
    data.to_csv(write_path, index=False)

if __name__ == "__main__":  # pragma: no cover

    # create parser
    parser = argparse.ArgumentParser()
    # add the argument region
    parser.add_argument('--r', type=str, help='Region')
    # parse args
    args = parser.parse_args()
    # call clean data with optional arg
    if args.r:
        clean_data(args.r)
    else:
        clean_data()
