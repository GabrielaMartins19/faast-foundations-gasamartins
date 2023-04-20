"""Main file"""
import pathlib
import argparse
from enum import Enum
from itertools import chain
from .load_data import DataOptions
from .clean_save import save_data

# Create enum of countries
class Countries(Enum):
    """Countries in dataset"""
    AT = 'AUSTRIA'
    BE = 'BELGIUM'
    BG = 'BULGARIA'
    CH = 'SWITZERLAND'
    CY = 'CYPRUS'
    CZ = 'CZECHIA'
    DK = 'DENMARK'
    EE = 'ESTONIA'
    EL = 'GREECE'
    ES = 'SPAIN'
    FI = 'FINLAND'
    FR = 'FRANCE'
    HR = 'CROACIA'
    HU = 'HUNGARY'
    IS = 'ICELAND'
    IT = 'ITALY'
    LI = 'LIECHTENSTEIN'
    LT = 'LITHUANIA'
    LU = 'LUXEMBOURG'
    LV = 'LATVIA'
    MT = 'MALTA'
    NL = 'NETHERLANDS'
    NO = 'NORWAY'
    PL = 'POLAND'
    PT = 'PORTUGAL'
    RO = 'ROMANIA'
    SE = 'SWEDEN'
    SI = 'SLOVENIA'
    SK = 'SLOVAKIA'
    DE = 'GERMANY'
    AL = 'ALBANIA'
    IE = 'IRELAND'
    ME = 'MONTENEGRO'
    MK = 'NORTH_MACEDONIA'
    RS = 'SERBIA'
    AM = 'ARMENIA'
    AZ = 'AZERBAIJAN'
    GE = 'GEORGIA'
    TR = 'TURKEY'
    UA = 'UKRAINE'
    BY = 'BELARUS'
    UK = 'UNITED_KINGDOM'
    XK = 'KOSOVO'
    FX = 'FRANCE_METROPOLITAN'
    MD = 'MOLDOVA'
    SM = 'SAN_MARINO'
    RU = 'RUSSIA'

    # for testing purpose
    @staticmethod
    def list():
        """Print list of countries"""
        return [l.value for l in Countries]

# Define possible regions
class Instituions(Enum):
    """Regions in dataset"""
    EU_27_2020 = 'EUROPEAN_UNION'
    DE_TOT = 'GERMANY_TOT'
    EA_18 = 'EURO_AREA_18'
    EA_19 = 'EURO_AREA_19'
    EFTA = 'EUROPE_FREE_TRADE_ASSOCIATION'
    EEA30_2007 = 'EUROPEAN_ECONOMIC_AREA_2007'
    EEA31 = 'EUROPEAN_ECONOMIC_AREA'
    EU27_2007 = 'EUROPEAN_UNION_2007'
    EU28 = 'EUROPEAN_UNION_28'

Regions = Enum('Regions', [(i.name, i.value) for i in chain(Countries, Instituions)])


def main(filename: str, region: str) -> None:
    """
    Main function to load, clean and save data.
    :param filename: Name of the file to load data
    :param region: Region to filter
    """
    region = Regions(region.upper()).name
    path = pathlib.Path(__file__).parent / 'data'

    dataoptions = DataOptions(filename=filename, path=path)

    dataoptions.load_data()
    #dataoptions.filter_data(region)

    save_data(data_tosave=dataoptions.data)

if __name__=='__main__': # pragma: no cover

    # Parse arguments from command line
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    parser.add_argument('region')
    args = parser.parse_args()

    main(args.filename, args.region)
