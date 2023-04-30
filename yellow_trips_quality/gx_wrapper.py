import pandas as pd
from datetime import datetime
import great_expectations as gx
from great_expectations.core.batch import RuntimeBatchRequest
from great_expectations.core.yaml_handler import YAMLHandler
from great_expectations.data_context.types.base import (
    DataContextConfig,
    InMemoryStoreBackendDefaults,
)
from great_expectations.core.expectation_configuration import ExpectationConfiguration
from great_expectations.core.expectation_suite import ExpectationSuite
from great_expectations.checkpoint.checkpoint import CheckpointConfig
from great_expectations.data_context import EphemeralDataContext

yaml = YAMLHandler()


class DataQuality():
    dataset_name:str = None
    dataframe: pd.DataFrame = None
    expectation_suite_name: str = None
    data_context: gx.DataContext = None
    batch_request: RuntimeBatchRequest = None
    checkpoint_name: str = None

    def __init__(self, dataset_name: str, dataframe: pd.DataFrame, expectations_as_list: list):
        
        # INITIALIZING THE DATA CONTEXT
        data_context_configuration = DataContextConfig(
            store_backend_defaults=InMemoryStoreBackendDefaults()
        )
        self.data_context: EphemeralDataContext = gx.get_context(project_config=data_context_configuration)

        # CONFIGURE DATASOURCE
        datasource_name = f"{dataset_name}_data_source"
        dataconnector_name = f"{dataset_name}_data_connector"
        datasource_config = {
            "name": datasource_name,
            "class_name": "Datasource",
            "execution_engine": {"class_name": "PandasExecutionEngine"},
            "data_connectors": {
                dataconnector_name: {
                    "class_name": "RuntimeDataConnector",
                    "batch_identifiers": ["batch_id", "batch_datetime"],
                }
            },
        }
        self.data_context.add_datasource(**datasource_config)

        # CREATE BATCH REQUEST
        self.batch_request = RuntimeBatchRequest(
            datasource_name=datasource_name,
            data_connector_name=dataconnector_name,
            data_asset_name=dataset_name,
            runtime_parameters={"batch_data": dataframe},  # our nyc trips dataframe
            batch_identifiers={
                "batch_id": f"{dataset_name}_{datetime.strftime(datetime.now(), '%Y%m%d%H%M%S')}",
                
            },
        )

        # BUILD EXPECTATION SUITE
        self.expectation_suite_name = f"{dataset_name}_expectation_suite"

        expectations: list = []
        expectation_suite: ExpectationSuite = ExpectationSuite(expectation_suite_name=self.expectation_suite_name)

        for item in expectations_as_list:
            config = ExpectationConfiguration(**item)
            expectations.append(config)

        expectation_suite.add_expectation_configurations(expectations)
        self.data_context.add_or_update_expectation_suite(expectation_suite=expectation_suite)

        # CREATING A CHECKPOINT TO VALIDATE EXPECTATIONS
        self.checkpoint_name = f"{dataset_name}_checkpoint"
        checkpoint_config = {
            "name": self.checkpoint_name,
            "config_version": 1.0,
            "class_name": "SimpleCheckpoint",
            "run_name_template": f"{dataset_name}_%Y%m%d-%H%M%S",
        }
        self.checkpoint = self.data_context.add_or_update_checkpoint(**checkpoint_config)

    
    def run_validations(self):
        checkpoint_result = self.data_context.run_checkpoint(
            checkpoint_name=self.checkpoint_name,
            validations=[
                {
                    "batch_request": self.batch_request,
                    "expectation_suite_name": self.expectation_suite_name
                }
            ]
        )

        return checkpoint_result


