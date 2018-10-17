class Capability:
    def __init__(self, id, name='', summary='', description=''):
        self._id = id
        self.name = name
        self.summary = summary
        self.description = description

    @property
    def id(self):
        return self._id
        

class Feature:
    def __init__(self, id, capabilityId, name='', summary='', description=''):
        self._id = id
        self.name = name
        self.summary = summary
        self.description = description
        self._capabilityId = capabilityId

    @property
    def id(self):
        return self._id

    @property
    def capabilityId(self):
        return self._capabilityId