#from road_mapping.model import Capability
import pytest
import road_mapping.model as model

def test_create_capability():
    capability = model.Capability('C_1', name='first capability')
    assert(capability.id == 'C_1')
    assert(capability.name == 'first capability')

def test_capability_immutable_id():
    capability = model.Capability('C_1', 'capability 1')
    with pytest.raises(AttributeError):
        capability.id = 'C_2'

def test_create_feature():
    feature = model.Feature('F_1', 'C_1', name='first feature', summary='this is a feature', description='this does something')
    assert(feature.id == 'F_1')
    assert(feature.parentId == 'C_1')
    assert(feature.name == 'first feature')
    assert(feature.summary == 'this is a feature')
    assert(feature.description == 'this does something')

def test_feature_immutable_ids():
    feature = model.Feature('F_1', 'C_1')
    with pytest.raises(AttributeError):
        feature.id = 'F_2'
    with pytest.raises(AttributeError):
        feature.parentId = 'C_2'