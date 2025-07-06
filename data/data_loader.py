# This class is responsible for managing the data loading process.
# It handles file path validation and ensures that the data is properly loaded.

import os
import pandas as pd

from config.settings import Config

class DataLoader:

    def __init__(self, data_path: str = None):

        self.data_path = data_path or Config.MYSIC_CSV_DATA_FILE_PATH
        self.dataframe = None

    def _load_data(self) -> pd.DataFrame:
        print("Loading process is starting...")
        try:
            if self._validate_csv():
                self.dataframe = pd.read_csv(self.data_path)
                #print(self.dataframe.head())
                self._validate_columns()  # Kolon kontrolünü burada çağırabilirsin
                return self.dataframe
            else:
                raise FileNotFoundError(f"CSV file not found or not readable at {self.data_path}")

        except Exception as e:
            print(f'An error occurred: {e}')
            return None

    def _validate_csv(self) -> bool:
        if os.path.exists(self.data_path) and os.access(self.data_path, os.R_OK):
            print(f"CSV file is exist and readable on {self.data_path}")
            return True
        else:
            print(f"CSV file is missing or not readable on {self.data_path}")
            return False

    def _validate_columns(self) -> list:

        required_columns = ["valence","year","acousticness","artists","danceability","duration_ms","energy","explicit",
                            "id","instrumentalness","key","liveness","loudness","mode","name","popularity",
                            "release_date","speechiness","tempo"]

        missing_columns = [col for col in required_columns if col not in self.dataframe.columns]

        if missing_columns:
            raise ValueError(f'At loading process, missing columns are existed: {missing_columns}')
