import pytest
from unittest.mock import patch, MagicMock
from pandas import DataFrame
from us_visa.components.data_ingestion import DataIngestion
from us_visa.entity.config_entity import DataIngestionConfig
from us_visa.entity.artifact_entity import DataIngestionArtifact
from us_visa.exception import USvisaException

@pytest.fixture
def mock_data_ingestion_config():
    # Mocking DataIngestionConfig with necessary attributes
    config = MagicMock(spec=DataIngestionConfig)
    config.collection_name = "mock_collection"
    config.feature_store_file_path = "/mock/path/feature_store.csv"
    config.training_file_path = "/mock/path/train.csv"
    config.testing_file_path = "/mock/path/test.csv"
    config.train_test_split_ratio = 0.2
    return config

@pytest.fixture
def mock_dataframe():
    # Creating a mock DataFrame
    return DataFrame({
        'column1': [1, 2, 3, 4, 5],
        'column2': ['a', 'b', 'c', 'd', 'e']
    })

@pytest.fixture
def mock_data_ingestion_artifact():
    # Mocking DataIngestionArtifact
    return MagicMock(spec=DataIngestionArtifact)

@pytest.fixture
def mock_usvisa_data():
    # Mocking USvisaData
    mock_data = MagicMock()
    mock_data.export_collection_as_dataframe.return_value = DataFrame({
        'column1': [1, 2, 3, 4, 5],
        'column2': ['a', 'b', 'c', 'd', 'e']
    })
    return mock_data

@pytest.mark.usefixtures("mock_data_ingestion_config", "mock_dataframe", "mock_data_ingestion_artifact", "mock_usvisa_data")
class TestDataIngestionInitiateDataIngestion:

    @pytest.mark.happy_path
    def test_initiate_data_ingestion_success(self, mock_data_ingestion_config, mock_usvisa_data, mock_data_ingestion_artifact):
        """
        Test that initiate_data_ingestion successfully processes data and returns a DataIngestionArtifact.
        """
        with patch('us_visa.components.data_ingestion.USvisaData', return_value=mock_usvisa_data):
            data_ingestion = DataIngestion(data_ingestion_config=mock_data_ingestion_config)
            result = data_ingestion.initiate_data_ingestion()
            assert isinstance(result, DataIngestionArtifact)
            assert result.trained_file_path == mock_data_ingestion_config.training_file_path
            assert result.test_file_path == mock_data_ingestion_config.testing_file_path

    @pytest.mark.edge_case
    def test_initiate_data_ingestion_empty_dataframe(self, mock_data_ingestion_config, mock_usvisa_data):
        """
        Test that initiate_data_ingestion handles an empty DataFrame gracefully.
        """
        mock_usvisa_data.export_collection_as_dataframe.return_value = DataFrame()
        with patch('us_visa.components.data_ingestion.USvisaData', return_value=mock_usvisa_data):
            data_ingestion = DataIngestion(data_ingestion_config=mock_data_ingestion_config)
            with pytest.raises(USvisaException):
                data_ingestion.initiate_data_ingestion()

    @pytest.mark.edge_case
    def test_initiate_data_ingestion_export_failure(self, mock_data_ingestion_config):
        """
        Test that initiate_data_ingestion raises an exception if export_data_into_feature_store fails.
        """
        with patch('us_visa.components.data_ingestion.USvisaData') as mock_usvisa_data:
            mock_usvisa_data.side_effect = Exception("Export failed")
            data_ingestion = DataIngestion(data_ingestion_config=mock_data_ingestion_config)
            with pytest.raises(USvisaException):
                data_ingestion.initiate_data_ingestion()

    @pytest.mark.edge_case
    def test_initiate_data_ingestion_split_failure(self, mock_data_ingestion_config, mock_usvisa_data):
        """
        Test that initiate_data_ingestion raises an exception if split_data_as_train_test fails.
        """
        with patch('us_visa.components.data_ingestion.USvisaData', return_value=mock_usvisa_data):
            with patch.object(DataIngestion, 'split_data_as_train_test', side_effect=Exception("Split failed")):
                data_ingestion = DataIngestion(data_ingestion_config=mock_data_ingestion_config)
                with pytest.raises(USvisaException):
                    data_ingestion.initiate_data_ingestion()