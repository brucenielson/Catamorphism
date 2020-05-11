# https://compiletoi.net/garcon-theres-a-catamorphism-in-my-python/

def fmap(f, data):
    if isinstance(data, list):
        return [f(x) for x in data]
    if isinstance(data, dict):
        return {k: f(v) for (k, v) in data.items()}
    return data


def cata(f, data):
    # First, we recurse inside all the values in data
    cata_on_f = lambda x: cata(f, x)
    recursed = fmap(cata_on_f, data)

    # Then, we apply f to the result
    return f(recursed)


def sum_one_level(data):
    if isinstance(data, list):
        return sum(data)
    return data



result = cata(sum_one_level, [[[1, 2], [3]], [4]])
print(result)
