def vectors(vector1, vector2):
    if len(vector1) != len(vector2):
        return None
    vector3 = []
    for v1, v2 in zip(vector1, vector2):
        vector3.append(v1 + v2)
    return vector3

print(vectors([1, 1], [1, 1]))
print(vectors([1, 2], [1, 4]))
print(vectors([1, 2, 1], [1, 4, 3]))

def scalar(number, vector):
    vector1 = []
    for apple in vector:
        vector1.append(number * apple)
    return vector1

print(scalar(5, [1, 2]))
print(scalar(3, [1, 0, -1]))
print(scalar(7, [3, 0, 5, 11, 2]))


def product(vec1, vec2):
    if len(vec1) != len(vec2):
        return None
    products = []
    for r1, r2 in zip(vec1, vec2):
        products.append(r1 * r2)

    sum_produc = 0
    for product in products:
        sum_produc += product

    return sum_produc


print(product([1, 1], [1, 1]))
print(product([1, 2], [1, 4]))
print(product([1, 2, 1], [1, 4, 3]))

