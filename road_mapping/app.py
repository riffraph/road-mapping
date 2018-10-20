import os
import sys
import argparse
#from . import model, model_loader, graph_generator
from . import model, model_loader, graph_generator, log

def generateVisualRoadMap(inputFilePath, outputFolderPath, viewFlag):
    logger = log.get_logger('road_mapping')

    capabilities, features = model_loader.xlsx_loader.loadModel(inputFilePath, logger)

    gvModel = graph_generator.graphviz_gen.generateGraph(capabilities, features, logger)
    graph_generator.graphviz_gen.generateDiagram(gvModel, outputFolderPath, viewFlag, logger)

    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='generate a visual representation of a road map')

    parser.add_argument('inputFilePath', help='path to the input file. Only .xlsx is supported for now')
    parser.add_argument('outputFolderPath', help='path to folder where the output is written to')
    parser.add_argument('-v', '--view', help='view the output image', action='store_true', default=False)

    args = parser.parse_args()
    
    generateVisualRoadMap(args.inputFilePath, args.outputFolderPath, args.view)