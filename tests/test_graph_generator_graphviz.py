import road_mapping.graph_generator.graphviz_gen as graphviz_gen
import road_mapping.model as model
import pytest

OUTPUT_PATH = "tests/output/"

def test_graph_generator_graphviz_capability_only():
    capabilities = []
    capabilities.append(model.Capability('C_1', name='first capability'))
    capabilities.append(model.Capability('C_2', name='second capability'))

    gvModel = graphviz_gen.generateGraph(capabilities)

    graphviz_gen.generateDiagram(gvModel, OUTPUT_PATH, True)
    assert(len(gvModel.body) == len(capabilities))


def test_graph_generator_graphviz_feature_only():
    features = []
    features.append(model.Feature('F_1', 'C_1', name='first feature'))

    with pytest.raises(Exception):
        gvModel = graphviz_gen.generateGraph([], features)


def test_graph_generator_graphviz_simple_model():
    capabilities = []
    capabilities.append(model.Capability('C_1', name='first capability'))
    capabilities.append(model.Capability('C_2', name='second capability'))

    features = []
    features.append(model.Feature('F_1', 'C_1', name='first feature'))

    gvModel = graphviz_gen.generateGraph(capabilities, features)

    assert(len(gvModel.body) == (len(capabilities) + (len(features) * 2)))