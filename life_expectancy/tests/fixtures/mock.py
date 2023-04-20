"""Mock file"""
import pathlib
import pytest
import pandas as pd

path = pathlib.Path(__file__).parent

@pytest.fixture()
def fixture_raw_data() -> pd.DataFrame:
    """
    Load raw data.
    :return: DataFrame with raw data.
    """
    return pd.read_csv(path / 'data_raw.csv')

@pytest.fixture()
def fixture_loaded_data() -> pd.DataFrame:
    """
    Load loaded data.
    :return: DataFrame with loaded data.
    """
    return pd.read_csv(path / 'data_loaded.csv')

@pytest.fixture()
def fixture_expected_data() -> pd.DataFrame:
    """
    Load expected data.
    :return: DataFrame with expected data.
    """
    return pd.read_csv(path / 'data_expected.csv')
