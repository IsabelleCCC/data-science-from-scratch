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

def vector_mean(vectors: List[Vector]) -> Vector:
    ''' Computa a média dos elementos '''
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

assert vector_mean([[1, 2], [3, 4], [5, 6]]) == [3, 4]

def dot(v: Vector, w: Vector) -> float:
    """Computes v_1 * w_1 + ... + v_n * w_n"""
    assert len(v) == len(w), "vectors must be same length"

    return sum(v_i * w_i for v_i, w_i in zip(v, w))

assert dot([1, 2, 3], [4, 5, 6]) == 32

def sum_of_squares(v: Vector) -> float:
    ''' Returns v_1 * v_1 + ... v_n * v_n '''
    return dot(v, v)

assert sum_of_squares([1, 2, 3]) == 14

import math

def magnitude(v: Vector) -> float:
	return math.sqrt(sum_of_squares(v))

assert magnitude([3, 4]) == 5

def squared_distance(v: Vector, w: Vector) -> float:
     ''' Computes (v_1 - w_1) ** 2 + ... + (v_n - w_n) ** 2 '''
     return sum_of_squares(subtract(v, w))

def distance(v: Vector, w: Vector) -> float:
     ''' Computes distance between v and w '''
     return math.sqrt(squared_distance(v, w))

# or

def distance(v: Vector, w: Vector):
     return magnitude(subtract(v , w))

Matrix = List[List[float]]

A = [[1, 2, 3],
     [4, 5, 6]]

B = [[1, 2],
     [3, 4],
      [5, 6]]

from typing import Tuple

def shape(A: Matrix) -> Tuple[int, int]:
     '''' Returns n of rows and n of columns '''
     num_rows = len(A)
     num_cols = len(A[0]) if A else 0
     return num_rows, num_cols

assert shape([[1, 2, 3], [4, 5, 6]]) == (2 , 3)

def get_row(A: Matrix, i: int) -> Vector:
     return A[i]

def get_col(A: Matrix, j: int) -> Vector:
     return [A_i[j] for A_i in A]

