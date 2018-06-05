from image_generator import graphviz_gen

OUTPUT_PATH = "output/"

def main():
    gvModel = graphviz_gen.initModel()
    graphviz_gen.populateModel(gvModel)
    graphviz_gen.generateDiagram(gvModel, OUTPUT_PATH)
    
if __name__ == "__main__":
    main()