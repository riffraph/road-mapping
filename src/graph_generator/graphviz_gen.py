from graphviz import Digraph

def initModel():
    # here we can specify what kind of graph we want to generate 
    # need to check whether the graph type affects how the 
    # model should be constructed
    gvModel = Digraph(comment="test", format="png")

    return gvModel


def generateDiagram(gvModel, output_path, view_diagram=False):
    if type(gvModel) is not Digraph:
        raise Exception('expected a Graphviz Digraph object')

    print("Generating diagram ...")
    print(gvModel.source)
    gvModel.render(output_path + 'tmp.gv', view=view_diagram)