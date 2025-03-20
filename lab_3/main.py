from sympy.strategies.core import switch

import matrix_operations as m

matrix1 = m.create_random_filled_matrix(3, 4, -5, 6)
matrix2 = m.create_random_filled_matrix(3, 4, -5, 6)
matrix3 = m.create_random_filled_matrix(3, 4, -5, 6)

print(matrix1)
print(matrix2)
print(matrix3)

positive1 = m.get_positive_numbers_amount(matrix1)
positive2 = m.get_positive_numbers_amount(matrix2)
positive3 = m.get_positive_numbers_amount(matrix3)

print(max(positive1, positive2, positive3))