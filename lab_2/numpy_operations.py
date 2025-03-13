import numpy as np
from collections import Counter

def get_elements_occuring_in_range_from_n_to_x_times(arr: np.ndarray, n: int, x: int) -> np.ndarray:
    count_dict = Counter(arr)
    print(count_dict)
    return np.array([key for key, value in count_dict.items() if n < value < x])

def inputarray() -> np.ndarray:
    length = int(input("Введіть довжину масиву: "))

    result = np.zeros(length, dtype=int)
    for i in range(length):
        result[i] = int(input(str(i) + " елемент:"))

    return result