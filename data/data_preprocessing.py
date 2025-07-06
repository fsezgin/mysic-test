# This class performs data preprocessing steps:
# - Missing value detection and cleaning
# - Selection of relevant columns
# - Necessary normalization operations
# - Saving the processed data in .npy format

from joblib import dump
import pandas as pd


from config.settings import Config
from sklearn.preprocessing import MinMaxScaler


class DataPreprocess:

    def __init__(self, dataframe: pd.DataFrame = None):

        self.scaler = MinMaxScaler()
        self.dataframe = dataframe

    def generate_preprocess(self):

        try:

            processed_data = self._normalization_and_missing_value_operation()
            return processed_data

        except Exception as e:
            print(e)


    def _normalization_and_missing_value_operation(self) -> pd.DataFrame:

        data_without_missing_value = self.dataframe.dropna()

        print("*" * 25)
        print(len(data_without_missing_value))

        # "explicit" "key" "mode" encoding maybe
        useless_columns =  ["year", "artists", "explicit", "id",  "key",  "mode", "name", "release_date"]

        clean_data = data_without_missing_value.drop(columns= useless_columns)

        raw_data = self.scaler.fit_transform(clean_data)

        dump(self.scaler, 'mysic_scaler.pkl')

        return raw_data