"""Test main"""
# pylint: disable=redefined-outer-name
# pylint: disable=unused-import
from unittest.mock import patch, Mock
from life_expectancy.main import Countries, main
from .fixtures.mock import fixture_raw_data

def test_countries():
    """Test countries"""
    countries_list = Countries.list()
    countries_expected = [
        'AUSTRIA',
        'BELGIUM',
        'BULGARIA',
        'SWITZERLAND',
        'CYPRUS',
        'CZECHIA',
        'DENMARK',
        'ESTONIA',
        'GREECE',
        'SPAIN',
        'FINLAND',
        'FRANCE',
        'CROACIA',
        'HUNGARY',
        'ICELAND',
        'ITALY',
        'LIECHTENSTEIN',
        'LITHUANIA',
        'LUXEMBOURG',
        'LATVIA',
        'MALTA',
        'NETHERLANDS',
        'NORWAY',
        'POLAND',
        'PORTUGAL',
        'ROMANIA',
        'SWEDEN',
        'SLOVENIA',
        'SLOVAKIA',
        'GERMANY',
        'ALBANIA',
        'IRELAND',
        'MONTENEGRO',
        'NORTH_MACEDONIA',
        'SERBIA',
        'ARMENIA',
        'AZERBAIJAN',
        'GEORGIA',
        'TURKEY',
        'UKRAINE',
        'BELARUS',
        'UNITED_KINGDOM',
        'KOSOVO',
        'FRANCE_METROPOLITAN',
        'MOLDOVA',
        'SAN_MARINO',
        'RUSSIA'
    ]
    assert not set(countries_list) ^ set(countries_expected)

@patch('life_expectancy.main.save_data')
@patch('life_expectancy.clean_save.pd.read_csv')
def test_main(read_mock: Mock, write_mock: Mock, fixture_raw_data):
    """Test main"""
    read_mock.return_value = fixture_raw_data
    main('test.tsv', 'Portugal')
    read_mock.assert_called_once()
    write_mock.assert_called_once()
