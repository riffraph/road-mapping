from road_mapping.graph_generator import graphviz_gen

OUTPUT_PATH = "output/"

def test_graph_generator_graphviz_simple_model():
    gvModel = graphviz_gen.initModel()
    gvModel.node('Node 1', 'content 1')
    gvModel.node('Node 2', 'content 2')
    gvModel.edge('Node 1', 'Node 2', "edgey", dir='both')
    graphviz_gen.generateDiagram(gvModel, OUTPUT_PATH, True)