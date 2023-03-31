def get_none():
    return None

def flatten_dict(input_list):
    input_list = list(input_list.values())
    print(input_list)
    return input_list

def flatten_dict_recursive(d):
    result = []
    for k, v in d.items():
        if not isinstance(v, dict):
            result.append(v)
        else:
            result.extend(flatten_dict_recursive(v))
    print(result)
    return result


flatten_dict({'a': 42, 'b': 3.14})
# [42, 3.14]

flatten_dict({'a': [42, 350], 'b': 3.14})
# [[42, 350], 3.14]

flatten_dict({'a': {'inner_a': 42, 'inner_b': 350}, 'b': 3.14})
# [{'inner_a': 42, 'inner_b': 350}, 3.14]

flatten_dict_recursive({'a': {'inner_a': 42, 'inner_b': 350}, 'b': 3.14})
# [42, 350, 3.14]

flatten_dict_recursive({'a': [{'inner_inner_a': 42}]})
# [42]