def flatten(lst):
    flattened = []
    for i in lst:
        if type(i) is list:
            flattened.extend(flatten(i))
        else:
            flattened.append(i)
    return flattened

print(flatten([1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]]))
