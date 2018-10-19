import road_mapping.graph_generator as graph_generator
import road_mapping.model_loader as model_loader
import road_mapping.model as model
import os
import pytest

OUTPUT_PATH = "tests/output/"
TEST_DATA_FOLDER_PATH = 'tests/data'
TEST_DATA_UNORMALIZED_HIERARCHY_DEFINED_BY_DATA_GROUPS = 'testdata_unnormalized_hierarchy_defined_by_data_groups.xlsx'
TEST_DATA_UNORMALIZED_HIERARCHY_DEFINED_BY_LINK_TO_PARENT = 'testdata_unnormalized_hierarchy_defined_by_link_to_parent.xlsx'

def test_integrated():
    filePath = os.path.join(TEST_DATA_FOLDER_PATH, TEST_DATA_UNORMALIZED_HIERARCHY_DEFINED_BY_LINK_TO_PARENT)
    capabilities, features = model_loader.xlsx_loader.loadModel(filePath)

    assert(len(capabilities) > 0)

    gvModel = graph_generator.graphviz_gen.generateGraph(capabilities, features)
    graph_generator.graphviz_gen.generateDiagram(gvModel, OUTPUT_PATH, True)

    assert(len(gvModel.body) == len(capabilities) + (len(features) * 2))
