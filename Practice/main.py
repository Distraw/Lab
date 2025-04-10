import torch
import time

tensor_variable1 = torch.randn(1000, 1000, requires_grad=True)
tensor_variable2 = torch.randn(1000, 1000, requires_grad=True)
tensor_constant1 = torch.randn(1000, 1000)
tensor_constant2 = torch.randn(1000, 1000)

start_time = time.time()
result_variable = tensor_variable1 * tensor_variable2
end_time = time.time()
print('Множення, змінний: ', end_time - start_time)

start_time = time.time()
result_constant = tensor_constant1 * tensor_constant2
end_time = time.time()
print('Множення, константний: ', end_time - start_time)

start_time = time.time()
result_variable = tensor_variable1 * 50
end_time = time.time()
print('Скаляр, змінний: ', end_time - start_time)

start_time = time.time()
result_constant = tensor_constant1 * 50
end_time = time.time()
print('Скаляр, константний: ', end_time - start_time)

start_time = time.time()
result_variable = tensor_variable1[0, :]
end_time = time.time()
print('Підвибір, змінний: ', end_time - start_time)

start_time = time.time()
result_constant = tensor_constant1[0, :]
end_time = time.time()
print('Підвибір, константний: ', end_time - start_time)