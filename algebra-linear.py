from typing import List

Vector = List[float]

def add(v: Vector, w: Vector) -> Vector:
    ''' Adds corresponding elements '''
    assert len(v) == len(w), 'Vectors must be the same length'

    return [v_i + w_i for v_i, w_i in zip(v, w)]

assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]

def subtract(v: Vector, w: Vector) -> Vector:
    ''' Substract corresponding elements '''
    assert len(v) == len(w), 'Vectors must be the same lenght'

    return [v_i - w_i for v_i, w_i in zip(v, w)]

assert subtract([5, 7, 9], [4, 5, 6]) == [1, 2, 3]

def vector_sum(vectors: List[Vector]) -> Vector:
    ''' Sums all corresponding elements '''
    assert vectors, 'No vectors provided!'

    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), 'different sizes'

    return [sum(vector[i] for vector in vectors)
            for i in range(num_elements)]

assert vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20]

def scalar_multiply(c: float, v: Vector) -> Vector:
    ''' Multiplies every element by c '''
    return [i * c for i in v]

assert scalar_multiply(2, [1, 2, 3]) == [2, 4, 6]