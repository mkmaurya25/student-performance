# import os
# import sys
# from src.utils.exception import CustomException
# from src.utils.loggers import logging
# import pandas as pd

# from sklearn.model_selection import train_test_split
# from dataclasses import dataclass

# from src.data.data_transformation import DataTransformation
# from src.data.data_transformation import DataTransformationConfig

# from models.model_training import ModelTrainerConfig
# from models.model_training import ModelTrainer

# @dataclass
# class DataIngestionConfig:
#     train_data_path: str = os.path.join('artifacts', "train.csv")
#     test_data_path: str = os.path.join('artifacts', "test.csv")
#     raw_data_path: str = os.path.join('artifacts', "data.csv")

# class DataIngestion:
#     def __init__(self):
#         self.ingestion_config = DataIngestionConfig()

#     def initiate_data_ingestion(self):
#         logging.info("Entered the data ingestion method or component")
#         try:
#             # Use os.path.join for platform-independent paths
#             df = pd.read_csv(os.path.join('data', 'raw', 'stud.csv'))
#             logging.info('Read the dataset as dataframe')

#             # Create directory if it does not exist
#             os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

#             # Save raw data
#             df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

#             logging.info("Train test split initiated")
#             train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

#             # Save train and test datasets
#             train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
#             test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

#             logging.info("Ingestion of the data is completed")

#             return (
#                 self.ingestion_config.train_data_path,
#                 self.ingestion_config.test_data_path
#             )
#         except Exception as e:
#             raise CustomException(e, sys)

# if __name__ == "__main__":
#     obj = DataIngestion()
#     train_data, test_data = obj.initiate_data_ingestion()

#     # Perform data transformation
#     data_transformation = DataTransformation()
#     train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_data, test_data)

#     # Train model
#     modeltrainer = ModelTrainer()
#     print(modeltrainer.initiate_model_trainer(train_arr, test_arr))

import os
import sys
from src.utils.exception import CustomException
from src.utils.loggers import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.data.data_transformation import DataTransformation
from src.data.data_transformation import DataTransformationConfig

from models.model_training import ModelTrainerConfig
from models.model_training import ModelTrainer

# Updated paths to save processed data in data/processed
@dataclass
class DataIngestionConfig:
    raw_data_path: str = os.path.join('data', 'raw', "stud.csv")  # Use raw data directly
    train_data_path: str = os.path.join('data', 'processed', "train.csv")
    test_data_path: str = os.path.join('data', 'processed', "test.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            # Read the raw data from data/raw/stud.csv
            df = pd.read_csv(self.ingestion_config.raw_data_path)
            logging.info('Read the dataset as dataframe')

            # Ensure the directory exists for processed data
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            logging.info("Train test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # Save train and test datasets in data/processed
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of the data is completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e, sys)

if __name__ == "__main__":
    # Data ingestion process
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()

    # Data transformation process
    data_transformation = DataTransformation()
    train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_data, test_data)

    # Model training process
    modeltrainer = ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr, test_arr))
