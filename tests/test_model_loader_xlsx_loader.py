import road_mapping.model_loader as model_loader
import os
import pytest

TEST_DATA_FOLDER_PATH = 'tests/data'
TEST_DATA_EMPTY_FILE_CSV = 'testdata_empty_file.csv'
TEST_DATA_EMPTY_FILE_XLSX = 'testdata_empty_file.xlsx'
TEST_DATA_UNORMALIZED_HIERARCHY_DEFINED_BY_DATA_GROUPS = 'testdata_unnormalized_hierarchy_defined_by_data_groups.xlsx'

def test_invalid_file_path():
    # input file is a folder
    filePath = os.path.join(TEST_DATA_FOLDER_PATH, '')
    with pytest.raises(Exception):
        _, _ = model_loader.xlsx_loader.loadModel(filePath)

    # input file is a different extension
    filePath = os.path.join(TEST_DATA_FOLDER_PATH, TEST_DATA_EMPTY_FILE_CSV)
    with pytest.raises(Exception):
        _, _ = model_loader.xlsx_loader.loadModel(filePath)


def test_unnormalized_hierarchy_defined_by_data_groups():
    filePath = os.path.join(TEST_DATA_FOLDER_PATH, TEST_DATA_UNORMALIZED_HIERARCHY_DEFINED_BY_DATA_GROUPS)
    capabilities, features = model_loader.xlsx_loader.loadModel(filePath)

    assert(len(capabilities) > 0)