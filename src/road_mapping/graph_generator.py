import graphviz 
import road_mapping.log as log


CAPABILITY_NODE_SHAPE = 'rectangle'
FEATURE_NODE_SHAPE = 'oval'

class graphviz_gen:

    def generateGraph(capabilities, features=[]):
        logger = log.get_logger('graph_generator')

        # here we can specify what kind of graph we want to generate 
        # need to check whether the graph type affects how the 
        # model should be constructed
        gvModel = graphviz.Digraph(comment="test", format="png")

        for c in capabilities:
            nodeId = str(c.id)
            nodeName = ''

            if c.name: 
                nodeName = c.name
            elif c.summary:
                nodeName = c.summary
            elif c.description:
                nodeName = c.description
            else:
                raise Exception('generateGraph: capability must have a name, summary or description field')

            gvModel.node(nodeId, nodeName, shape=CAPABILITY_NODE_SHAPE)
            logger.debug('added Capability node: nodeId={}, nodeName={}'.format(nodeId, nodeName))

        for f in features:
            nodeId = str(f.id)
            nodeName = ''
            parentId = str(f.parentId)

            if f.name: 
                nodeName = f.name
            elif f.summary:
                nodeName = f.summary
            elif f.description:
                nodeName = f.description
            else:
                raise Exception('generateGraph: feature must have a name, summary or description field')

            gvModel.node(nodeId, nodeName, shape=FEATURE_NODE_SHAPE)
            logger.debug('added Feature node: nodeId={}, nodeName={}'.format(nodeId, nodeName))

            # check if the parent capability exists
            filter_iter = filter(lambda x: x.id == f.parentId, capabilities)
            if next(filter_iter, None) is None:
                raise Exception('generateGraph: feature cannot be created without a capability')

            gvModel.edge(parentId, nodeId, '', dir='forward')

        return gvModel


    def generateDiagram(gvModel, output_path, view_diagram=False):
        if type(gvModel) is not graphviz.Digraph:
            raise Exception('expected a Graphviz Digraph object')

        print("Generating diagram ...")
        print(gvModel.source)
        gvModel.render(output_path + 'tmp.gv', view=view_diagram)