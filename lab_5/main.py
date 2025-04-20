import tensor_operations as t
import numpy as np

tensor1 = t.create_random_filled_tensor(3, 4, -5, 6)
tensor2 = t.create_random_filled_tensor(3, 4, -5, 6)
tensor3 = t.create_random_filled_tensor(3, 4, -5, 6)

print('1st matrix:\n', tensor1, '\n')
print('2nd matrix:\n', tensor2, '\n')
print('3rd matrix:\n', tensor3, '\n')

positive = {'1st matrix': t.get_positive_numbers_amount(tensor1),
                '2nd matrix': t.get_positive_numbers_amount(tensor2),
                '3rd matrix': t.get_positive_numbers_amount(tensor3)}
print(max(positive, key=positive.get), ' has most positive numbers')

# task 2
print('\n\nFirst 3 rows of 1st tensor:\n', tensor1[:3], '\n')

tensor2 = np.delete(tensor2, 2, axis=1)
tensor3 = np.delete(tensor3, 2, axis=1)

print('Matrix2:\n', tensor2, '\n')
print('Matrix3:\n', tensor3, '\n')