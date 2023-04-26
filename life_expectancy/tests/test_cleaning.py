"""Tests for cleaning"""
from unittest.mock import patch
import pandas as pd
from life_expectancy import clean, save

def test_clean_data(fixture_loaded_data, fixture_expected_data):
    """
    Test load data.
    """
    results = clean.clean_data(fixture_loaded_data).reset_index(drop=True)

    pd.testing.assert_frame_equal(results, fixture_expected_data)

def test_save_data(fixture_expected_data, capfd):
    """
    Test save data
    """
    with patch.object(fixture_expected_data, 'to_csv') as to_csv_mock:
        to_csv_mock.side_effect = print('Data saved', end="")
        save.save_data(
            fixture_expected_data
        )
        to_csv_mock.assert_called_once()

        # capfd: capture stdout
        out, _ = capfd.readouterr()
        assert out == "Data saved"
