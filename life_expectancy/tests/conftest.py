"""Pytest configuration file"""
import pandas as pd
import pytest

from . import FIXTURES_DIR

@pytest.fixture(scope="session")
def pt_life_expectancy_expected() -> pd.DataFrame:
    """Fixture to load the expected output of the cleaning script"""
    return pd.read_csv(FIXTURES_DIR / "pt_life_expectancy_expected.csv")

@pytest.fixture()
def fixture_raw_data() -> pd.DataFrame:
    """
    Load raw data.
    :return: DataFrame with raw data.
    """
    return pd.read_csv(FIXTURES_DIR / 'data_raw.csv')

@pytest.fixture()
def fixture_loaded_data() -> pd.DataFrame:
    """
    Load loaded data.
    :return: DataFrame with loaded data.
    """
    return pd.read_csv(FIXTURES_DIR / 'data_loaded.csv')

@pytest.fixture()
def fixture_expected_data() -> pd.DataFrame:
    """
    Load expected data.
    :return: DataFrame with expected data.
    """
    return pd.read_csv(FIXTURES_DIR / 'data_expected.csv')
