from vector import Vector
    
def test_print(vector):
    print("Vector: {}".format(vector))

def test_dimension(vector):
    print("Vector dimension: {}".format(len(vector)))

def test_length(vector):
    print("Vector length: {:.2f}".format(vector.length()))

def test_addition(vector1, vector2):
    print("Vector1 + Vector2: {}".format(vector1 + vector2))

def test_scaling(vector, scalar):
    vector.scaling(scalar)
    print("Scaling vector by {}: {}".format(scalar, vector))

# Main program starts here
v1 = Vector([2,4])
v2 = Vector([3,-4])
test_print(v1)
test_print(v2)
test_length(v1)
test_length(v2)
test_dimension(v1)
test_addition(v1,v2)
test_scaling(v1, 2)

print()
v1 = Vector([3,5,-2])
v2 = Vector([2,-3,4])
test_print(v1)
test_print(v2)
test_length(v1)
test_length(v2)
test_dimension(v1)
test_addition(v1,v2)
test_scaling(v2, 3)