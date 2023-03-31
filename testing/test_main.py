from main import get_none, flatten_dict 

def test_get_none():
    assert get_none() is None

def test_flatten_dict():
    assert type(flatten_dict({'a': 42, 'b': 3.14})) is list