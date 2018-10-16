from graph_generator import graphviz_gen

OUTPUT_PATH = "output/"

def main():
    # load model from file


    # generate the graph using the model
    gvModel = graphviz_gen.initModel()

    print("Populate Graphviz model ...")
    
    # add nodes
    gvModel.node('A', 'aaa')
    gvModel.node('B', 'bbb')
    gvModel.node('C', 'bbb')

    # add edges
    gvModel.edge('A', 'B', "edgey", dir='both')

    # generate the diagram
    graphviz_gen.generateDiagram(gvModel, OUTPUT_PATH, True)
    
if __name__ == "__main__":
    main()