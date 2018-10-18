import road_mapping.graph_generator as graph_generator
import road_mapping.model as model
import pytest

OUTPUT_PATH = "tests/output/"

def test_graph_generator_graphviz_capability_only():
    capabilities = []
    capabilities.append(model.Capability('C_1', name='first capability'))
    capabilities.append(model.Capability('C_2', name='second capability'))
    capabilities.append(model.Capability('C_3', summary='summary test'))
    capabilities.append(model.Capability('C_4', description='description test'))
    capabilities.append(model.Capability(1234, description='number as id test'))

    gvModel = graph_generator.graphviz_gen.generateGraph(capabilities)

    assert(len(gvModel.body) == len(capabilities))


def test_graph_generator_graphviz_feature_only():
    features = []
    features.append(model.Feature('F_1', 'C_1', name='first feature'))

    with pytest.raises(Exception):
        gvModel = graph_generator.graphviz_gen.generateGraph([], features)


def test_graph_generator_graphviz_simple_model():
    capabilities = []
    capabilities.append(model.Capability('C_1', name='first capability'))
    capabilities.append(model.Capability('C_2', name='second capability'))

    features = []
    features.append(model.Feature('F_1', 'C_1', name='first feature'))

    gvModel = graph_generator.graphviz_gen.generateGraph(capabilities, features)

    assert(len(gvModel.body) == (len(capabilities) + (len(features) * 2)))