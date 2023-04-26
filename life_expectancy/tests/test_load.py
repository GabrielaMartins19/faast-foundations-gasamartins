"""Tests for load data"""
from unittest.mock import patch, Mock
from life_expectancy.load_data import DataOptions
from . import OUTPUT_DIR

@patch('life_expectancy.load_data.pd.read_csv')
def test_load_data(read_mock: Mock, fixture_raw_data):
    """Test load data"""
    read_mock.return_value = fixture_raw_data
    data = DataOptions(
        filename='test.tsv',
        path=OUTPUT_DIR
    )
    data.load_data()
    read_mock.assert_called_once()
