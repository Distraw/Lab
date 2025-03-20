import numpy as np

def create_random_filled_matrix(width: int, height: int, low: int, high: int) -> np.ndarray:
    return np.random.randint(low=low, high=high, size=(width, height))

def get_positive_numbers_amount(matrix: np.ndarray) -> int:
    return np.sum(matrix > 0)