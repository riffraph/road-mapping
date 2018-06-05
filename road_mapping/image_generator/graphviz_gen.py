from graphviz import Digraph

def initModel():
    # here we can specify what kind of graph we want to generate 
    # need to check whether the graph type affects how the 
    # model should be constructed
    gvModel = Digraph(comment="test", format="png")

    return gvModel


def populateModel(gvModel):
    # should probably validate that the dot parameter is the right graphviz type...

    print("Populate Graphviz model ...")
    
    # add nodes
    gvModel.node('A', 'aaa')
    gvModel.node('B', 'bbb')

    # add edges
    gvModel.edge('A', 'B')
    
    print(gvModel.source)


def generateDiagram(gvModel, output_path):
    gvModel.render(output_path + 'tmp.gv', view=True)