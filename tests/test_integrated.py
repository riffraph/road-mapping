import road_mapping.app as app
import os
import pytest

OUTPUT_PATH = "tests/output/"
TEST_DATA_FOLDER_PATH = 'tests/data'
TEST_DATA_UNNORMALIZED_SIMPLE = 'testdata_unnormalized_simple.xlsx'
TEST_DATA_UNNORMALIZED_HIERARCHY_DEFINED_BY_DATA_GROUPS = 'testdata_unnormalized_hierarchy_defined_by_data_groups.xlsx'
TEST_DATA_UNNORMALIZED_HIERARCHY_DEFINED_BY_LINK_TO_PARENT = 'testdata_unnormalized_hierarchy_defined_by_link_to_parent.xlsx'

def test_integrated():
    filePath = os.path.join(TEST_DATA_FOLDER_PATH, TEST_DATA_UNNORMALIZED_SIMPLE)
    app.generateVisualRoadMap(filePath, OUTPUT_PATH, False)
