def min_max(values):
    return min(values), max(values)

def mean(values):
    return sum(values) / len(values)

print(mean((1, 2, 3, 4, 5)))
print(min_max((1, 2, 3, 4, 5)))