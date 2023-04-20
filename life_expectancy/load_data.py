"""Load data in other formats"""
# pylint: disable=redefined-outer-name
# pylint: disable=too-few-public-methods
# pylint: disable=anomalous-backslash-in-string
# pylint: disable=no-member
# pylint: disable=attribute-defined-outside-init
import pathlib
from abc import ABC
import re
import pandas as pd

class LoadData(ABC):
    """
    Class used to load data from different types of files (tsv, zipped json)
    """

    @staticmethod
    def read_data(filename: str, path: pathlib.Path):
        """Load data"""

class LoadDataTSVSV(LoadData):
    """
    Load data from TSV file
    """

    @staticmethod
    def read_data(filename : str, path: pathlib.Path) -> pd.DataFrame:
        """
        Function to read data from file.
        :param filename: Name of the file to read
        :param path: Path to file
        :return: Dataframe with loaded data from file
        """

        # Define full path to file
        file = path / filename

        # Read data from path
        df_data = pd.read_csv(file, sep='[,\t]', engine='python')

        return df_data

class LoadZippedData(LoadData):
    """
    Load data from JSON in zipped file
    """

    @staticmethod
    def read_data(filename: str, path: pathlib.Path) -> pd.DataFrame:
        """
        Function to read data from file.
        :param filename: Name of the file to read
        :param path: Path to file
        :return: Dataframe with loaded data from file
        """

        data = pd.read_json(
                        path / filename, compression='infer'
                    ).drop(
                        columns=['flag', 'flag_detail']
                    )

        return data

class DataOptions():
    """
    Load all type of data
    """

    def __init__(self, filename: str, path: pathlib.Path) -> None:
        """
        Init to pass the filename and respective path
        :param filename: Name of the file to read
        :param path: Path to file
        """

        self._filename = filename
        self._path = path
        self._extension = re.search("\.(.*)", self._filename)[0]

    def _get_extension(self) -> LoadData:
        """
        Function to obtain the extension of file and return the correct loader
        """

        if self._extension == ".tsv":
            return LoadDataTSVSV()
        if self._extension == ".zip":
            return LoadZippedData()

        # if not tsv or zip, return error
        raise ValueError('Not tsv or zip file.')

    def load_data(self) -> pd.DataFrame:
        """
        Load file accordind to extension
        :return: Dataframe with loaded data
        """

        loader = self._get_extension()
        self.data: pd.DataFrame = loader.read_data(self._filename, self._path)
