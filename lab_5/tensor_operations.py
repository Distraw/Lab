import torch

def create_random_filled_tensor(width: int, height: int, low: int, high: int) -> torch.Tensor:
    return torch.randint(low=low, high=high, size=(width, height)).int()

def get_positive_numbers_amount(matrix: torch.Tensor) -> int:
    return (matrix > 0).sum().item()
