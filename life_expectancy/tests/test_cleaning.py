"""Tests for the cleaning module"""
import pandas as pd
import pytest
from unittest.mock import patch, Mock

from life_expectancy.cleaning import main, load_data, clean_data
from life_expectancy.tests.fixtures.mock import raw_data, expect_data

from . import OUTPUT_DIR

@pytest.fixture
def fixture_raw_data():
    return pd.DataFrame(raw_data())

@pytest.fixture
def fixture_expected_data():
    return pd.DataFrame(expect_data())

@patch('pandas.read_csv')
def test_load_data(read_table_mock: Mock, fixture_raw_data):
    read_table_mock.return_value = fixture_raw_data
    results = load_data()
    read_table_mock.assert_called_once()

    pd.testing.assert_frame_equal(results, fixture_raw_data)


def test_clean_data(fixture_raw_data, fixture_expected_data):
    pt_life_expectancy_data = clean_data(
        fixture_raw_data,
        region='PT'
    ).reset_index(drop=True)

    pd.testing.assert_frame_equal(
        pt_life_expectancy_data, fixture_expected_data
    )
