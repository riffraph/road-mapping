class Capability:
    def __init__(self, id, name):
        self._id = id
        self.name = name

    @property
    def id(self):
        return self._id
        

class Feature:
    def __init__(self, id, name, capabilityId):
        self._id = id
        self.name = name
        self._capabilityId = capabilityId

    @property
    def id(self):
        return self._id

    @property
    def capabilityId(self):
        return self._capabilityId