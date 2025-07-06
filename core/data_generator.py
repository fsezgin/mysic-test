import os

import numpy as np

from config.settings import Config
from data.data_loader import DataLoader
from data.data_preprocessing import DataPreprocess

class DataGenerator:

    def __init__(self, vector_path: str = None):

        self.vector_path = vector_path or Config.MYSIC_VECTOR_DATABASE_PATH

        self.data_loader = DataLoader()
        self.data_preprocessor = None
        self.dataframe = None

    def generate_data(self):

        print(" Starting Data Generate Process ")

        try:

            dataframe = self.data_loader._load_data()

            print(dataframe.head())
            print(len(dataframe))

            self.data_preprocessor = DataPreprocess(dataframe=dataframe)

            array = self.data_preprocessor.generate_preprocess()

            print("ARRAY" * 10)
            print(array)

            if not os.path.exists(self.vector_path):
                if array is None:
                    raise ValueError("Dosya yok ve feature sayısı bilinmiyor. array veya feature_dim verilmeli.")

                np.save(self.vector_path, array)

            else:
                print(f"{self.vector_path} zaten mevcut.")

        except Exception as e:
            print(e)
