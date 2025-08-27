import json
import sys

def fill(test_structure, value_map):
    if isinstance(test_structure, dict):
        if 'id' in test_structure and test_structure['id'] in value_map:
            test_structure['value'] = value_map[test_structure['id']]

        for key, value in test_structure.items():
            if isinstance(value, (dict, list)):
                test_structure[key] = fill(value, value_map)

    elif isinstance(test_structure, list):
        for i, item in enumerate(test_structure):
            test_structure[i] = fill(item, value_map)

    return test_structure

with open(sys.argv[1], 'r') as file:
    values_data = json.load(file)

with open(sys.argv[2], 'r') as file:
    tests_data = json.load(file)

value_map = {}
for i in values_data.get('values', []):
    value_map[i['id']] = i['value']

res = fill(tests_data, value_map)


with open(sys.argv[3], 'w') as file:
    json.dump(res, file, indent=2)

