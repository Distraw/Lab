import numpy as np
from collections import Counter

def get_elements_occuring_in_range_from_n_to_x_times(arr: np.array, n: int, x: int):
    unique_values, counts = np.unique(arr, return_counts=True)

    result = []
    for value, count in zip(unique_values, counts):
        if n < count < x:
            result.append(value)

    return np.array(result, dtype=arr.dtype)

def input_numpy_array() -> np.ndarray:
    length = int(input("Введіть довжину масиву: "))

    result = np.zeros(length, dtype=int)
    for i in range(length):
        result[i] = int(input(str(i) + " елемент:"))

    return result