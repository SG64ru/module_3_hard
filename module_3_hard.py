data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

add = 0
def calculate_structure_sum(data):
    global add
    if  isinstance(data, (int, float)):
        add = add + data
    elif isinstance(data, str):
        add = add + len(data)
    elif isinstance(data, (tuple, list, set)):
        for elem in data:
            calculate_structure_sum(elem)
    elif isinstance(data, dict):
        for key, value in data.items():
            calculate_structure_sum(key)
            calculate_structure_sum(value)


    return add

result = calculate_structure_sum(data_structure)
print(result)