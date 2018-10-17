#from road_mapping.model import Capability
import road_mapping.model as model
import pytest

def test_create_capability():
    capability = model.Capability('C_1', 'capability 1')
    assert(capability.id == 'C_1')
    assert(capability.name == 'capability 1')

def test_capability_immutable_id():
    capability = model.Capability('C_1', 'capability 1')
    with pytest.raises(AttributeError):
        capability.id = 'C_2'

def test_create_feature():
    feature = model.Feature('F_1', 'feature 1', 'C_1')
    assert(feature.id == 'F_1')
    assert(feature.name == 'feature 1')
    assert(feature.capabilityId == 'C_1')

def test_feature_immutable_ids():
    feature = model.Feature('F_1', 'feature 1', 'C_1')
    with pytest.raises(AttributeError):
        feature.id = 'F_2'
    with pytest.raises(AttributeError):
        feature.capabilityId = 'C_2'