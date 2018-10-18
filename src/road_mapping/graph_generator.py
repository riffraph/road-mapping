import graphviz 

class graphviz_gen:

    def generateGraph(capabilities, features=[]):
        # here we can specify what kind of graph we want to generate 
        # need to check whether the graph type affects how the 
        # model should be constructed
        gvModel = graphviz.Digraph(comment="test", format="png")

        for c in capabilities:
            nodeName = ''
            if not c.name: 
                nodeName = c.name
            elif not c.summary:
                nodeName = c.summary
            elif not c.description:
                nodeName = c.description
            else:
                raise Exception('generateGraph: capability must have a name, summary or description field')

            gvModel.node(str(c.id), nodeName)

        for f in features:
            gvModel.node(f.id, f.name)

            # check if the parent capability exists
            filter_iter = filter(lambda x: x.id == f.capabilityId, capabilities)
            if next(filter_iter, None) is None:
                raise Exception('generateGraph: feature cannot be created without a capability')

            gvModel.edge(f.id, f.capabilityId, "edgey", dir='both')

        return gvModel


    def generateDiagram(gvModel, output_path, view_diagram=False):
        if type(gvModel) is not graphviz.Digraph:
            raise Exception('expected a Graphviz Digraph object')

        print("Generating diagram ...")
        print(gvModel.source)
        gvModel.render(output_path + 'tmp.gv', view=view_diagram)