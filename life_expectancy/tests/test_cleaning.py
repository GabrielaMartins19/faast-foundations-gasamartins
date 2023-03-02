"""Tests for the cleaning module"""
# pylint: disable=redefined-outer-name
from unittest.mock import patch, Mock
import pandas as pd
import pytest

from life_expectancy.cleaning import load_data, clean_data, save_data
from life_expectancy.tests.fixtures.mock import raw_data, expect_data

@pytest.fixture()
def fixture_raw_data():
    """Fixture row data"""
    return pd.DataFrame(raw_data())

@pytest.fixture()
def fixture_expected_data():
    """Fixture expected data"""
    return pd.DataFrame(expect_data())

@patch('pandas.read_csv')
def test_load_data(read_table_mock: Mock, fixture_raw_data):
    """Test load data"""
    read_table_mock.return_value = fixture_raw_data
    results = load_data()
    read_table_mock.assert_called_once()

    pd.testing.assert_frame_equal(results, fixture_raw_data)

def test_clean_data(fixture_raw_data, fixture_expected_data):
    """Test clean data"""
    pt_life_expectancy_data = clean_data(
        fixture_raw_data,
        region='PT'
    ).reset_index(drop=True)

    pd.testing.assert_frame_equal(
        pt_life_expectancy_data, fixture_expected_data
    )

def test_save_data(fixture_expected_data, capfd):
    """Test save data"""
    with patch.object(fixture_expected_data, 'to_csv') as to_csv_mock:
        to_csv_mock.side_effect = print('Data saved', end="")
        save_data(
            fixture_expected_data
        )
        to_csv_mock.assert_called_once()

        # capfd: capture stdout
        out, _ = capfd.readouterr()
        assert out == "Data saved"
