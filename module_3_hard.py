def calculate_structure_sum(*args):
    summa = 0

    for data in args:
        if isinstance(data, (int, float)):
            summa += data
        elif isinstance(data, str):
            summa += len(data)
        elif isinstance(data, (list, tuple, set)):
            summa += calculate_structure_sum(*data)
        elif isinstance(data, dict):
            for key, value in data.items():
                summa += calculate_structure_sum(key)
                summa += calculate_structure_sum(value)

    return summa


# Пример
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)  #99
