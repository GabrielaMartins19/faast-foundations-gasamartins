"""Tests for load data"""
# pylint: disable=redefined-outer-name
from unittest.mock import patch, Mock
from life_expectancy.load_data import DataOptions
from .fixtures.mock import fixture_raw_data, fixture_loaded_data
from . import OUTPUT_DIR

@patch('life_expectancy.load_data.pd.read_csv')
def test_load_data(read_mock: Mock, fixture_raw_data, fixture_loaded_data):
    """Test load data"""
    read_mock.return_value = fixture_raw_data
    data = DataOptions(
        filename='test.tsv',
        path=OUTPUT_DIR
    )
    data.load_data()
    read_mock.assert_called_once()
