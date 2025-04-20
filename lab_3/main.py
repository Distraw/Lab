import matrix_operations as m
import numpy as np

matrix1 = m.create_random_filled_matrix(3, 4, -5, 6)
matrix2 = m.create_random_filled_matrix(3, 4, -5, 6)
matrix3 = m.create_random_filled_matrix(3, 4, -5, 6)

print('1st matrix:\n', matrix1, '\n')
print('2nd matrix:\n', matrix2, '\n')
print('3rd matrix:\n', matrix3, '\n')

positive = {'1st matrix': m.get_positive_numbers_amount(matrix1),
                '2nd matrix': m.get_positive_numbers_amount(matrix2),
                '3rd matrix': m.get_positive_numbers_amount(matrix3)}
print(max(positive, key=positive.get), ' has most positive numbers')

# task 2
print('\n\nFirst 3 rows of 1st matrix:\n', matrix1[:3], '\n')

matrix2 = np.delete(matrix2, 2, axis=1)
matrix3 = np.delete(matrix3, 2, axis=1)

print('Matrix2:\n', matrix2, '\n')
print('Matrix3:\n', matrix3, '\n')