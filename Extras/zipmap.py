def zipmap(keys, values):
    if len(keys) == 0 or len(values) == 0:
        return {}
    res = zipmap(keys[1:], values[1:])
    res[keys[0]] = values[0]
    return res



# 2nd approach- dict unpacking and merging
def zipmap(keys, values):
    if len(keys) == 0 or len(values) == 0:
        return {}

    first_pair = {keys[0]: values[0]}
    rest_pairs = zipmap(keys[1:], values[1:])  # Recursive call to get the rest

    # Merging with unpacking
    return {**first_pair, **rest_pairs}


# using update method
def zipmap(keys, values):
    if len(keys) == 0 or len(values) == 0:
        return {}

    first_pair = {keys[0]: values[0]}  # The initial dictionary with the first key-value pair
    rest_pairs = zipmap(keys[1:], values[1:])  # Recursive call for the remaining pairs

    first_pair.update(rest_pairs)  # Merge with the recursive result
    return first_pair




