from graphviz import Digraph

def initModel():
    # here we can specify what kind of graph we want to generate 
    # need to check whether the graph type affects how the 
    # model should be constructed
    gvModel = Digraph(comment="test", format="png")

    return gvModel


def populateModel(gvModel: Digraph):
    # should probably validate that the dot parameter is the right graphviz type...
    if type(gvModel) is not Digraph:
        raise Exception('expected a Graphviz Digraph object')

    print("Populate Graphviz model ...")
    
    # add nodes
    gvModel.node('A', 'aaa')
    gvModel.node('B', 'bbb')
    gvModel.node('C', 'bbb')

    # add edges
    gvModel.edge('A', 'B')
    
    print(gvModel.source)

    return gvModel


def generateDiagram(gvModel, output_path, view_diagram=False):
    print("Generating diagram ...")
    gvModel.render(output_path + 'tmp.gv', view=view_diagram)