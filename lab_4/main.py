import torch

# 1 task
my_tensor = torch.randint(0, 100, (10, 5))
new_tensor = my_tensor[my_tensor > my_tensor.mean(dtype=torch.float32)]

print("Оригінальний тензор: ", my_tensor)
print("Середнє значення: ", my_tensor.mean(dtype=torch.float32))
print("Фінальний тензор: ", new_tensor)

# 2 task
print("\n\n\n\n")
tensor1 = torch.randint(0, 100, (5, 5))
tensor2 = torch.randint(0, 100, (5, 5))

mask1 = tensor1 < tensor2
mask2 = tensor1 > tensor2


tensor_t1 = tensor1.masked_fill(mask1, 0)
tensor_t2 = tensor1.masked_fill(~mask2, 0)
# ~true = false ~false = true

print("t1: ", tensor1)
print("t2: ", tensor1)