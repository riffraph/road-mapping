class Capability:
    def __init__(self, id, name='', summary='', description=''):
        self._id = id
        self.name = name
        self.summary = summary
        self.description = description

    @property
    def id(self):
        return self._id

    def __str__(self):
        return '-- id={}, name={}, summary={}, description={} --'.format(self.id, self.name, self.summary, self.description)
        

class Feature:
    def __init__(self, id, parentId, name='', summary='', description=''):
        self._id = id
        self.name = name
        self.summary = summary
        self.description = description
        self._parentId = parentId

    @property
    def id(self):
        return self._id

    @property
    def parentId(self):
        return self._parentId

    def __str__(self):
        return '-- id={}, name={}, summary={}, description={}, parentId={} --'.format(self.id, self.name, self.summary, self.description, self.parentId)